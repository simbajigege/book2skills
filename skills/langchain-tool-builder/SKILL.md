---
name: langchain-tool-builder
description: Build LangChain (Python) tools using Claude Code's fail-closed design pattern — unified name/schema/security/execution in one class, with automatic three-layer execution (validate → permission → call). Use this skill whenever the user wants to define a new LangChain tool, add permission or validation logic to an existing tool, set up the ClaudeStyleTool base class in a project, or asks about "build_tool", "Claude Code style tool", "工具定义", or "langchain tool with permissions". Also trigger when the user says "create a tool for X" or "定义一个工具" in a LangChain Python project context, even without mentioning Claude Code explicitly.
---

# LangChain Tool Builder

Helps define LangChain (Python) tools using Claude Code's `buildTool()` pattern:
a unified class that co-locates identity, schema, security properties, and execution logic,
with fail-closed defaults so new tools are safe by default.

## Why this pattern matters

Claude Code enforces three things that vanilla LangChain tools lack:
1. **Fail-closed defaults** — `is_read_only`, `is_destructive`, `is_concurrency_safe` all default to False.
   A tool that forgets to declare its properties is conservatively treated as write-capable.
2. **Layered execution** — `validate_semantics → check_permissions → _call` are separate methods,
   so validation logic doesn't bleed into permission logic or business logic.
3. **Self-contained definition** — schema, description, security metadata, and execution all live
   in one class. No separate permission middleware to wire up.

## Workflow

### Step 1 — Install the base class

Check if `claude_style_tool.py` exists in the project's utils directory.
The expected location for the `ai-base` project is:
`/Users/jigege/ai-base/backend/base/utils/claude_style_tool.py`

If it doesn't exist, copy it from `references/claude_style_tool.py` in this skill directory.
Tell the user where it was placed and what it provides.

If working in a different project, ask the user where their utils/tools directory is.

### Step 2 — Interview the user

Collect answers to these questions. Defaults are shown — skip questions where the default is clearly fine.

**Naming convention**: use `{service}_{action}_{resource}` format with a service prefix so the tool stays unambiguous when multiple tool sets are loaded simultaneously (e.g. `stock_get_price`, `stock_list_symbols`, `github_create_issue`). Start with a verb: `get`, `list`, `search`, `create`, `delete`.

| Field | Question | Default |
|---|---|---|
| `name` | 工具名（格式：`{service}_{action}_{resource}`，例如 `stock_get_price`） | — required |
| `description` | 给 LLM 看的一句话描述：**精确匹配**实际功能，不要模糊扩大，否则 agent 会在不该用的场景误调用 | — required |
| Schema fields | 工具接受哪些参数？（字段名、类型、说明；在 Field description 里加 example，如 `e.g. '2024-01-01'`） | — required |
| `is_read_only` | 这个工具只读数据，不写入/不产生副作用吗？ | `False` |
| `is_destructive` | 这个工具会做不可逆操作（删除、覆盖）吗？ | `False` |
| `is_concurrency_safe` | 这个工具可以和其他工具同时运行吗？ | `False` |
| `response_format` | 返回数据是给 agent 程序化处理（JSON）还是给用户展示（Markdown）？ | 视场景，默认 Markdown |
| 是否列表工具 | 如果返回多条记录，要支持分页吗？ | 超过 50 条建议加 |
| `_validate_input_semantics` | 有没有需要在执行前拦截的语义问题？（如：参数太短、路径格式不对） | 不需要 |
| `_check_permissions` | 有没有需要检查的权限？（如：只允许读特定路径、需要某个 env var） | 不需要 |
| `_call` | 工具的核心执行逻辑是什么？ | — required |

You don't have to ask all questions upfront — you can infer reasonable answers from context.
For example, a "search" tool is almost certainly `is_read_only=True, is_concurrency_safe=True`.

### Step 3 — Generate the tool file

Create a `.py` file for the tool. Follow this field order (matches Claude Code's BashTool):

```
1. imports
2. Input schema (Pydantic BaseModel)
3. Tool class:
   a. name, description, args_schema      — identity
   b. is_read_only, is_destructive, is_concurrency_safe, max_result_chars  — security metadata
   c. _validate_input_semantics()         — semantic validation (omit if unneeded)
   d. _check_permissions()               — permission check (omit if unneeded)
   e. _call()                            — actual logic
```

Suggest a file path consistent with the project's tool/agent directory structure.
For `ai-base`, suggest: `/Users/jigege/ai-base/backend/base/tools/<tool_name>.py`

### Step 4 — Show security property summary

After generating, print a one-line summary of the tool's security posture:

```
SearchDocsTool: read_only=True  destructive=False  concurrency_safe=True  max_result=10K
```

This helps the user quickly verify the fail-closed properties are set correctly.

---

## Output template

Use this structure when generating the tool file. Adjust based on what the user actually needs.

```python
"""<tool_name>.py — <one-line description>"""

from typing import Optional
from pydantic import BaseModel, Field
from base.utils.claude_style_tool import ClaudeStyleTool


# ---------------------------------------------------------------------------
# Input schema
# ---------------------------------------------------------------------------

class <ToolName>Input(BaseModel):
    <field_name>: <type> = Field(description="<description>")
    # ... more fields


# ---------------------------------------------------------------------------
# Tool class
# ---------------------------------------------------------------------------

class <ToolName>Tool(ClaudeStyleTool):
    # — identity —
    name: str = "<tool_name>"
    description: str = "<one-sentence description for the LLM>"
    args_schema = <ToolName>Input

    # — security metadata (fail-closed: only set True when verified) —
    is_read_only: bool = <True/False>
    is_destructive: bool = <True/False>
    is_concurrency_safe: bool = <True/False>
    max_result_chars: int = 10_000

    # — semantic validation (omit if no input constraints needed) —
    def _validate_input_semantics(self, <params>) -> tuple[bool, Optional[str]]:
        if not <condition>:
            # Error messages must be actionable: tell the agent WHAT to do next
            return False, "<why invalid>. Try <concrete fix, e.g. 'use filter=active_only'>"
        return True, None

    # — permission check (omit if no access control needed) —
    def _check_permissions(self, <params>) -> tuple[bool, Optional[str]]:
        if not <allowed>:
            return False, "<why denied>. <suggested next step>"
        return True, None

    # — core logic —
    def _call(self, <params>, **kwargs) -> str:
        # ... implement tool logic here
        return result
```

## Using build_tool() for simple tools

When the tool has no custom validation or permission logic, `build_tool()` is cleaner:

```python
from base.utils.claude_style_tool import build_tool
from pydantic import BaseModel, Field

class SearchInput(BaseModel):
    query: str = Field(description="Search query string")

search_tool = build_tool(
    name="search_docs",
    description="Search the documentation index for relevant content.",
    args_schema=SearchInput,
    call_fn=lambda query, **_: search_index(query),
    is_read_only=True,
    is_concurrency_safe=True,
)
```

## Common security property patterns

| Tool type | is_read_only | is_destructive | is_concurrency_safe |
|---|---|---|---|
| 搜索 / 查询 | `True` | `False` | `True` |
| 文件读取 | `True` | `False` | `True` |
| 文件写入 / 修改 | `False` | `False` | `False` |
| 删除操作 | `False` | `True` | `False` |
| API 调用（GET） | `True` | `False` | `True` |
| API 调用（POST/DELETE） | `False` | 视情况 | `False` |
| 数据库查询 | `True` | `False` | `True` |
| 数据库写入 | `False` | `False` | `False` |

## Output design principles

### Atomic tools — one tool, one responsibility

Keep each tool focused on a single operation. Let the agent compose multiple tools to complete complex tasks. A tool that does too much is harder for the agent to reuse and reason about.

### Response format — JSON vs Markdown

| Format | When to use |
|---|---|
| JSON | Agent needs to parse/filter the result programmatically |
| Markdown | Result will be shown directly to a user |

Support both when uncertain — accept an optional `response_format: str = "markdown"` parameter and branch in `_call`. For JSON output use `json.dumps(data, ensure_ascii=False, indent=2)`.

### Pagination for list tools

Any tool that can return more than ~50 records should support pagination. Return a dict with these fields so the agent knows when to continue fetching:

```python
return json.dumps({
    "items": [...],
    "total": 150,
    "count": 20,
    "offset": 0,
    "has_more": True,
    "next_offset": 20,
}, ensure_ascii=False, indent=2)
```

Add `offset: int = Field(default=0, description="Pagination offset")` and `limit: int = Field(default=20, description="Max items to return, default 20")` to the input schema.

### Actionable error messages

Error strings returned from `_validate_input_semantics` and `_check_permissions` must guide the agent toward a fix — not just describe the failure:

```python
# Bad: agent is stuck
return False, "Query too short."

# Good: agent knows exactly what to try next
return False, "Query too short (got 2 chars, need ≥ 3). Provide a more specific search term."
```

---

## Reference files

- `references/claude_style_tool.py` — 完整的 ClaudeStyleTool 基类和 build_tool() 工厂函数
  安装路径：`/Users/jigege/ai-base/backend/base/utils/claude_style_tool.py`
