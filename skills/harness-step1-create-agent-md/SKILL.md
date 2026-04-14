---
name: harness-step1-create-agents-md
description: |
  Harness Engineering 第一阶段：扫描现有项目，生成 AGENTS.md（目录文件）和完整的 docs/ 知识库结构。
  
  当用户想要"为项目添加 agent 支持"、"让 AI 更好地理解我的项目"、"开始 harness engineering"、
  "创建 AGENTS.md"、"搭建 agent 文档结构"、"让 Claude Code 更好地工作"时，立即使用此 skill。
  
  也适用于用户说"帮我把项目文档整理好给 agent 用"、"我想开始用 AI agent 开发"等场景。
---

# Harness Step 1: 创建 AGENTS.md 与 docs/ 知识库

## 目标

为项目建立 agent 可读的知识库地基：
- 一份简短的 `AGENTS.md`（~100 行，作为"目录"而非百科全书）
- 一套 `docs/` 目录结构，存放真正的知识

**核心原则**：agent 看不到的东西就不存在。所有架构决策、命名约定、技术选型，必须以文件形式存在于仓库中。

---

## 执行步骤

### Step 1：扫描项目

按顺序收集项目信息，**已知信息跳过，不要重复提问**：

```bash
# 1. 项目根目录结构（2层）
find . -maxdepth 2 -not -path '*/node_modules/*' -not -path '*/.git/*' \
  -not -path '*/__pycache__/*' -not -path '*/dist/*' -not -path '*/.next/*' | sort

# 2. 识别技术栈
cat package.json 2>/dev/null || cat pyproject.toml 2>/dev/null || \
  cat go.mod 2>/dev/null || cat Cargo.toml 2>/dev/null || echo "未找到包管理文件"

# 3. 查看是否已有文档
ls -la *.md 2>/dev/null; ls -la docs/ 2>/dev/null

# 4. 查看 README（如有）
head -80 README.md 2>/dev/null || head -80 readme.md 2>/dev/null
```

从扫描结果中提取：
- **项目名称和用途**（从 README 或 package.json）
- **技术栈**（语言、框架、主要依赖）
- **目录结构**（主要模块划分）
- **已有文档**（避免重复，复用现有内容）

### Step 2：生成 docs/ 目录结构

创建以下文件（内容根据扫描结果填写，不要留空占位符）：

**必须创建的文件：**

```
AGENTS.md                    ← 目录文件，~100行
docs/
├── ARCHITECTURE.md          ← 模块划分、依赖关系
├── CONVENTIONS.md           ← 命名规则、代码风格
├── TECH_DECISIONS.md        ← 技术选型理由
├── QUALITY.md               ← 验收标准、完成定义
└── exec-plans/
    ├── active/              ← 当前进行中的计划（空目录，放 .gitkeep）
    ├── completed/           ← 已完成的计划（空目录，放 .gitkeep）
    ├── backlog.md           ← 待开发功能列表（已知需求，尚未排期）
    └── tech-debt-tracker.md ← 已知技术债务
```

**可选创建（根据项目实际情况判断）：**

```
docs/
├── design-docs/             ← 有复杂设计决策时创建
├── product-specs/           ← 有产品规格时创建
└── references/              ← 有外部文档需要本地化时创建
```

### Step 3：写 AGENTS.md

严格遵守以下格式，控制在 100 行以内：

```markdown
# [项目名称] — Agent 工作指南

## 这是什么项目
[1-3句话：项目用途、核心功能、服务对象]

## 快速定向
- **我在哪个目录？** 运行 `pwd` 确认工作目录
- **技术栈**：[语言] + [框架] + [主要工具]
- **入口文件**：[主要入口，如 src/main.ts、app/main.py]
- **启动命令**：[如何启动开发服务器]
- **测试命令**：[如何跑测试]

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

## 工作规范
1. **改之前先读**：修改任何模块前，先读对应的架构文档
2. **完成即提交**：每个功能完成后立即 git commit，写清楚做了什么
3. **更新文档**：如果你的修改影响了架构或约定，同步更新 docs/
4. **不要猜**：看不懂的地方先读文档，文档没有再问

## 禁止事项
[根据项目实际情况填写，例如：]
- 不要直接修改 `generated/` 目录下的文件（自动生成）
- 不要跳过测试直接合并
- 不要在 service 层引用 UI 组件（见 docs/ARCHITECTURE.md）
```

### Step 4：写各个 docs/ 文件

每个文件的内容要求：

**`docs/ARCHITECTURE.md`**
- 模块/包的划分和职责
- 依赖方向规则（哪层能引用哪层）
- 主要数据流
- 不要写实现细节，写"是什么"和"为什么这样分"

**`docs/CONVENTIONS.md`**
- 文件命名规则
- 变量/函数/类命名规则
- 目录组织规则
- 注释风格
- 任何团队约定俗成的习惯

**`docs/TECH_DECISIONS.md`**
- 为什么选这个框架而不是其他
- 为什么用这个库
- 历史上做过的重要架构决定和原因
- 如果扫描时无法判断原因，写"待补充"并注明这是需要人工填写的

**`docs/QUALITY.md`**
- 一个功能算"完成"的标准（Definition of Done）
- 代码审查检查清单
- 测试覆盖要求
- 性能基准（如果有）

**`docs/exec-plans/backlog.md`**
- 已知但尚未排期的待开发功能列表，这一点可以向用户询问
- 每条格式：`[优先级: P1/P2/P3] 功能描述 — 背景说明`
- 注意：backlog 是"想做但还没做"，不是技术债务（技术债务是"已有但做得不好"）
- 如果扫描时发现后端已实现但前端未上线的功能、或文档中提到的计划中功能，写入此处
- 如果扫描时没有发现明显的 backlog，写空列表并注明"待发现时补充"

**`docs/exec-plans/tech-debt-tracker.md`**
- 已知的技术债务列表（现有代码中质量不佳、需要改进的部分）
- 每条格式：`[优先级] 问题描述 — 影响范围`
- 注意：不要把 backlog（待开发功能）混入此文件
- 如果扫描时没有发现明显债务，写空列表并注明"待发现时补充"

---

## 质量检验

生成完成后，自检以下问题：

- [ ] AGENTS.md 是否控制在 150 行以内？
- [ ] AGENTS.md 里是否有具体的启动/测试命令（而非"见文档"）？
- [ ] docs/ 里的文件是否有实际内容，而非空占位符？
- [ ] TECH_DECISIONS.md 里无法判断的决策是否标注了"待补充"？
- [ ] 目录表里的每个链接是否对应实际存在的文件？

---

## 完成后告知用户

输出一个简短摘要：
1. 创建了哪些文件
2. 哪些内容是从项目扫描中推断的（可能需要人工核实）
3. 哪些字段需要用户手动补充（标注了"待补充"的地方）
4. 下一步：可以运行 `harness-step2` skill 来建立状态管理（progress 文件 + tasks.json）
