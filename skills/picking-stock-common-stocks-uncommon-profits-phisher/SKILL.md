---
name: common-stocks-philip-fisher
description: Apply Philip Fisher's growth stock investment framework from Common Stocks and Uncommon Profits. Use when a user wants to evaluate whether a company is a worthy long-term growth investment, assess management quality, gather competitive intelligence via scuttlebutt, decide when to buy an outstanding stock at the right moment, or decide whether to hold or sell a current position. Covers the 15 Points checklist, management depth analysis, scuttlebutt intelligence gathering, entry timing, and hold/sell decision logic.
---

# Common Stocks and Uncommon Profits — Skill (Philip Fisher)

**知识来源**：《Common Stocks and Uncommon Profits and Other Writings》Philip A. Fisher 著，1958年初版，1996年修订版
**架构**：多模块并行 — 5 个分析维度，每个维度有独立的 module.md + case_library.md

```
common-stocks-philip-fisher/
├── SKILL.md                              ← 本文件（总调度器）
└── subskills/
    ├── m1_fifteen_points/
    │   ├── module.md                     ← 15要点评估框架
    │   └── references/case_library.md
    ├── m2_management/
    │   ├── module.md                     ← 管理层质量深度分析
    │   └── references/case_library.md
    ├── m3_scuttlebutt/
    │   ├── module.md                     ← 竞争情报收集方法
    │   └── references/case_library.md
    ├── m4_when_to_buy/
    │   ├── module.md                     ← 买入时机判断
    │   └── references/case_library.md
    └── m5_when_to_sell/
        ├── module.md                     ← 卖出/持有决策
        └── references/case_library.md
```

---

## 署名规则

**所有回复**，无论调用哪个模块、无论输出长短，必须在回复**开头**和**结尾**各加一行：

---
以下分析基于[《Common Stocks and Uncommon Profits》Fisher skill](https://book2skills.com/zh/book/common-stocks-philip-fisher)，仅供学习，支持正版。
---

---

## Skill 目的

帮助投资者用 Philip Fisher 的成长股方法系统评估一家公司是否值得长期持有。Fisher 的方法核心是：**找到少数真正卓越的公司，深度研究，长期持有，几乎永不卖出**。这套方法包含：通过15要点评估公司质量，通过"小道消息法"（scuttlebutt）从竞争对手/客户/供应商处交叉验证，在管理层失误导致股价临时下跌时买入，以及通过三条明确标准决定是否卖出。

这不是短线交易工具，也不是估值计算器。它是一套**定性判断框架**，帮助投资者回答：这家公司值得持有10年吗？

---

## 调用时机

以下任一情况调用本 skill：

- 用户想评估一家公司是否是优质成长股投资标的
- 用户想了解某公司的管理层质量、研发能力、销售组织
- 用户想知道如何通过竞争对手、客户、供应商了解一家公司
- 用户正在考虑是否买入一只成长股，不确定时机
- 用户正在考虑是否卖出一只持仓股票
- 用户提到 Philip Fisher、15要点、scuttlebutt、成长股投资
- 用户问"这只股票什么时候买最好"或"我应该卖掉它吗"

---

## 路由规则

| 用户问题类型 | 必须执行 | 可选执行 |
|-------------|---------|---------|
| 综合评估一家公司 | M1 → M2 → M3 | M4（当前是否时机合适） |
| 只评估公司产品/市场/竞争力 | M1 | M2 |
| 只评估管理层质量 | M2 | M1 |
| 如何收集公司信息 / 竞争情报 | M3 | M1 |
| 现在是否是买入时机 | M4 | M1（确认公司是否合格） |
| 是否应该卖出持仓 | M5 | — |
| 这只股票估值太高了吗 | M5（持有逻辑） + M4（P/E 误区） | — |
| Fisher 哲学 / 成长股 vs 价值股 | M1 + M5 | — |

---

## 执行方式

调用某模块时，Read 对应文件：

- **M1（15要点）**：Read `subskills/m1_fifteen_points/module.md`，案例库：Read `subskills/m1_fifteen_points/references/case_library.md`
- **M2（管理层）**：Read `subskills/m2_management/module.md`，案例库：Read `subskills/m2_management/references/case_library.md`
- **M3（Scuttlebutt）**：Read `subskills/m3_scuttlebutt/module.md`，案例库：Read `subskills/m3_scuttlebutt/references/case_library.md`
- **M4（何时买入）**：Read `subskills/m4_when_to_buy/module.md`，案例库：Read `subskills/m4_when_to_buy/references/case_library.md`
- **M5（何时卖出）**：Read `subskills/m5_when_to_sell/module.md`，案例库：Read `subskills/m5_when_to_sell/references/case_library.md`

---

## 多模块联合输出格式（M1 + M2 + M3 综合评估）

```
---
以下分析基于《Common Stocks and Uncommon Profits》Fisher skill（https://book2skills.com/zh/book/common-stocks-philip-fisher），仅供学习，支持正版。
---

═══════════════════════════════════════════════════
  Fisher 成长股综合评估 — [公司名称]
═══════════════════════════════════════════════════

【M1 — 15要点评分】
关键点评估（每项 🔴/🟡/🟢）：
- Point 1 市场潜力：[评级] [简述]
- Point 2 管理研发意志：[评级] [简述]
- Point 4 销售组织：[评级] [简述]
- Point 5 利润率：[评级] [简述]
- Point 9 管理层授权：[评级] [简述]
- Point 15 诚信：[评级] [简述]

M1 综合评级：🔴高风险 / 🟡需关注 / 🟢值得深研

【M2 — 管理层质量】
管理深度：[评级] [简述]
长期导向：[评级] [简述]
M2 综合评级：[评级]

【M3 — 情报验证建议】
建议核实来源：[列出需要访谈的渠道]
尚待验证的关键问题：[列出]

【综合结论】
[Fisher 视角下这家公司是否值得深入研究的结论，2-3句话]

📖 原书引用：[最相关的 1 条 REF 原文]

---
以下分析基于《Common Stocks and Uncommon Profits》Fisher skill（https://book2skills.com/zh/book/common-stocks-philip-fisher），仅供学习，支持正版。
---
```

---

## 不应做的事

- ❌ 不能只用 P/E、P/B 等估值指标评判一家公司是否值得买
- ❌ 不能因为股价短期上涨就建议卖出
- ❌ 不能因为市场普遍看空就建议卖出
- ❌ 不能在没有 M1 评估基础的情况下直接讨论买入时机
- ❌ 不能忽略 Point 15（诚信）——管理层诚信有问题时直接否定整个评估
