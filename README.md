# 📚 book2skills

> Transform the wisdom of classic books into AI Agent Skills.

**book2skills** is an open-source project focused on systematically distilling high-quality practical books into Agent Skills format, enabling AI agents like Claude and Claude Code to directly apply the methodologies from these books to solve real-world problems.

---

## 🎯 Philosophy

The value of a great book shouldn't exist only in human memory.

By distilling a book's core frameworks, decision processes, and evaluation criteria into structured Skills, anyone can let AI agents directly apply time-tested wisdom.

**Our principles:**
- 📖 **Faithful to the source** — Every Skill is based on reading the complete original book, not secondhand summaries
- 🧩 **Actionable** — Not just knowledge transfer, but transformation into executable judgment frameworks for agents
- 🔍 **Verifiable** — Every criterion and rule is annotated with its source chapter for traceability
- 🌐 **Open standard** — Follows specifications, compatible with Claude, Claude Code, Cursor, VS Code, and more

---

## 📦 Skills List

| Skill | Book | Author | Category | Status |
|-------|------|--------|----------|--------|
| [common-stocks-uncommon-profits](./skills/common-stocks-uncommon-profits/) | *Common Stocks and Uncommon Profits* | Philip Fisher | Investing | ✅ Released |
| [html-line-svg](./skills/html-line-svg/) | Original Skill | simbajigege | Design & Visualization | ✅ Released |
| *(more coming soon)* | | | | 🔜 |

---

## 🚀 Quick Start

### Using with Claude.ai

1. Go to any Skill folder and download the corresponding `.skill` file (see [Releases](../../releases))
2. Open Claude.ai → Settings → Features → Custom Skills → Upload

### Using with Claude Code

```bash
# Clone the entire repository
git clone https://github.com/simbajigege/book2skills.git

# Copy the desired skill to your project
cp -r book2skills/skills/common-stocks-uncommon-profits .claude/skills/
```

### Manual Installation (any platform supporting Agent Skills)

Copy the `skills/<skill-name>/` folder to your platform's skills directory.

---

## 🗺️ Roadmap

We plan to progressively convert the following books into Skills:

**Investing**
- [ ] *The Intelligent Investor* — Benjamin Graham
- [ ] *One Up On Wall Street* — Peter Lynch
- [ ] *Poor Charlie's Almanack* — Charlie Munger

**Business Thinking**
- [ ] *Good to Great* — Jim Collins
- [ ] *Zero to One* — Peter Thiel
- [ ] *The Innovator's Dilemma* — Clayton Christensen

**Mental Models**
- [ ] *Thinking, Fast and Slow* — Daniel Kahneman
- [ ] *The Art of Problem Solving* — Russell Ackoff

> Have a book you'd like to see? [Submit an Issue](../../issues/new?template=book-request.md) and vote!

---

## 🤝 How to Contribute

Everyone is welcome! Ways to contribute:

1. **Submit a book request** — Tell us which book you'd most like to see converted
2. **Contribute a new Skill** — Follow the [Contributing Guide](./CONTRIBUTING.md) and submit a PR
3. **Improve existing Skills** — Found an error or inaccuracy? Open an Issue or submit a PR directly
4. **Spread the word** — Star ⭐ this project and share it with interested friends

---

## 📁 Project Structure

```
book2skills/
├── README.md
├── CONTRIBUTING.md          # Contributing guide
├── skills/
│   ├── common-stocks-uncommon-profits/    # Each skill in its own folder
│   │   ├── SKILL.md         # Core file: triggers + main framework
│   │   └── references/      # Detailed reference files (loaded on demand)
│   │       ├── fifteen-points.md
│   │       ├── scuttlebutt.md
│   │       ├── when-to-buy-sell.md
│   │       └── donts.md
│   └── (more skills...)
└── .github/
    └── ISSUE_TEMPLATE/      # Issue templates
```

---

## 📄 License

The code in this project is licensed under the [MIT License](./LICENSE).

Skill content is distilled from original works for personal learning and research purposes only. Copyright belongs to the original authors.

---

<p align="center">
  Made with ❤️ | Making great books accessible through AI
</p>
