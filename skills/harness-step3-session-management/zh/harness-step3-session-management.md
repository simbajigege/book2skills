---
title: "Harness Step 3 — 建立跨 Session 状态管理"
author: "simbajigege"
book_code: "harness-step3-session-management"
description: "创建 init.sh（环境健康检查）、tasks.json（结构化任务队列）和 progress.md（会话日志），解决 Claude Code 每次新对话失忆的问题，让任意 session 在 30 秒内完全恢复工作状态。"
tagline: "状态靠文件传递，不靠 agent 记忆——彻底解决失忆问题"
tags: ["AI 工程", "Claude Code", "任务管理", "Harness Engineering", "状态管理"]
cover_url: "/assets/books/covers/harness-step3-session-management.png"
github_url: "https://github.com/simbajigege/book2skills/skills/harness-step3-session-management"
download_url: "/skills/harness-step3-session-management.zip"
related_skills:
  - title: "Harness Step 1 — 创建 AGENTS.md 与知识库"
    url: "/zh/book/harness-step1-create-agent-md"
  - title: "Harness Step 2 — 填充 docs/ 知识库内容"
    url: "/zh/book/harness-step2-fill-docs"
  - title: "SEO Metadata Audit"
    url: "/zh/book/seo-metadata-audit"
examples:
  - human: "AGENTS.md 和 docs/ 都已经建好了。现在我想解决 agent 失忆的问题——每次开新会话都要重新告诉它上次做到哪里了。帮我建立状态管理。"
    ai: |
      好，我来创建三个文件，之后每次新会话你只需要让 agent 读这三个文件，
      30 秒内就能恢复工作状态。

      ---

      ## 创建 `init.sh`

      ```bash
      #!/bin/bash
      # 每次 session 开始时运行，验证环境正常

      echo "=== 环境检查 ==="

      # 检查依赖
      [ -d "backend/.venv" ] || { echo "⚠ 后端虚拟环境不存在，运行 poetry install"; }
      [ -d "frontend/node_modules" ] || { echo "⚠ 前端依赖未安装，运行 npm install"; }

      # 冒烟测试
      cd backend && poetry run python -c "from base.config import get_config; print('✓ 后端模块正常')"

      echo "=== 完成，读 tasks.json 查看待处理任务 ==="
      ```

      ---

      ## 创建 `tasks.json`

      根据当前项目状态，初始任务如下：

      ```json
      {
        "project": "my-project",
        "last_updated": "2026-04-13",
        "current_focus": "完成用户认证模块",
        "tasks": [
          {
            "id": "auth-01",
            "title": "实现 JWT 刷新 token 逻辑",
            "description": "当 access token 过期时自动使用 refresh token 续期，前端单例防竞态。",
            "status": "pending",
            "priority": "high",
            "verify": "运行 shop/test/auth_test.py，所有测试通过；手动测试 token 过期后自动续期",
            "requires_eval": false
          }
        ]
      }
      ```

      ---

      ## 创建 `progress.md`

      ```markdown
      # 项目进度记录

      ## 2026-04-13 初始化 Harness
      - 完成 step1：建立 docs/ 骨架
      - 完成 step2：填充知识库
      - 完成 step3：建立状态管理
      - 下次从这里开始：读 tasks.json，做 auth-01
      ```

      ---

      同时在 `AGENTS.md` 里新增了"Session 启动流程"一节：

      ```markdown
      ## Session 启动流程
      1. bash init.sh — 验证环境
      2. git log --oneline -10 — 了解最近历史
      3. head -20 progress.md — 看上次做到哪里
      4. 读 tasks.json — 选 priority=high 且 status=pending 的任务开始
      ```

      **下次开新会话时**，让 agent 执行这 4 步，它会自动知道从哪里继续。
      你不需要再解释"上次我们做了什么"。

  - human: "tasks.json 里的 verify 字段怎么写才有用？我现在写的是'确认功能正常'，这太模糊了。"
    ai: |
      "确认功能正常"对 agent 没有意义——它不知道用什么标准判断"正常"。
      verify 必须是**可执行的步骤**，最好是一条命令或一个具体操作。

      ---

      ## 好的 verify 写法

      **纯后端任务：**
      ```json
      "verify": "cd backend && python -m pytest shop/test/test_payment.py -v — 全部通过"
      ```

      **前端 UI 任务：**
      ```json
      "verify": "npm run build 无报错；在浏览器打开 /pricing，点击'订阅'按钮，弹出支付弹窗"
      ```

      **配置变更任务：**
      ```json
      "verify": "python -c \"from base.config import get_config; c = get_config(); assert c.db_host != ''\" 无报错"
      ```

      **删除废弃代码：**
      ```json
      "verify": "git diff --name-only — 只出现被删除的文件路径；npm run build 无报错"
      ```

      ---

      ## 判断 verify 够不够具体的标准

      问自己：**另一个不了解这个任务背景的人，能不能按 verify 里的步骤独立判断任务是否完成？**

      如果答案是"不能"，verify 就不够具体。继续拆分，直到答案变成"能"。

      ---

      ## requires_eval 的判断

      verify 通过了，但任务还需要人工判断整体质量时，把 `requires_eval` 设为 `true`。
      典型场景：新功能（不是 bug fix）、涉及权限逻辑、改动超过 3 个文件。
      纯删除、文档更新、配置调整可以直接设 `false`。
---

# Harness Step 3 — 建立跨 Session 状态管理

Claude Code 的会话是无状态的——每次对话结束，agent 对"上次做了什么"一无所知。传统解决方案是每次新对话手动解释背景，这既费时又不可靠。这个 skill 从根本上解决这个问题：状态写进文件，不放在 agent 的记忆里。

## 创建的三个文件

**`init.sh` — 环境健康检查**
每次 session 开始时运行。验证依赖已安装、配置文件存在、核心模块可导入。30 秒内发现环境问题，不让坏环境浪费整个 session。

**`tasks.json` — 结构化任务队列**
每个任务包含：`id`、`title`、`description`、`status`、`priority`、`verify`（可执行的完成验证步骤）、`requires_eval`（是否需要独立评审）。Agent 不猜下一步做什么，直接读任务队列。

**`progress.md` — 追加式会话日志**
每次 session 完成任务后在顶部追加一条记录。下次 session 读前 20 行，立即知道上次停在哪里。不删除历史，形成可追溯的工作流水账。

## Session 启动流程（写入 AGENTS.md）

```
1. bash init.sh          → 验证环境
2. git log --oneline -10 → 了解最近历史
3. head -20 progress.md  → 看上次做到哪里
4. 读 tasks.json         → 选 priority=high 且 status=pending 的任务
```

## verify 字段的设计原则

verify 必须是可执行的步骤，不能是模糊描述。检验标准：**另一个完全不了解背景的人，能否按 verify 独立判断任务是否完成？** 如果不能，继续拆分。

## 适用场景

- Harness Step 1 + 2 完成后，建立完整的 agent 工作体系
- 长期项目，多人/多 session 协作
- 任何"agent 老是忘记上次做了什么"的场景

## 局限说明

tasks.json 不会自动执行任务，需要人工或 agent 手动触发。被搁置的任务应在 `blocked_by` 字段说明原因，让下一个 session 能直接跳到可执行的任务。
