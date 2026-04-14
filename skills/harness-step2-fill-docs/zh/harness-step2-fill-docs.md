---
title: "Harness Step 2 — 填充 docs/ 知识库内容"
author: "simbajigege"
book_code: "harness-step2-fill-docs"
description: "深度阅读项目代码，将隐藏在代码里的架构知识、命名约定、技术决策显式写入 docs/ 各文件，让 agent 在任何 session 都能快速理解项目全貌，而不是靠猜测。"
tagline: "把代码里的隐性知识变成 agent 可读的显式文档"
tags: ["AI 工程", "Claude Code", "文档工程", "Harness Engineering", "架构文档"]
cover_url: "/assets/books/covers/harness-step2-fill-docs.png"
github_url: "https://github.com/simbajigege/book2skills/skills/harness-step2-fill-docs"
download_url: "/skills/harness-step2-fill-docs.zip"
related_skills:
  - title: "Harness Step 1 — 创建 AGENTS.md 与知识库"
    url: "/zh/harness-step1-create-agent-md"
  - title: "Harness Step 3 — 建立跨 Session 状态管理"
    url: "/zh/harness-step3-session-management"
  - title: "SEO Metadata Audit"
    url: "/zh/seo-metadata-audit"
examples:
  - human: "AGENTS.md 和 docs/ 骨架已经建好了，但里面大部分是占位符。帮我把 docs/ARCHITECTURE.md 和 docs/CONVENTIONS.md 填充成有实质内容的文档。"
    ai: |
      好，我先深度扫描代码，再写文档。**结论先行，不写任何我无法从代码推断的内容**。

      ---

      ## 扫描过程

      读取了：`backend/main.py`、`backend/bookskill/service/`、`backend/base/database_operations/`、
      `frontend/src/app/[locale]/`、`frontend/src/services/`、`pyproject.toml`、`package.json`

      ---

      ## 写入 `docs/ARCHITECTURE.md`

      ```markdown
      # 架构说明

      ## 分层规则（后端）

      HTTP 请求 → Routes（仅校验 + 序列化）→ Services（全部业务逻辑）→
      DatabaseOperations（SQL 封装）→ PostgreSQL / Redis

      严禁跨层跳级：Routes 不得直接调 DatabaseOperations。

      ## 模块划分

      - `base/`：框架基础层，无业务逻辑
      - `user/`：认证域（JWT + Google OAuth2）
      - `shop/`：支付域（Stripe/PayPal 适配器模式）
      - `bookskill/`：核心业务域（书籍解析 + Skill 生成 + 对话）

      依赖方向：bookskill / shop → user → base，不可反向。
      ```

      写入 `docs/CONVENTIONS.md`：

      ```markdown
      # 代码约定

      ## 文件命名（后端）
      - 路由文件：`{domain}_routes.py`（示例：`book_routes.py`）
      - 服务文件：`{domain}_service.py`（示例：`book_parse_service.py`）
      - DB 操作：`{table}_operation.py`（示例：`book_operation.py`）

      ## 变量命名
      - Python：全部 snake_case，类名 PascalCase
      - TypeScript：变量 camelCase，组件 PascalCase，常量 UPPER_SNAKE_CASE
      ```

      ---

      **标注了「待补充」的地方（需要你来填）：**
      - `TECH_DECISIONS.md`：Redis 队列的选型原因 — 从代码中只能看到用法，看不到为什么不用 Celery
      - `QUALITY.md`：书籍处理流水线的预期完成时间 — 需要实测数据

      其余内容全部从代码推断，可以直接使用。

  - human: "TECH_DECISIONS.md 里有好几个「待补充」，这些内容我说不清楚当时为什么这样选，怎么办？"
    ai: |
      不知道原因是正常的——选型决策往往在代码里看不到。以下两种处理方式，按情况选：

      ---

      ## 方式 1：写「推断原因」并标注

      从代码的用法里，可以反推出一些合理理由。我来写，你来确认或纠正：

      ```markdown
      ### Redis 任务队列（而非 Celery）
      **推断原因**：书籍处理是单次异步任务，不需要 Celery 的定时调度、任务链、
      优先级队列等复杂能力；Redis list 的 blpop/rpush 够用，运维更简单。
      **⚠ 待确认**：如果当时有其他考虑，请补充在此。
      ```

      这比空着强——agent 有参考依据，你也不需要从零重建记忆。

      ---

      ## 方式 2：接受不确定性，直接标注

      ```markdown
      ### Redis 任务队列
      **选择原因**：原始决策原因不明，请补充。
      **当前观察**：用于书籍处理异步任务（worker 进程 blpop 消费）。
      **替代方案**：Celery（更重，有自动重试、定时任务能力）。
      ```

      这种写法诚实，也比完全空白有用——至少告诉 agent"这里有个未记录的决策"，
      不会让 agent 凭空猜测或改掉它。

      ---

      ## 建议

      优先用方式 1，让我来写推断版本，你花 2 分钟确认一遍比从零回忆快得多。
      遇到完全想不起来的，用方式 2，不要为了填满而捏造原因。
---

# Harness Step 2 — 填充 docs/ 知识库内容

docs/ 骨架创建后，最常见的问题是：文件存在，但内容是占位符。agent 读到"命名规则：见代码"这种文字，等于什么都没读。这个 skill 解决这一问题——深度读懂代码，把隐性知识变成显式文档，每条规则都有代码实例支撑。

## 会填充哪些文件

| 文件 | 填充内容 |
|------|---------|
| `docs/ARCHITECTURE.md` | 模块职责、依赖方向规则（带原因）、主要数据流 |
| `docs/CONVENTIONS.md` | 文件命名规律（含实际示例）、变量/函数命名规律 |
| `docs/TECH_DECISIONS.md` | 每个主要库/框架的选型原因（能推断则推断，不能则标注「待补充」） |
| `docs/QUALITY.md` | 项目特有的完成定义、代码审查检查清单 |
| `docs/exec-plans/tech-debt-tracker.md` | 扫描中发现的重复代码、命名不一致、TODO 注释等 |

## 核心原则

**推断出来的内容标注来源，无法确定的内容标注「待补充」**——不用模糊占位符糊弄过去。

扫描结束后，skill 会给出一份「待补充」清单，这是需要你人工确认的部分。大多数项目通常有 3-5 个这样的条目，主要集中在：
- 技术选型的历史原因（代码里只有结论）
- 性能基准和 SLA（需要实测数据）
- 团队约定俗成的习惯（没有写在代码里的规范）

## 支持的使用场景

- Step 1 建好骨架后，立即填充实质内容
- 项目经历重大重构后，更新文档与代码的一致性
- 接手他人项目，快速生成自己能看懂的架构说明

## 使用方式

1. 确认项目中已有 `AGENTS.md` 和 `docs/` 目录（运行 Step 1 生成）
2. 说"填充文档内容"或"写 ARCHITECTURE.md"
3. Skill 扫描入口文件、模块边界、依赖声明、命名模式
4. 写入所有 docs/ 文件，列出「待补充」清单
5. 你只需要确认或补充那些 skill 无法推断的内容

## 局限说明

Skill 从代码推断，不访问 git history 或团队沟通记录。历史决策原因（"为什么当时选了 X"）通常需要人工补充；运行时行为（API 响应格式、实际查询性能）无法从文件中读取。
