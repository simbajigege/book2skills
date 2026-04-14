---
title: "Harness Step 1 — 创建 AGENTS.md 与知识库"
author: "simbajigege"
book_code: "harness-step1-create-agent-md"
description: "扫描项目代码库，自动生成 AGENTS.md（agent 工作指南）和完整的 docs/ 知识库骨架，让 Claude Code 在任意新会话中 30 秒内定向，无需重复解释项目结构。"
tagline: "一次扫描，永久定向——让 agent 第一次就读懂你的项目"
tags: ["AI 工程", "Claude Code", "开发工具", "Harness Engineering", "agent 支持"]
cover_url: "/assets/books/covers/harness-step1-create-agent-md.png"
github_url: "https://github.com/simbajigege/book2skills/skills/harness-step1-create-agent-md"
download_url: "/skills/harness-step1-create-agent-md.zip"
related_skills:
  - title: "Harness Step 2 — 填充 docs/ 知识库内容"
    url: "/zh/harness-step2-fill-docs"
  - title: "Harness Step 3 — 建立跨 Session 状态管理"
    url: "/zh/harness-step3-session-management"
  - title: "SEO Metadata Audit"
    url: "/zh/seo-metadata-audit"
examples:
  - human: "我有一个 FastAPI 后端 + Next.js 前端的项目，最近开始用 Claude Code 开发，但每次开新会话都要重新解释项目结构。帮我创建 AGENTS.md，让 agent 能快速定向。"
    ai: |
      好的，我先扫描项目再生成。

      **扫描结果（推断）：**
      - 技术栈：Python 3.11 + FastAPI / Next.js 14 + TypeScript
      - 后端入口：`backend/main.py`（或 `start_web.py`）
      - 前端入口：`frontend/src/app/layout.tsx`
      - 依赖文件：`backend/pyproject.toml`，`frontend/package.json`

      ---

      生成的 `AGENTS.md`（写入项目根目录）：

      ```markdown
      # MyProject — Agent 工作指南

      ## 这是什么项目
      [根据扫描结果填写，如：一个内容管理平台，FastAPI 提供 REST API，Next.js 静态导出前端]

      ## 快速定向
      - **技术栈**：Python 3.11 + FastAPI / Next.js 14 + TypeScript
      - **后端入口**：`backend/start_web.py`
      - **前端入口**：`frontend/src/app/layout.tsx`
      - **后端启动**：`cd backend && python start_web.py`
      - **前端启动**：`cd frontend && npm run dev`
      - **后端测试**：`cd backend && python -m pytest`
      - **前端构建**：`cd frontend && npm run build`

      ## 知识库地图
      在做任何修改前，先阅读相关文档：

      | 我想了解... | 去读这个文件 |
      |------------|-------------|
      | 整体架构、模块划分 | `docs/ARCHITECTURE.md` |
      | 命名规则、代码风格 | `docs/CONVENTIONS.md` |
      | 技术选型原因 | `docs/TECH_DECISIONS.md` |
      | 什么叫"完成" | `docs/QUALITY.md` |
      | 当前进行中的计划 | `docs/exec-plans/active/` |
      | 待开发功能列表 | `docs/exec-plans/backlog.md` |
      | 已知技术债务 | `docs/exec-plans/tech-debt-tracker.md` |

      ## 禁止事项
      - 不要直接修改 `frontend/out/`（静态构建输出）
      - 不要在 service 层之外直接操作数据库
      ```

      同时创建了以下 `docs/` 文件骨架：
      - `docs/ARCHITECTURE.md` — 模块划分、分层规则
      - `docs/CONVENTIONS.md` — 命名约定
      - `docs/TECH_DECISIONS.md` — 技术选型记录
      - `docs/QUALITY.md` — 完成标准
      - `docs/exec-plans/backlog.md` — 待开发功能
      - `docs/exec-plans/tech-debt-tracker.md` — 技术债务

      **需要你手动确认的内容：**
      - `docs/TECH_DECISIONS.md` 中的"选型原因"部分标注了「待补充」，因为代码中无法推断
      - `docs/exec-plans/backlog.md` 目前为空，建议告诉我 3-5 个计划中的功能

      下一步运行 `/harness-step2-fill-docs`，我来深度读代码、填充文档实质内容。

  - human: "生成的 AGENTS.md 有点长，agent 每次都要读很多内容。有没有办法控制长度？"
    ai: |
      有，核心原则是：**AGENTS.md 是目录，不是百科全书**。

      ## 控制长度的三条规则

      **规则 1：启动命令只列命令，不解释原理**

      ❌ 冗长写法：
      ```
      后端启动：先确保 Poetry 虚拟环境已激活，然后 cd 到 backend 目录，
      接着运行 python start_web.py，该脚本会自动加载 .env.dev 并启动 uvicorn...
      ```

      ✅ 简洁写法：
      ```
      后端启动：cd backend && python start_web.py
      ```

      **规则 2：架构细节放 docs/，AGENTS.md 只给指针**

      AGENTS.md 写：`整体架构见 docs/ARCHITECTURE.md`
      不要在 AGENTS.md 里描述每个模块的职责。

      **规则 3：禁止事项只列"反直觉"的**

      如果 agent 不可能自己想到做某件事，不需要禁止。
      只列那些"看起来合理但会出问题"的操作。

      ---

      ## 理想长度目标

      - `AGENTS.md`：80–120 行
      - 每个 `docs/` 文件：200–400 行（内容丰富但聚焦）

      如果你的 AGENTS.md 超过 150 行，大概率是把 docs/ 里的内容搬过来了。把它挪回 docs/ 对应文件，AGENTS.md 只留指针就行。
---

# Harness Step 1 — 创建 AGENTS.md 与知识库

使用 Claude Code 的最大挑战之一是「失忆」——每次开新会话，agent 对项目一无所知，你必须重新解释架构、命名规范、启动命令。这个 skill 从根源解决这个问题：扫描代码库，一次性生成结构化的知识文件，让未来任何 agent session 都能在 30 秒内完成定向。

## 核心产出

```
project-root/
├── AGENTS.md                    ← agent 的「目录文件」，80-120 行
└── docs/
    ├── ARCHITECTURE.md          ← 模块划分、依赖规则、主要数据流
    ├── CONVENTIONS.md           ← 命名规范、文件组织约定
    ├── TECH_DECISIONS.md        ← 技术选型理由
    ├── QUALITY.md               ← 完成定义（Definition of Done）
    └── exec-plans/
        ├── active/              ← 当前进行中的计划
        ├── backlog.md           ← 待开发功能列表
        └── tech-debt-tracker.md ← 已知技术债务
```

## 设计原则

- **AGENTS.md 是目录，docs/ 是书**：agent 用 AGENTS.md 定向，用 docs/ 理解细节
- **推断 ≠ 捏造**：无法从代码推断的内容一律标注「待补充」，不伪造
- **适配任何技术栈**：Python/Node.js/Go/Rust，单体/微服务/monorepo 均可扫描

## 支持的使用场景

- 现有项目首次引入 agent 支持
- 团队新成员接手项目（让 agent 帮你快速读懂代码库）
- 重构后更新 agent 的项目认知
- 任何想让 Claude Code 少问你"这是什么项目"的场景

## 使用方式

1. 在项目根目录打开 Claude Code 会话
2. 说"为项目添加 agent 支持"或"创建 AGENTS.md"
3. Skill 自动扫描代码库（2-3 层目录、依赖文件、已有文档）
4. 生成所有文件，列出哪些内容需要你手动确认
5. 运行 `harness-step2-fill-docs` 深度填充文档内容

## 局限说明

Skill 只读取文件系统，无法获取运行时行为（如 API 响应格式、数据库实际内容）。`TECH_DECISIONS.md` 中的历史选型原因通常需要人工补充——代码里只有结论，没有当时的讨论过程。
