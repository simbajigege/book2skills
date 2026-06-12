# Agent Tool Builder

A skill that helps you define agent tools using the fail-closed design pattern — unified name, schema, security metadata, and execution logic in one class, with three-layer execution (validate → permission → call). Framework-agnostic: works with hermes-agent, LangChain, or any Python agent framework.

## What It Does

- Guides you through defining a new tool with correct security properties (fail-closed defaults)
- Generates a complete `.py` file with input schema, security metadata, and three-layer execution logic
- Asks targeted questions to determine `is_read_only`, `is_destructive`, `is_concurrency_safe`
- Prints a one-line security posture summary after generation

## When to Use It

- "Build a tool for X"
- "Define a new agent tool"
- "Add permission / validation logic to this tool"
- "Create a tool for my LangChain agent"
- "定义一个工具" / "创建一个工具"

## Installation

### Option 1 — CLI (recommended)

```bash
npx skills add simbajigege/book2skills/skills/agent-tool-builder
```

### Option 2 — Manual upload

1. Download the skill folder (or clone this repo).
2. In Claude.ai, go to **Settings → Skills** and upload the folder.
3. The skill will appear in your available skills list.

## File Structure

```
agent-tool-builder/
├── SKILL.md              # Main skill instructions
├── README.md             # This file
├── references/
│   └── agent_tool_base.py  # AgentTool base class (copy into your project)
```

## License

For personal and educational use. This skill encodes a tool-definition design pattern — not a reproduction of any copyrighted source material.
