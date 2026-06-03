# LangChain Tool Builder

Build LangChain (Python) tools using Claude Code's fail-closed design pattern — a unified class that co-locates identity, schema, security properties, and execution logic, with automatic three-layer execution (validate → permission → call).

## What It Does

- Installs the `ClaudeStyleTool` base class into your project (one-time setup)
- Interviews you on tool name, description, schema, and security properties
- Generates a fully structured `.py` tool file with correct field ordering
- Prints a security posture summary to verify fail-closed defaults at a glance
- Supports both class-based tools (`ClaudeStyleTool`) and factory-based tools (`build_tool()`)

## When to Use It

Trigger phrases and scenarios that activate this skill:

- "build a tool for X" / "create a LangChain tool"
- "定义一个工具" / "工具定义"
- "Claude Code style tool" / "build_tool"
- "add permission logic to a tool" / "add validation to a tool"
- Setting up `ClaudeStyleTool` base class in a new project
- Any LangChain Python project where you need a new agent tool

## Installation

### Option 1 — CLI (recommended)

```bash
npx skills add simbajigege/book2skills/skills/langchain-tool-builder
```

### Option 2 — Manual upload

1. Download the skill folder (or clone this repo).
2. In Claude.ai, go to **Settings → Skills** and upload the folder.
3. The skill will appear in your available skills list.

## File Structure

```
langchain-tool-builder/
├── SKILL.md          # Main skill instructions
├── README.md         # This file
└── LICENSE           # License
```

## License

MIT — free to use, modify, and distribute.
