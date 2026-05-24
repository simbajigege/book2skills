---
name: compact-memory-implementation
description: Developer implementation guide for adding compact memory to an Agent — covers fork agent pattern for compaction, trigger strategy, summary format design, and memory restoration in subsequent sessions. Use when a developer asks how to implement compact memory, context compression, or memory persistence in their agent built with Claude Agent SDK or Anthropic API.
---

# compact-memory-implementation

A developer guide for building compact memory into an Agent: detect when to compress, fork a compactor sub-agent, produce a structured summary, and restore it in the next session.

## Step 1 — Understand the setup

Before designing anything, clarify:

- **SDK / language**: Claude Agent SDK? Direct Anthropic API? Python or TypeScript?
- **Agent architecture**: single-agent loop, multi-agent, tool-calling?
- **Session model**: one long-running session or multiple short sessions?
- **What must survive compaction**: task state, decisions, tool results, conversation history?

This determines which pattern fits.

---

## Step 2 — When to trigger compact

Three strategies, pick based on your session model:

**1. Token threshold** (recommended)
Check `usage.input_tokens` from the previous response. When it exceeds ~70–80% of your model's context limit, trigger compact.

```python
COMPACT_THRESHOLD = 150_000  # adjust per model

if response.usage.input_tokens > COMPACT_THRESHOLD:
    compact = compact_memory(history)
    history = []  # reset — compact moves to system prompt
```

**2. Turn count**
Compact every N turns. Simpler but less adaptive — misses sessions with a few very long turns.

```python
COMPACT_EVERY_N = 30

if turn_count % COMPACT_EVERY_N == 0:
    compact = compact_memory(history)
```

**3. Phase boundary**
Compact at natural task boundaries (after research, before implementation). Requires the agent to detect phases. Produces summaries that align with meaningful milestones, but harder to implement reliably.

**Recommended default**: token threshold at 70%, with turn-count fallback at N=40.

---

## Step 3 — Fork agent for compaction

The compactor is a **separate agent call** whose only job is to read the current state and return a structured summary. Fork it synchronously — the main agent waits for the result before continuing.

```python
def compact_memory(history: list[dict]) -> dict:
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",  # cheaper model is fine for compaction
        max_tokens=4096,
        system=COMPACTOR_SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": format_history_for_compact(history),
            }
        ],
    )
    return json.loads(response.content[0].text)
```

**Why fork instead of self-compact:**
- The main agent may have drifted in focus; the compactor starts fresh with the full picture
- Compaction is a different cognitive task — summarizing vs. executing
- A cheaper, smaller model (Haiku) can do compaction; save the expensive model for main work
- Clean separation makes the compact output easier to validate and test

---

## Step 4 — How to compact: format and prompt

### Compact output schema

```json
{
  "task": "What the agent is working on and why — the goal, not the steps",
  "current_state": "Exact status at compaction point: what is done, what is not, what is in progress",
  "key_decisions": [
    { "decision": "...", "reason": "...", "constraint": "..." }
  ],
  "eliminated_approaches": [
    { "approach": "...", "reason_ruled_out": "..." }
  ],
  "open_questions": ["..."],
  "next_steps": ["..."],
  "relevant_tool_results": {
    "key": "Only results future steps will need — summarized, not raw dumps"
  },
  "compacted_at_turn": 42
}
```

### Compactor system prompt

```
You are a conversation compactor. Read the provided conversation and produce a JSON summary that captures everything a fresh agent needs to continue the work without asking what happened.

Include:
- Current task and goal (not the steps taken to get here)
- Exact current state — what is done and what is not
- Decisions made and WHY (reasoning, not just the choice)
- Approaches tried and ruled out with reasons (prevents re-exploration)
- Open questions and blockers
- Concrete next steps in priority order
- Tool results that future steps will need (summarize, don't dump raw output)

Omit:
- Intermediate reasoning that led nowhere
- Completed sub-tasks with no future relevance
- Raw tool output that has already been acted on
- Anything derivable by reading the code or running a command

Output valid JSON matching the schema provided. No prose outside the JSON.
```

### Format history for compactor

```python
def format_history_for_compact(history: list[dict]) -> str:
    lines = ["Conversation to compact:\n"]
    for msg in history:
        role = msg["role"].upper()
        content = msg["content"] if isinstance(msg["content"], str) else "[tool use]"
        lines.append(f"[{role}]: {content[:2000]}")  # cap very long messages
    return "\n".join(lines)
```

---

## Step 5 — How to use after compacting: memory restoration

The compact object becomes the "memory" for the next turn or session. Inject it into the system prompt so it's always visible to the agent.

### Pattern A — System prompt injection (recommended)

```python
MEMORY_BLOCK_TEMPLATE = """
## Restored memory (compacted at turn {turn})

**Task**: {task}

**Current state**: {current_state}

**Key decisions**:
{decisions}

**Ruled out approaches**:
{eliminated}

**Next steps**:
{next_steps}

Begin from current state above. Do not re-explore eliminated approaches.
"""

def build_system_with_memory(base_system: str, compact: dict | None) -> str:
    if compact is None:
        return base_system
    memory = MEMORY_BLOCK_TEMPLATE.format(
        turn=compact["compacted_at_turn"],
        task=compact["task"],
        current_state=compact["current_state"],
        decisions="\n".join(f"- {d['decision']} (because {d['reason']})"
                            for d in compact["key_decisions"]),
        eliminated="\n".join(f"- {e['approach']}: {e['reason_ruled_out']}"
                             for e in compact["eliminated_approaches"]),
        next_steps="\n".join(f"- {s}" for s in compact["next_steps"]),
    )
    return base_system + "\n\n" + memory
```

### Pattern B — First message injection (for stateless API callers)

```python
messages = [
    {
        "role": "user",
        "content": f"[Resuming from compacted state — turn {compact['compacted_at_turn']}]\n"
                   f"{json.dumps(compact, indent=2)}\n\n"
                   f"Continue from the next steps listed above.",
    }
]
```

### Persistence across sessions

```python
import json, pathlib

MEMORY_DIR = pathlib.Path("memory")
MEMORY_DIR.mkdir(exist_ok=True)

def save_compact(session_id: str, compact: dict) -> None:
    (MEMORY_DIR / f"{session_id}.json").write_text(json.dumps(compact, indent=2))

def load_compact(session_id: str) -> dict | None:
    path = MEMORY_DIR / f"{session_id}.json"
    return json.loads(path.read_text()) if path.exists() else None
```

---

## Step 6 — Full agent loop

```python
def run_agent(session_id: str, user_input: str) -> str:
    compact = load_compact(session_id)
    system = build_system_with_memory(BASE_SYSTEM, compact)
    history = []
    turn = 0

    while True:
        response = client.messages.create(
            model="claude-opus-4-7",
            system=system,
            messages=history + [{"role": "user", "content": user_input}],
            max_tokens=8192,
        )

        # Trigger compact if context is growing too large
        if response.usage.input_tokens > COMPACT_THRESHOLD:
            compact = compact_memory(history)
            save_compact(session_id, compact)
            system = build_system_with_memory(BASE_SYSTEM, compact)
            history = []  # reset history — compact is now in system
            turn = 0
            continue

        if response.stop_reason == "end_turn":
            return response.content[0].text

        history.append({"role": "assistant", "content": response.content})
        user_input = handle_tool_calls(response)  # your tool dispatch
        turn += 1
```

---

## Step 7 — Chaining compacts across sessions

If a session resumes multiple times, don't stack compacts — re-compact instead:

```python
COMPACTOR_WITH_PRIOR = """
You are updating an existing memory compact with new information from a continuation session.

Prior compact:
{prior_compact}

New conversation turns since last compact:
{new_turns}

Produce an updated compact that:
- Merges both sources
- Removes resolved items and completed steps
- Adds new decisions, eliminations, and open questions
- Keeps next_steps current

Output valid JSON. No prose outside the JSON.
"""

def compact_memory_with_prior(history: list[dict], prior: dict) -> dict:
    prompt = COMPACTOR_WITH_PRIOR.format(
        prior_compact=json.dumps(prior, indent=2),
        new_turns=format_history_for_compact(history),
    )
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=4096,
        system=prompt,
        messages=[{"role": "user", "content": "Update the compact."}],
    )
    return json.loads(response.content[0].text)
```

---

## Common pitfalls

| Pitfall | Fix |
|---|---|
| Compact loses tool results needed later | Include summarized results in `relevant_tool_results` |
| Fresh session ignores compact | Inject into system prompt, not buried in messages |
| Compactor uses the same expensive model | Use Haiku for compaction, Opus for main work |
| Compact grows unbounded across sessions | Re-compact using "chaining compacts" pattern above |
| Compacting too often (every turn) | Use token threshold, not turn frequency |
| Compact JSON fails to parse | Add retry with explicit error feedback to compactor |
