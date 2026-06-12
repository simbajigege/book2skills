---
name: agent-tool-builder
description: "Define agent tools using the fail-closed design pattern — unified name/schema/security/execution in one class, with three-layer execution (validate → permission → call). Use this skill whenever the user wants to define a new agent tool, add permission or validation logic to an existing tool, or asks about 'build a tool', '定义一个工具', 'create a tool for X', '工具定义'. Framework-agnostic: works with hermes-agent, LangChain, or any Python agent framework."
---

# Agent Tool Builder

Helps define agent tools using the fail-closed design pattern:
a unified class that co-locates identity, schema, security properties, and execution logic,
with fail-closed defaults so new tools are safe by default.

## Why this pattern matters

Three things that ad-hoc tool definitions lack:
1. **Fail-closed defaults** — `is_read_only`, `is_destructive`, `is_concurrency_safe` all default to False.
   A tool that forgets to declare its properties is conservatively treated as write-capable.
2. **Layered execution** — `validate_semantics → check_permissions → _call` are separate methods,
   so validation logic doesn't bleed into permission logic or business logic.
3. **Self-contained definition** — schema, description, security metadata, and execution all live
   in one place. No separate middleware to wire up.

---

## Workflow

### Step 1 — Identify the target framework

Ask which agent framework the tool will be registered in (e.g. hermes-agent, LangChain, plain Python).
This determines the import path and registration method, but the design principles are identical.

Check if `agent_tool_base.py` exists in the project's utils/tools directory.
If not, copy it from `references/agent_tool_base.py` in this skill directory.
Tell the user where it was placed.

### Step 2 — Interview the user

Collect answers to these questions. Defaults are shown — skip questions where the default is clearly fine.

**Naming convention**: use `{service}_{action}_{resource}` format with a service prefix so the tool stays unambiguous when multiple tool sets are loaded simultaneously (e.g. `stock_get_price`, `stock_list_symbols`, `stock_search_news`). Start with a verb: `get`, `list`, `search`, `create`, `delete`.

| Field | Question | Default |
|---|---|---|
| `name` | 工具名（格式：`{service}_{action}_{resource}`，例如 `stock_get_price`） | — required |
| `description` | 给 LLM 看的一句话描述：**精确匹配**实际功能，不要模糊扩大，否则 agent 会在不该用的场景误调用 | — required |
| Schema fields | 工具接受哪些参数？（字段名、类型、说明；在 Field description 里加 example） | — required |
| `is_read_only` | 这个工具只读数据，不写入/不产生副作用吗？ | `False` |
| `is_destructive` | 这个工具会做不可逆操作（删除、覆盖）吗？ | `False` |
| `is_concurrency_safe` | 这个工具可以和其他工具同时运行吗？ | `False` |
| `response_format` | 返回数据是给 agent 程序化处理（JSON）还是给用户展示（Markdown）？ | 视场景，默认 Markdown |
| 是否列表工具 | 如果返回多条记录，要支持分页吗？ | 超过 50 条建议加 |
| `_validate_input_semantics` | 有没有需要在执行前拦截的语义问题？（如：参数太短、格式不对） | 不需要 |
| `_check_permissions` | 有没有需要检查的权限？（如：需要某个 env var、调用方身份限制） | 不需要 |
| `_call` | 工具的核心执行逻辑是什么？ | — required |

You don't have to ask all questions upfront — infer reasonable answers from context.
For example, a "search" or "get" tool is almost certainly `is_read_only=True, is_concurrency_safe=True`.

### Step 3 — Generate the tool file

Create a `.py` file for the tool. Follow this field order:

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

Suggest a file path consistent with the project's tool directory structure.

### Step 4 — Show security property summary

After generating, print a one-line summary of the tool's security posture:

```
StockGetPriceTool: read_only=True  destructive=False  concurrency_safe=True  max_result=10K
```

---

## Output template

```python
"""<tool_name>.py — <one-line description>"""

from typing import Optional
from pydantic import BaseModel, Field
from base.utils.agent_tool_base import AgentTool


# ---------------------------------------------------------------------------
# Input schema
# ---------------------------------------------------------------------------

class <ToolName>Input(BaseModel):
    <field_name>: <type> = Field(description="<description>. e.g. '<example>'")
    # ... more fields


# ---------------------------------------------------------------------------
# Tool class
# ---------------------------------------------------------------------------

class <ToolName>Tool(AgentTool):
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
    def _validate_input_semantics(self, <params>, **kwargs) -> tuple[bool, Optional[str]]:
        if not <condition>:
            return False, "<why invalid>. Try <concrete fix>"
        return True, None

    # — permission check (omit if no access control needed) —
    def _check_permissions(self, <params>, **kwargs) -> tuple[bool, Optional[str]]:
        if not <allowed>:
            return False, "<why denied>. <suggested next step>"
        return True, None

    # — core logic —
    def _call(self, <params>, **kwargs) -> str:
        # ... implement tool logic here
        return result
```

---

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

---

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

Any tool that can return more than ~50 records should support pagination:

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

Add `offset: int = Field(default=0, description="Pagination offset")` and `limit: int = Field(default=20, description="Max items to return")` to the input schema.

### Actionable error messages

Error strings must guide the agent toward a fix — not just describe the failure:

```python
# Bad: agent is stuck
return False, "Query too short."

# Good: agent knows exactly what to try next
return False, "Query too short (got 2 chars, need >= 3). Provide a more specific search term."
```

---

## Reference files

- `references/agent_tool_base.py` — 完整的 AgentTool 基类（纯 Python，无框架依赖）
