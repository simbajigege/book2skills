# 贡献指南

感谢你有兴趣为 book2skills 做贡献！

---

## 贡献一个新 Skill 的流程

### 第一步：选书

好的 Skill 候选书籍应满足：
- **实用性强** — 书中有具体的框架、标准、决策流程，而非纯理论
- **经过时间检验** — 经典著作优先，出版至少 5 年以上
- **可操作化** — 书中的方法论可以被提炼为 Agent 可执行的步骤

在开始前，请先[提交 Issue](../../issues/new?template=book-request.md) 确认该书籍尚未有人认领。

### 第二步：阅读原书

**必须完整阅读原著**，不接受基于摘要或二手资料创建的 Skill。

阅读时重点提炼：
- 核心框架和评估标准
- 决策流程和判断规则
- 作者明确反对的做法（"不要做什么"往往和"要做什么"同等重要）
- 具体的可操作步骤

### 第三步：创建 Skill 文件夹

```
skills/your-skill-name/
├── SKILL.md              # 必须
└── references/           # 推荐，用于存放详细内容
    ├── framework.md
    └── ...
```

**SKILL.md 格式要求：**

```yaml
---
name: your-skill-name         # 小写字母、数字、连字符，最长 64 字符
description: >                # 使用折叠块语法避免引号问题
  描述这个 Skill 做什么，以及何时触发它。
  包含触发短语示例。要稍微"积极"一些，
  让 Agent 知道遇到相关问题时主动调用。
---

# Skill 标题

（正文内容）
```

**YAML 注意事项：**
- description 中不要直接使用双引号 `"` 或单引号 `'`
- 推荐使用 `>` 折叠块语法写多行 description
- name 不能包含 "anthropic" 或 "claude"

### 第四步：测试

在提交 PR 前，请在 Claude.ai 或 Claude Code 中实际测试你的 Skill：
- 安装后，提问触发语是否能正确调用 Skill
- 对 2-3 个真实问题测试输出质量
- 在 PR 中附上至少一个测试案例截图

### 第五步：提交 PR

PR 标题格式：`Add skill: [书名] — [作者名]`

PR 描述请包含：
- 书籍基本信息（书名、作者、出版年份）
- Skill 能回答哪类问题（3 个示例问题）
- 你是否完整阅读了原著（是/否）

---

## Skill 质量标准

| 标准 | 说明 |
|------|------|
| 忠实原著 | 内容可以追溯到书中具体章节，不添加未在书中出现的观点 |
| 可操作 | 用户提问后能得到具体的判断或建议，而非模糊的泛泛而谈 |
| 结构清晰 | 使用标题、表格、列表组织内容，便于 Agent 定位信息 |
| YAML 合法 | `name` 和 `description` 字段格式正确，可以被正确解析 |
| 体积合理 | SKILL.md 控制在 500 行以内；详细内容放入 references/ |

---

## 文件命名规范

- Skill 文件夹名：`kebab-case`，建议格式为 `{主题}-{书名关键词}`，例如 `fisher-investing`、`collins-good-to-great`
- references/ 中的文件：描述性命名，例如 `framework.md`、`evaluation-criteria.md`、`common-mistakes.md`

---

## 有问题？

欢迎在 [Discussions](../../discussions) 中提问，或直接在相关 Issue 下留言。
