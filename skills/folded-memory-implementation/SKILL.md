---
name: folded-memory-implementation
description: Developer implementation guide for building hierarchical (folded) memory into an Agent. Three-layer architecture where recent turns stay detailed, older content compresses into episodes, and the oldest distills into durable semantic facts. Use when compact-memory-implementation is not retaining enough, or when agents need to recall decisions from many sessions ago.
---

# folded-memory-implementation

A developer guide for hierarchical memory: instead of replacing history with a single flat summary, maintain three memory layers at different levels of detail. Old content is compressed more aggressively — not discarded. Each layer is independently stored and selectively recalled.

**Prerequisite**: read `compact-memory-implementation` first. Folded memory builds on the same fork-agent and trigger concepts.

---

## The core idea

```
L1 Working memory    [ turn 38..50 ] — raw turns, full detail, short window
L2 Episodic memory   [ turn 10..37 ] — compressed episodes, medium detail
L3 Semantic memory   [ turn 1..9  ] — abstract facts and decisions, sparse
```

When L1 fills up → fork an episode compactor → move oldest L1 turns into L2.
When L2 fills up → fork a semantic extractor → distill L2 into L3.

At each agent turn, inject the right combination of layers into the system prompt.

---

## Step 1 — Understand the setup

Same questions as `compact-memory-implementation`, plus:

- **How long do sessions run?** If sessions are short (<50 turns), flat compact is enough.
- **What kind of information ages badly?** Decisions and patterns age well (good for L3). Exact tool outputs age badly (keep only in L1 or summarize into L2).
- **Does the agent need to cite past reasoning?** If yes, L2/L3 must preserve decision rationale, not just conclusions.

---

## Step 2 — Three-layer architecture

### Layer 1 — Working memory

- **Content**: raw conversation turns, full fidelity
- **Window**: last N turns (e.g., 20 turns or ~30k tokens)
- **Trigger to flush**: when L1 exceeds its window, oldest turns move to L2
- **Injected as**: full message history in `messages[]`

### Layer 2 — Episodic memory

- **Content**: compressed episode summaries — what happened, what was decided, what was tried
- **Window**: up to M episodes (e.g., 10 episodes, each covering ~20 turns)
- **Trigger to flush**: when episode count exceeds M, oldest episodes distill into L3
- **Injected as**: structured block in system prompt

### Layer 3 — Semantic memory

- **Content**: abstract facts, stable decisions, eliminated approaches, domain knowledge learned
- **Window**: unbounded, but aggressively filtered — only durable knowledge
- **Trigger to flush**: never purged, but updated/merged when contradicted
- **Injected as**: compact block in system prompt, always present

---

## Step 3 — Data structures

```python
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Episode:
    episode_id: int
    turn_range: tuple[int, int]       # (start_turn, end_turn)
    summary: str
    decisions: list[dict]             # [{"decision": ..., "reason": ...}]
    eliminated: list[dict]            # [{"approach": ..., "why": ...}]
    open_questions: list[str]
    tool_results: dict[str, Any]      # summarized results worth keeping

@dataclass
class SemanticMemory:
    facts: list[str]                  # stable domain facts
    decisions: list[dict]             # durable decisions (never re-litigate)
    eliminated_approaches: list[dict] # things proven not to work
    patterns: list[str]               # recurring patterns observed

@dataclass
class FoldedMemory:
    semantic: SemanticMemory
    episodes: list[Episode]
    current_episode_id: int = 0
    total_turns_seen: int = 0
```

---

## Step 4 — Fork agent: L1 → L2 (episode compactor)

Triggered when working memory (L1) exceeds its window. Takes the oldest N turns and compresses them into one `Episode`.

```python
EPISODE_COMPACTOR_PROMPT = """
You are an episode compactor. Read the provided conversation turns and produce a structured Episode summary.

An Episode captures:
- What was attempted and what happened (not the full dialogue — the outcome)
- Decisions made and WHY (the reasoning behind them, not just the choice)
- Approaches tried and ruled out, with reasons (prevents re-exploration)
- Open questions that were not resolved
- Tool results that future turns will need (summarize, don't dump raw output)

Do NOT include:
- Intermediate back-and-forth that led to a conclusion (keep the conclusion, drop the path)
- Tool outputs that have already been acted on and have no future relevance
- Anything a fresh agent could derive by reading the code or running a command

Output valid JSON:
{
  "summary": "2-3 sentence narrative of what happened in this episode",
  "decisions": [{"decision": "...", "reason": "...", "constraint": "..."}],
  "eliminated": [{"approach": "...", "why": "..."}],
  "open_questions": ["..."],
  "tool_results": {"key": "summarized result"}
}
"""

def compact_l1_to_episode(turns: list[dict], episode_id: int, turn_range: tuple) -> Episode:
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=2048,
        system=EPISODE_COMPACTOR_PROMPT,
        messages=[{"role": "user", "content": format_turns(turns)}],
    )
    data = json.loads(response.content[0].text)
    return Episode(
        episode_id=episode_id,
        turn_range=turn_range,
        **data,
    )
```

---

## Step 5 — Fork agent: L2 → L3 (semantic extractor)

Triggered when the episode count exceeds the L2 window. Takes the oldest episodes and distills durable knowledge into `SemanticMemory`.

```python
SEMANTIC_EXTRACTOR_PROMPT = """
You are a semantic memory extractor. Read the provided episode summaries and extract only
knowledge that is durable — facts, decisions, and patterns that will still matter many
sessions from now.

Extract:
- Stable domain facts discovered ("the API always returns 200 even on failure — check data.success")
- Decisions that should never be re-litigated ("chose optimistic locking because DB doesn't support SELECT FOR UPDATE")
- Approaches definitively ruled out ("tried polling every 5s — causes rate limiting, don't retry")
- Recurring patterns that should inform future behavior

Do NOT extract:
- Task-specific state that will be resolved (current blockers, in-progress work)
- Results tied to a specific turn or tool call
- Anything that changes frequently

Merge with the existing semantic memory provided — update facts that were contradicted,
remove decisions that are now resolved, add new ones.

Output valid JSON:
{
  "facts": ["..."],
  "decisions": [{"decision": "...", "reason": "...", "constraint": "..."}],
  "eliminated_approaches": [{"approach": "...", "why": "..."}],
  "patterns": ["..."]
}
"""

def distill_episodes_to_semantic(
    episodes: list[Episode],
    existing_semantic: SemanticMemory,
) -> SemanticMemory:
    payload = {
        "existing_semantic": asdict(existing_semantic),
        "episodes_to_distill": [asdict(e) for e in episodes],
    }
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=2048,
        system=SEMANTIC_EXTRACTOR_PROMPT,
        messages=[{"role": "user", "content": json.dumps(payload, indent=2)}],
    )
    data = json.loads(response.content[0].text)
    return SemanticMemory(**data)
```

---

## Step 6 — When to trigger each layer

```python
L1_MAX_TURNS = 20        # working memory window
L2_MAX_EPISODES = 8      # episodic memory window

def maybe_fold(memory: FoldedMemory, l1_turns: list[dict]) -> tuple[FoldedMemory, list[dict]]:
    """Check thresholds and fold layers if needed. Returns updated memory and remaining L1."""

    # L1 → L2: flush oldest turns when L1 is full
    if len(l1_turns) >= L1_MAX_TURNS:
        flush_count = L1_MAX_TURNS // 2             # flush half, keep recent half
        turns_to_flush = l1_turns[:flush_count]
        turn_range = (
            memory.total_turns_seen - len(l1_turns),
            memory.total_turns_seen - len(l1_turns) + flush_count - 1,
        )
        episode = compact_l1_to_episode(
            turns_to_flush,
            episode_id=memory.current_episode_id,
            turn_range=turn_range,
        )
        memory.episodes.append(episode)
        memory.current_episode_id += 1
        l1_turns = l1_turns[flush_count:]           # keep the recent half

    # L2 → L3: distill oldest episodes when L2 is full
    if len(memory.episodes) >= L2_MAX_EPISODES:
        flush_count = L2_MAX_EPISODES // 2
        episodes_to_distill = memory.episodes[:flush_count]
        memory.semantic = distill_episodes_to_semantic(episodes_to_distill, memory.semantic)
        memory.episodes = memory.episodes[flush_count:]

    return memory, l1_turns
```

---

## Step 7 — Recall: build system prompt from layers

Inject L3 always. Inject L2 episodes as a digest. L1 goes into the `messages[]` array directly.

```python
def build_system_with_folded_memory(base_system: str, memory: FoldedMemory) -> str:
    blocks = [base_system]

    # L3 — always present
    if memory.semantic.facts or memory.semantic.decisions:
        blocks.append(_format_semantic(memory.semantic))

    # L2 — episode digest (most recent episodes first)
    if memory.episodes:
        blocks.append(_format_episodes(memory.episodes))

    return "\n\n".join(blocks)

def _format_semantic(s: SemanticMemory) -> str:
    lines = ["## Semantic memory (durable knowledge)"]
    if s.facts:
        lines += ["**Facts**:"] + [f"- {f}" for f in s.facts]
    if s.decisions:
        lines += ["**Decisions**:"] + [f"- {d['decision']} (because {d['reason']})" for d in s.decisions]
    if s.eliminated_approaches:
        lines += ["**Ruled out**:"] + [f"- {e['approach']}: {e['why']}" for e in s.eliminated_approaches]
    if s.patterns:
        lines += ["**Patterns**:"] + [f"- {p}" for p in s.patterns]
    return "\n".join(lines)

def _format_episodes(episodes: list[Episode]) -> str:
    lines = ["## Episode memory (recent history, oldest → newest)"]
    for ep in episodes:
        lines.append(f"\n### Episode {ep.episode_id} (turns {ep.turn_range[0]}–{ep.turn_range[1]})")
        lines.append(ep.summary)
        if ep.decisions:
            lines += ["Decisions:"] + [f"- {d['decision']}" for d in ep.decisions]
        if ep.open_questions:
            lines += ["Open:"] + [f"- {q}" for q in ep.open_questions]
    return "\n".join(lines)
```

---

## Step 8 — Full agent loop

```python
def run_agent(session_id: str, user_input: str) -> str:
    memory = load_folded_memory(session_id)   # returns empty FoldedMemory if new session
    l1_turns = []

    while True:
        system = build_system_with_folded_memory(BASE_SYSTEM, memory)

        response = client.messages.create(
            model="claude-opus-4-7",
            system=system,
            messages=l1_turns + [{"role": "user", "content": user_input}],
            max_tokens=8192,
        )
        memory.total_turns_seen += 1

        # Fold if needed
        l1_turns.append({"role": "user", "content": user_input})
        l1_turns.append({"role": "assistant", "content": response.content[0].text})
        memory, l1_turns = maybe_fold(memory, l1_turns)

        save_folded_memory(session_id, memory, l1_turns)

        if response.stop_reason == "end_turn":
            return response.content[0].text

        user_input = handle_tool_calls(response)
```

---

## Step 9 — Persistence

```python
import json, pathlib
from dataclasses import asdict

MEMORY_DIR = pathlib.Path("memory")

def save_folded_memory(session_id: str, memory: FoldedMemory, l1_turns: list[dict]) -> None:
    MEMORY_DIR.mkdir(exist_ok=True)
    (MEMORY_DIR / f"{session_id}_folded.json").write_text(
        json.dumps({"memory": asdict(memory), "l1_turns": l1_turns}, indent=2)
    )

def load_folded_memory(session_id: str) -> tuple[FoldedMemory, list[dict]]:
    path = MEMORY_DIR / f"{session_id}_folded.json"
    if not path.exists():
        return FoldedMemory(semantic=SemanticMemory([], [], [], [])), []
    data = json.loads(path.read_text())
    memory = FoldedMemory(
        semantic=SemanticMemory(**data["memory"]["semantic"]),
        episodes=[Episode(**e) for e in data["memory"]["episodes"]],
        current_episode_id=data["memory"]["current_episode_id"],
        total_turns_seen=data["memory"]["total_turns_seen"],
    )
    return memory, data["l1_turns"]
```

---

## When to use folded memory vs. flat compact

| Situation | Use |
|---|---|
| Sessions under ~50 turns | `compact-memory-implementation` |
| Context overflows but information loss is acceptable | `compact-memory-implementation` |
| Agent runs for hundreds of turns across many sessions | folded memory |
| Decisions from 10 sessions ago must still be retrievable | folded memory |
| Domain knowledge accumulates and shouldn't be re-learned | folded memory |
| Team is just getting started with agent memory | `compact-memory-implementation` first |

---

## Common pitfalls

| Pitfall | Fix |
|---|---|
| L3 grows unbounded with low-quality facts | Set a quality bar in the extractor prompt: "only extract if it will matter 10 sessions from now" |
| Episodes lose tool results needed later | Include summarized results in `Episode.tool_results` |
| System prompt gets too long with all three layers | Cap L2 to 5 most recent episodes; L3 to 20 items max |
| Semantic memory contradicts itself across updates | Include prior semantic in extractor input and instruct it to merge, not append |
| Folding too eagerly (every turn) | L1 window should be at least 15–20 turns |
