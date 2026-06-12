"""
agent_tool_base.py — Framework-agnostic agent tool base class

Brings Claude Code's buildTool() pattern to any Python agent framework:
  - Fail-closed security defaults (all False unless explicitly declared True)
  - Three-layer execution: validate_semantics → check_permissions → _call
  - Self-contained tool definition: schema, description, security in one class

Usage:
  1. Subclass AgentTool for full control.
  2. Use build_tool() factory for quick one-off tools.
  3. Adapt to your framework's registration API (LangChain, hermes-agent, etc.)
     by wrapping or subclassing alongside your framework's base tool class.
"""

from abc import ABC, abstractmethod
from typing import Any, Optional, Type, Callable

from pydantic import BaseModel


# ---------------------------------------------------------------------------
# Base tool class
# ---------------------------------------------------------------------------

class AgentTool(ABC):
    """
    Framework-agnostic tool base class with Claude Code's three-layer execution pattern.

    Security properties — all default False (fail-closed):
      is_read_only:        True → tool only reads data, no writes or side effects
      is_destructive:      True → tool can perform irreversible operations (delete, overwrite)
      is_concurrency_safe: True → tool can run simultaneously with others without data races
      max_result_chars:    Output beyond this is truncated to protect the LLM context window

    Execution order inside run():
        1. _validate_input_semantics(**kwargs)  — catch bad input early, before any I/O
        2. _check_permissions(**kwargs)         — authorization, env var checks, etc.
        3. _call(**kwargs)                      — actual tool work

    Both hooks default to (True, None) — override only the layers you need.
    Separation matters:
      - validation  = "is this input sensible?"
      - permissions = "is this caller allowed?"
      - _call       = "do the work"

    Example subclass:

        class StockGetPriceTool(AgentTool):
            name = "stock_get_price"
            description = "Get the latest price for a stock symbol."
            args_schema = StockGetPriceInput
            is_read_only = True
            is_concurrency_safe = True

            def _validate_input_semantics(self, symbol: str, **kwargs):
                if not symbol.strip():
                    return False, "symbol is required. e.g. 'AAPL'"
                return True, None

            def _call(self, symbol: str, **kwargs) -> str:
                price = fetch_price(symbol)
                return f"**{symbol}** latest price: ${price}"
    """

    name: str = ""
    description: str = ""
    args_schema: Optional[Type[BaseModel]] = None

    # Security metadata — fail-closed defaults
    is_read_only: bool = False
    is_destructive: bool = False
    is_concurrency_safe: bool = False
    max_result_chars: int = 10_000

    def run(self, **kwargs: Any) -> str:
        """Entry point. Runs all three layers in order."""

        # Layer 1: semantic validation (fast, no I/O)
        valid, msg = self._validate_input_semantics(**kwargs)
        if not valid:
            return f"[ValidationError] {msg}"

        # Layer 2: permission check (may involve I/O — env vars, role checks, etc.)
        allowed, reason = self._check_permissions(**kwargs)
        if not allowed:
            return f"[PermissionDenied] {reason}"

        # Layer 3: actual execution
        result = self._call(**kwargs)

        # Truncate large results to protect the LLM context window
        if isinstance(result, str) and len(result) > self.max_result_chars:
            result = (
                result[: self.max_result_chars]
                + f"\n...[output truncated — {len(result)} chars total, showing first {self.max_result_chars}]"
            )

        return result

    def _validate_input_semantics(self, **kwargs) -> tuple[bool, Optional[str]]:
        """
        Override to add semantic validation before any execution or I/O.

        Return (True, None) to proceed.
        Return (False, "reason") to block with a ValidationError message.

        Good for: input length/format checks, required-field presence,
        blocking known-bad patterns (e.g. empty symbol, invalid date format).
        """
        return True, None

    def _check_permissions(self, **kwargs) -> tuple[bool, Optional[str]]:
        """
        Override to add permission checks after validation but before execution.

        Return (True, None) to allow.
        Return (False, "reason") to deny with a PermissionDenied message.

        Good for: API key presence checks, role-based access,
        rate limiting guards, allowlist enforcement.
        """
        return True, None

    @abstractmethod
    def _call(self, **kwargs) -> str:
        """Implement the actual tool logic here. Return a string result."""
        ...

    def get_schema(self) -> dict:
        """Return OpenAI-compatible function schema for this tool."""
        if self.args_schema is None:
            return {
                "name": self.name,
                "description": self.description,
                "parameters": {"type": "object", "properties": {}, "required": []},
            }
        schema = self.args_schema.model_json_schema()
        return {
            "name": self.name,
            "description": self.description,
            "parameters": schema,
        }


# ---------------------------------------------------------------------------
# build_tool() factory — for quick one-off tools without subclassing
# ---------------------------------------------------------------------------

def build_tool(
    name: str,
    description: str,
    args_schema: Type[BaseModel],
    call_fn: Callable,
    *,
    is_read_only: bool = False,
    is_destructive: bool = False,
    is_concurrency_safe: bool = False,
    max_result_chars: int = 10_000,
    validate_fn: Optional[Callable] = None,
    permission_fn: Optional[Callable] = None,
) -> AgentTool:
    """
    Factory for creating AgentTool instances without subclassing.

    Args:
        name:                Tool identifier (snake_case, shown to LLM)
        description:         One-sentence description for the LLM
        args_schema:         Pydantic BaseModel defining input parameters
        call_fn:             Callable(**kwargs) -> str — the actual tool logic
        is_read_only:        True if tool only reads (default: False)
        is_destructive:      True if tool can cause irreversible changes (default: False)
        is_concurrency_safe: True if safe to run in parallel (default: False)
        max_result_chars:    Truncate output beyond this length (default: 10_000)
        validate_fn:         Optional callable(**kwargs) -> (bool, str|None)
        permission_fn:       Optional callable(**kwargs) -> (bool, str|None)

    Example:
        my_tool = build_tool(
            name="stock_get_price",
            description="Get the latest price for a stock symbol.",
            args_schema=StockGetPriceInput,
            call_fn=lambda symbol, **_: fetch_price(symbol),
            is_read_only=True,
            is_concurrency_safe=True,
        )
    """

    class _BuiltTool(AgentTool):
        def _call(self, **kwargs) -> str:
            return call_fn(**kwargs)

        def _validate_input_semantics(self, **kwargs):
            return validate_fn(**kwargs) if validate_fn else (True, None)

        def _check_permissions(self, **kwargs):
            return permission_fn(**kwargs) if permission_fn else (True, None)

    tool = _BuiltTool()
    tool.name = name
    tool.description = description
    tool.args_schema = args_schema
    tool.is_read_only = is_read_only
    tool.is_destructive = is_destructive
    tool.is_concurrency_safe = is_concurrency_safe
    tool.max_result_chars = max_result_chars

    _BuiltTool.__name__ = "".join(w.title() for w in name.split("_")) + "Tool"

    return tool
