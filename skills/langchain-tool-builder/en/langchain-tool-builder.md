---
title: "LangChain Tool Builder"
author: "simbajigege"
book_code: "langchain-tool-builder"
description: "Build LangChain (Python) tools using Claude Code's fail-closed design pattern — unified name, schema, security, and execution in one class, with automatic three-layer execution (validate → permission → call). New tools are safe by default."
tagline: "One class, one tool — fail-closed security properties, three-layer execution automatic"
tags: ["LangChain", "Python", "AI engineering", "tool definition", "Claude Code", "agent tools"]
cover_url: "/assets/books/covers/book-indigo.svg"
github_url: "https://github.com/simbajigege/book2skills/skills/langchain-tool-builder"
download_url: "/skills/langchain-tool-builder.zip"
related_skills: []
examples:
  - human: |
      I'm building a LangChain agent for internal developer tooling. I need a tool that searches our GitHub repos by keyword (calls the GitHub Search API), returns repo name, description, and star count. It's read-only and safe to run concurrently. Can you scaffold it?
    ai: |
      Sure. A search tool over a read-only API maps cleanly to `is_read_only=True`, `is_concurrency_safe=True`, `is_destructive=False`.

      First, let me check if the base class is already in place:

      ```bash
      ls backend/utils/claude_style_tool.py
      ```

      Found it. Here's the generated tool:

      **Suggested path:** `backend/tools/github_search_repos.py`

      ```python
      """github_search_repos.py — Search GitHub repositories by keyword"""

      import os, json, requests
      from typing import Optional
      from pydantic import BaseModel, Field
      from base.utils.claude_style_tool import ClaudeStyleTool


      class GithubSearchReposInput(BaseModel):
          query: str = Field(description="GitHub search keyword. e.g. 'langchain tool builder'")
          limit: int = Field(default=10, description="Max results (1–30). Default 10.")


      class GithubSearchReposTool(ClaudeStyleTool):
          name: str = "github_search_repos"
          description: str = "Search GitHub repositories by keyword. Returns repo name, description, and star count. Read-only."
          args_schema = GithubSearchReposInput

          is_read_only: bool = True
          is_destructive: bool = False
          is_concurrency_safe: bool = True
          max_result_chars: int = 8_000

          def _validate_input_semantics(self, query: str, limit: int) -> tuple[bool, Optional[str]]:
              if len(query.strip()) < 2:
                  return False, "query too short (< 2 chars). Provide a more specific search term."
              if not (1 <= limit <= 30):
                  return False, f"limit must be 1–30, got {limit}."
              return True, None

          def _call(self, query: str, limit: int = 10, **kwargs) -> str:
              token = os.getenv("GITHUB_TOKEN", "")
              headers = {"Authorization": f"Bearer {token}"} if token else {}
              resp = requests.get(
                  "https://api.github.com/search/repositories",
                  params={"q": query, "per_page": limit, "sort": "stars"},
                  headers=headers, timeout=10,
              )
              resp.raise_for_status()
              items = resp.json().get("items", [])
              results = [{"name": r["full_name"], "description": r.get("description", ""), "stars": r["stargazers_count"]} for r in items]
              return json.dumps(results, ensure_ascii=False, indent=2)
      ```

      Security summary:

      ```
      GithubSearchReposTool: read_only=True  destructive=False  concurrency_safe=True  max_result=8K
      ```

  - human: |
      Now I need a write tool: the agent should be able to create a GitHub issue in a specified repo. It should only be allowed to create issues in repos under the `my-org` organization.
    ai: |
      Creating an issue is a POST — so `is_read_only=False`. It's not irreversible, so `is_destructive=False`. Concurrent creation can cause duplicates, so `is_concurrency_safe=False`. The org restriction goes in `_check_permissions`.

      **Suggested path:** `backend/tools/github_create_issue.py`

      ```python
      """github_create_issue.py — Create a GitHub issue, restricted to my-org repos"""

      import os, json, requests
      from typing import Optional
      from pydantic import BaseModel, Field
      from base.utils.claude_style_tool import ClaudeStyleTool

      ALLOWED_ORG = "my-org"


      class GithubCreateIssueInput(BaseModel):
          repo: str = Field(description="Full repo name. e.g. 'my-org/backend-api'")
          title: str = Field(description="Issue title.")
          body: str = Field(default="", description="Issue body in Markdown. Optional.")


      class GithubCreateIssueTool(ClaudeStyleTool):
          name: str = "github_create_issue"
          description: str = "Create a GitHub issue. Only allowed for repos under the my-org organization."
          args_schema = GithubCreateIssueInput

          is_read_only: bool = False
          is_destructive: bool = False
          is_concurrency_safe: bool = False
          max_result_chars: int = 1_000

          def _check_permissions(self, repo: str, title: str, body: str) -> tuple[bool, Optional[str]]:
              org = repo.split("/")[0]
              if org != ALLOWED_ORG:
                  return False, f"Only '{ALLOWED_ORG}' repos allowed. Got org '{org}'. Use '{ALLOWED_ORG}/your-repo'."
              return True, None

          def _call(self, repo: str, title: str, body: str = "", **kwargs) -> str:
              token = os.environ["GITHUB_TOKEN"]
              resp = requests.post(
                  f"https://api.github.com/repos/{repo}/issues",
                  headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"},
                  json={"title": title, "body": body}, timeout=10,
              )
              resp.raise_for_status()
              data = resp.json()
              return json.dumps({"issue_number": data["number"], "url": data["html_url"]}, indent=2)
      ```

      Security summary:

      ```
      GithubCreateIssueTool: read_only=False  destructive=False  concurrency_safe=False  max_result=1K
      ```
---

# LangChain Tool Builder

Writing LangChain tools by hand has a subtle failure mode: security properties end up scattered — permission logic bleeds into execution logic, a new tool forgets to set `is_read_only` and becomes implicitly write-capable. This skill applies Claude Code's `buildTool()` pattern to fix this at the source: one class co-locates identity, schema, security metadata, and execution, and new tools are fail-closed safe by default.

## Core Framework

| Layer | Method | Responsibility |
|---|---|---|
| Security metadata | Class attributes | `is_read_only`, `is_destructive`, `is_concurrency_safe` — all default False (fail-closed) |
| Semantic validation | `_validate_input_semantics` | Reject malformed inputs before execution; error messages must be actionable |
| Permission check | `_check_permissions` | Reject unauthorized access (path traversal, missing env vars, wrong org) |
| Core logic | `_call` | Business execution — only runs after the first two layers pass |

## Supported Query Types

- "Build a tool to search / query / create / delete X"
- "Add permission checking to this tool"
- "Add input validation to this tool"
- "Set up ClaudeStyleTool base class in my project"
- "build_tool" / "Claude Code style tool" / "create a LangChain tool"

## How to Use

1. Open Claude Code and say "build a tool for X" or "create a LangChain tool"
2. The skill checks if `ClaudeStyleTool` base class is installed, and copies it if not
3. Collects tool name, description, schema fields, and security property answers
4. Generates a complete `.py` tool file in correct field order
5. Prints a one-line security posture summary for quick verification
6. For simple tools with no custom validation, uses the `build_tool()` factory instead

## Limitations

Security properties require developer judgment — the skill will ask the right questions, but whether a tool is truly concurrency-safe depends on your business logic. The `_call` body is scaffolded with a placeholder; you fill in the actual implementation.
