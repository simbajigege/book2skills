# 📚 book2skills

> 将经典书籍的智慧，转化为 AI Agent 可直接使用的 Skills。

**book2skills** 是一个开源项目，专注于将高质量的实用类书籍系统性地提炼为 [Agent Skills](https://agentskills.io) 格式，让 Claude、Claude Code 等 AI Agent 能够直接运用书中的方法论来解决实际问题。

---

## 🎯 理念

一本好书的价值，不应该只存在于人的脑海中。

通过将书籍的核心框架、决策流程、评估标准提炼为结构化的 Skill，任何人都可以让 AI Agent 直接运用这些经过时间检验的智慧。

**我们遵循的原则：**
- 📖 **忠实原著** — 每个 Skill 均基于完整阅读原书，而非二手摘要
- 🧩 **可操作** — 不只是知识搬运，而是转化为 Agent 可执行的判断框架
- 🔍 **可验证** — 每个标准和规则都标注来源章节，便于溯源
- 🌐 **开放标准** — 遵循 [agentskills.io](https://agentskills.io) 规范，兼容 Claude、Claude Code、Cursor、VS Code 等平台

---

## 📦 Skills 列表

| Skill | 原著 | 作者 | 分类 | 状态 |
|-------|------|------|------|------|
| [fisher-investing](./skills/fisher-investing/) | *Common Stocks and Uncommon Profits* | Philip Fisher | 投资 | ✅ 已发布 |
| *(更多即将推出)* | | | | 🔜 |

---

## 🚀 快速开始

### 在 Claude.ai 中使用

1. 进入任意 Skill 文件夹，下载对应的 `.skill` 文件（见 [Releases](../../releases)）
2. 打开 Claude.ai → Settings → Features → Custom Skills → Upload

### 在 Claude Code 中使用

```bash
# 克隆整个仓库
git clone https://github.com/simbajigege/book2skills.git

# 将需要的 skill 复制到你的项目
cp -r book2skills/skills/fisher-investing .claude/skills/
```

### 手动安装（任意支持 Agent Skills 的平台）

将 `skills/<skill-name>/` 文件夹复制到你的平台对应的 skills 目录即可。

---

## 🗺️ 路线图

我们计划陆续将以下书籍转化为 Skills：

**投资类**
- [ ] *The Intelligent Investor* — Benjamin Graham
- [ ] *One Up On Wall Street* — Peter Lynch
- [ ] *Poor Charlie's Almanack* — Charlie Munger

**商业思维类**
- [ ] *Good to Great* — Jim Collins
- [ ] *Zero to One* — Peter Thiel
- [ ] *The Innovator's Dilemma* — Clayton Christensen

**思维方法类**
- [ ] *Thinking, Fast and Slow* — Daniel Kahneman
- [ ] *The Art of Problem Solving* — Russell Ackoff

> 有你想要的书？欢迎[提交 Issue](../../issues/new?template=book-request.md) 投票！

---

## 🤝 如何贡献

欢迎任何人参与！贡献方式：

1. **提交书籍请求** — 告诉我们你最希望看到哪本书被转化
2. **贡献新 Skill** — 按照[贡献指南](./CONTRIBUTING.md)提交 PR
3. **改进现有 Skill** — 发现错误或不准确的地方，提 Issue 或直接 PR
4. **传播** — Star ⭐ 本项目，分享给可能感兴趣的朋友

---

## 📁 项目结构

```
book2skills/
├── README.md
├── CONTRIBUTING.md          # 贡献指南
├── skills/
│   ├── fisher-investing/    # 每个 skill 一个独立文件夹
│   │   ├── SKILL.md         # 核心文件：触发器 + 主框架
│   │   └── references/      # 详细参考文件（按需加载）
│   │       ├── fifteen-points.md
│   │       ├── scuttlebutt.md
│   │       ├── when-to-buy-sell.md
│   │       └── donts.md
│   └── (更多 skills...)
└── .github/
    └── ISSUE_TEMPLATE/      # Issue 模板
```

---

## 📄 许可证

本项目代码采用 [MIT License](./LICENSE)。

Skills 内容基于原著提炼，仅供个人学习和研究使用，版权归原作者所有。

---

<p align="center">
  Made with ❤️ | 用 AI 让好书触手可及
</p>
