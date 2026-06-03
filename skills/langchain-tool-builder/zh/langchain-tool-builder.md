---
title: "LangChain Tool Builder"
author: "simbajigege"
book_code: "langchain-tool-builder"
description: "用 Claude Code 的 fail-closed 设计模式定义 LangChain（Python）工具——name、schema、权限、执行逻辑统一写在一个类里，自动走 validate → permission → call 三层流程，新工具默认安全。"
tagline: "一个类搞定工具定义——安全属性 fail-closed，三层拦截自动运行"
tags: ["LangChain", "Python", "AI 工程", "工具定义", "Claude Code", "agent 工具"]
cover_url: "/assets/books/covers/book-indigo.svg"
github_url: "https://github.com/simbajigege/book2skills/skills/langchain-tool-builder"
download_url: "/skills/langchain-tool-builder.zip"
related_skills: []
examples:
  - human: |
      我在用 LangChain 做一个 AI 助手，需要查询 MySQL 里的员工信息。想定义一个工具让 agent 能搜索员工，传入姓名关键词，返回匹配的员工列表（姓名、部门、职级）。这个工具是只读的，多个工具可以并发跑。帮我生成。
    ai: |
      好的，先梳理安全属性：查询类工具 `is_read_only=True`、`is_concurrency_safe=True`，不会删除数据所以 `is_destructive=False`。

      先检查基类是否就位：

      ```bash
      ls /Users/jigege/ai-base/backend/base/utils/claude_style_tool.py
      ```

      文件存在，跳过安装。下面生成工具文件：

      **建议路径：** `/Users/jigege/ai-base/backend/base/tools/hr_search_employees.py`

      ```python
      """hr_search_employees.py — 按姓名关键词搜索员工信息"""

      from typing import Optional
      from pydantic import BaseModel, Field
      from base.utils.claude_style_tool import ClaudeStyleTool
      import mysql.connector
      import json


      class HrSearchEmployeesInput(BaseModel):
          keyword: str = Field(description="姓名搜索关键词，支持模糊匹配。e.g. '张伟'")
          limit: int = Field(default=20, description="最多返回条数，默认 20，最大 50")
          offset: int = Field(default=0, description="分页偏移量，默认 0")


      class HrSearchEmployeesTool(ClaudeStyleTool):
          # — identity —
          name: str = "hr_search_employees"
          description: str = "按姓名关键词搜索员工，返回姓名、部门、职级。只用于查询，不做任何写操作。"
          args_schema = HrSearchEmployeesInput

          # — security metadata —
          is_read_only: bool = True
          is_destructive: bool = False
          is_concurrency_safe: bool = True
          max_result_chars: int = 10_000

          def _validate_input_semantics(self, keyword: str, limit: int, offset: int) -> tuple[bool, Optional[str]]:
              if len(keyword.strip()) < 1:
                  return False, "keyword 不能为空。请提供至少 1 个字符的姓名关键词。"
              if limit > 50:
                  return False, f"limit 最大 50，当前 {limit}。请将 limit 调小后重试。"
              return True, None

          def _call(self, keyword: str, limit: int = 20, offset: int = 0, **kwargs) -> str:
              # ... 查询逻辑
              pass
      ```

      安全属性总结：

      ```
      HrSearchEmployeesTool: read_only=True  destructive=False  concurrency_safe=True  max_result=10K
      ```

  - human: |
      我还需要一个写工具：把 agent 生成的员工报告存成 CSV 文件。路径要限制在 /data/reports/ 目录下，不能让 agent 随便写文件。
    ai: |
      这个工具有写操作，安全属性应该是 `is_read_only=False`、`is_concurrency_safe=False`（避免并发写同一文件覆盖）。权限检查放在 `_check_permissions` 里，拦截越权路径。

      **建议路径：** `/Users/jigege/ai-base/backend/base/tools/hr_save_report.py`

      ```python
      """hr_save_report.py — 将员工报告保存为 CSV，限定写入 /data/reports/ 目录"""

      import os, csv, json
      from typing import Optional
      from pydantic import BaseModel, Field
      from base.utils.claude_style_tool import ClaudeStyleTool

      ALLOWED_DIR = "/data/reports"


      class HrSaveReportInput(BaseModel):
          filename: str = Field(description="文件名（不含路径）。e.g. 'q1_report.csv'")
          rows: str = Field(description="JSON 格式行数据。e.g. '[{\"name\":\"张伟\",\"dept\":\"研发\"}]'")


      class HrSaveReportTool(ClaudeStyleTool):
          name: str = "hr_save_report"
          description: str = "将员工报告数据保存为 CSV，写入路径限定在 /data/reports/ 目录。"
          args_schema = HrSaveReportInput

          is_read_only: bool = False
          is_destructive: bool = False
          is_concurrency_safe: bool = False
          max_result_chars: int = 500

          def _check_permissions(self, filename: str, rows: str) -> tuple[bool, Optional[str]]:
              if "/" in filename or "\\" in filename:
                  return False, f"filename 不能含路径分隔符，当前：'{filename}'。只传文件名，不含目录。"
              return True, None

          def _call(self, filename: str, rows: str, **kwargs) -> str:
              data = json.loads(rows)
              path = os.path.join(ALLOWED_DIR, filename)
              with open(path, "w", newline="", encoding="utf-8") as f:
                  writer = csv.DictWriter(f, fieldnames=data[0].keys())
                  writer.writeheader()
                  writer.writerows(data)
              return f"已写入 {len(data)} 行到 {path}"
      ```

      安全属性总结：

      ```
      HrSaveReportTool: read_only=False  destructive=False  concurrency_safe=False  max_result=500
      ```
---

# LangChain Tool Builder

在 LangChain 项目里手写工具有一个隐患：安全属性分散在多处——权限逻辑可能混在执行逻辑里，新工具忘记声明 `is_read_only` 就默认可写。这个 skill 用 Claude Code 的 `buildTool()` 模式解决这个问题：一个类统一管理工具的身份、参数 schema、安全属性和执行逻辑，新工具 fail-closed 默认安全。

## 核心框架

| 层级 | 方法 | 职责 |
|---|---|---|
| 安全元数据 | 类属性 | `is_read_only`、`is_destructive`、`is_concurrency_safe` 三个 bool，默认 False（fail-closed） |
| 语义校验 | `_validate_input_semantics` | 在执行前拦截"参数格式不对"的情况，错误消息必须可操作 |
| 权限检查 | `_check_permissions` | 在执行前拦截"不该用这个工具"的情况（路径越权、缺少 env var） |
| 核心逻辑 | `_call` | 真正的业务执行，只在前两层通过后才运行 |

## 支持的查询类型

- "帮我定义一个查询/搜索/创建/删除工具"
- "给这个工具加权限检查 / 参数校验"
- "在项目里安装 ClaudeStyleTool 基类"
- "工具定义" / "build_tool" / "Claude Code style tool"
- "定义一个工具" / "create a LangChain tool"

## 使用方式

1. 打开 Claude Code，说"帮我定义一个工具"或"create a tool for X"
2. Skill 检查基类是否就位，没有则自动安装
3. 收集工具名、描述、参数 schema、安全属性
4. 生成完整的 `.py` 工具文件，打印安全属性摘要供校验
5. 对于简单工具，使用 `build_tool()` 工厂函数，更简洁

## 局限说明

安全属性需要开发者明确声明——Skill 会引导你回答，但最终判断（这个工具是否并发安全？）需要你对业务逻辑有判断力。`_call` 内部的实际执行逻辑也需要你自己补全。
