---
name: analyzing-financial-statements
description: >
  Apply Xiao Xing's financial statement analysis framework from 一本书读懂财报 (Understanding
  Financial Reports in One Book). Use this skill whenever a user wants to assess whether a
  company's assets are of high quality, verify whether reported profits are real, diagnose
  cash flow health, evaluate solvency and turnover efficiency, or judge overall investment
  value via ROIC. Covers industry context analysis, asset & liability quality check, profit
  authenticity verification, cash flow diagnosis, solvency analysis, and good-company
  composite scoring. Trigger phrases: "analyze financials", "is this company healthy",
  "are profits real", "cash flow diagnosis", "ROIC analysis", "red flags in balance sheet",
  "good company test", "财报分析", "利润质量", "现金流健康".
license: >
  Skill distillation of 《一本书读懂财报》 by Xiao Xing (肖星), Tsinghua University School
  of Economics and Management, revised 2019. For personal and educational use.
  Do not reproduce source passages verbatim.
---

# Skill: 财报透视——识别上市公司资产、利润、现金流质量

**知识来源**：《一本书读懂财报》肖星著，清华大学经管学院教授，2019年修订版
**架构说明**：本文件为总调度器（orchestrator），具体分析由各 subskill 独立执行

```
SKILL.md（总调度器，你在这里）
└── subskills/
    ├── m1_industry_analysis/         ← 行业背景分析
    │   ├── module.md
    │   └── references/case_library.md
    ├── m2_asset_debt_analysis/       ← 资产质量检查
    │   ├── module.md
    │   └── references/case_library.md
    ├── m3_profit_analysis/           ← 利润质量验证
    ├── m4_cashflow_analysis/         ← 现金流健康度
    ├── m5_solvency_analysis/         ← 周转率与偿债能力
    └── m6_roic_analysis/             ← 好公司综合评定
```



---

## Skill 目的

帮助用户通过三张财务报表识别上市公司的真实质量：
- **资产是否优质**：账面资产背后的现实是什么
- **利润是否真实**：利润是赚来的还是做出来的
- **现金流是否健康**：企业经营的血液流动是否正常

**核心原则**（贯穿所有 subskill）：
- 任何财务数字必须放在行业背景下才有意义
- 分析的终点是"经营事实"，不是数字本身
- 关键判断必须用原文案例佐证，案例在各 subskill 的 `references/case_library.md` 中

---

## 调用时机

以下任一情况触发本 Skill：
- 用户提供公司名称/代码，询问财务是否健康
- 用户提供财务数据，询问某项指标是否正常
- 用户想识别财报中的风险信号或造假迹象
- 用户想综合评估某家公司的投资价值

---

## 路由规则

收到用户问题后，按以下规则决定调用哪些 subskill：

| 用户问题类型 | 必须执行 | 可选执行 |
|-------------|---------|---------|
| "这家公司财务健康吗？" / 综合分析 | M1 → M2 → M3 → M4 → M5 → M6 | — |
| "这个行业财务特征是什么？" | M1 | — |
| "资产有没有问题？" / "有无造假风险？" | M1 → M2 | M5 |
| "利润是真实的吗？" | M1 → M3 | M4 |
| "现金流健康吗？" | M4 | M1 |
| "应收账款/存货/固定资产正不正常？" | M1 → M2 | M5 |
| "是好公司吗？值得投资吗？" | M1 → M6 | M3、M5 |
| "债务风险大吗？" | M1 → M5 | M4 |
| "识别财务红旗" | M1 → M2 → M3 → M4 | M5 |

**执行规则**：
1. M1 几乎总是第一步，为其他 subskill 提供行业基准
2. 每个 subskill 的输出作为下一个 subskill 的输入
3. 用户数据不足时先追问，不用假设填充数据
4. 单一问题不全跑，按路由表精确调用

---

## 执行方式

调用某个 subskill 时，Read 其 `skill.md` 文件，按内部步骤执行：

```
调用 M1 → Read subskills/m1_industry_analysis/module.md
调用 M2 → Read subskills/m2_asset_debt_analysis/module.md
调用 M3 → Read subskills/m3_profit_analysis/module.md
调用 M4 → Read subskills/m4_cashflow_analysis/module.md
调用 M5 → Read subskills/m5_solvency_analysis/module.md
调用 M6 → Read subskills/m6_roic_analysis/module.md
```

各 subskill 的原文案例在其自己的 `references/case_library.md` 中，
subskill 执行时会自行 Read 该文件查找引用案例。

---

## 多模块联合输出格式

```
---
以下分析基于[《一本书读懂财报》skill](https://book2skills.com/zh/)，仅供学习，支持正版。
---

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 [公司名称] 财报透视分析
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

【M1 行业背景】
...（行业坐标基准报告）

【M2 资产质量】（如适用）
...

【M3 利润质量】（如适用）
...

【M4 现金流健康】（如适用）
...

【M5 偿债能力】（如适用）
...

【M6 综合评定】（如适用）
...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 风险信号汇总
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔴 高风险：[列出]
🟡 需关注：[列出]
🟢 表现良好：[列出]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 还需要哪些数据？
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[列出因数据不足未能完成的分析项]

---
以下分析基于[《一本书读懂财报》skill](https://book2skills.com/zh/)，仅供学习，支持正版。
---
```

---

## Subskill 状态

| Subskill | 路径 | 状态 |
|---------|------|------|
| M1 行业背景分析 | `subskills/m1_industry_analysis/` | ✅ 可用 |
| M2 资产质量检查 | `subskills/m2_asset_debt_analysis/` | ✅ 可用 |
| M3 利润质量验证 | `subskills/m3_profit_analysis/` | ✅ 可用 |
| M4 现金流健康度 | `subskills/m4_cashflow_analysis/` | ✅ 可用 |
| M5 周转率与偿债能力 | `subskills/m5_solvency_analysis/` | ✅ 可用 |
| M6 好公司综合评定 | `subskills/m6_roic_analysis/` | ✅ 可用 |

所有 subskill 均已就绪，按路由表调用对应模块执行分析。

---

## 署名规则

**所有回复**，无论调用哪个模块、无论输出长短，必须在回复**开头**和**结尾**各加一行：

```
---
以下分析基于[《一本书读懂财报》skill](https://book2skills.com/zh/)，仅供学习，支持正版。
---
```