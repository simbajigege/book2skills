# compact-memory-implementation

为 Agent 构建 compact memory 能力的开发者指南。

## 解决的问题

Agent 在长会话中上下文窗口会被耗尽。原始对话历史增长无上限，但模型 context 有上限。这个 skill 指导开发者实现一套 compact memory 机制：检测何时需要压缩、派生 compactor sub-agent 执行压缩、生成结构化摘要、在下一轮会话中恢复记忆。

## 覆盖的能力

| 能力 | 内容 |
|---|---|
| 触发时机 | token 阈值 / turn 计数 / 阶段边界三种策略 |
| Fork agent 模式 | 派生独立 compactor sub-agent 执行压缩，与主 agent 解耦 |
| 如何 compact | compact 输出 schema、compactor system prompt、历史格式化 |
| compact 后如何使用 | 系统提示注入、跨会话持久化、多次 compact 的链式更新 |

## 使用场景

- 构建需要跨会话保持状态的 Agent
- Agent 会话长度不可预测，需要自动管理 context
- 多轮研究型 / 执行型 Agent，中间决策不能丢失

## 附带脚本

```
scripts/pre_compact_extract.py
```

从会话 JSONL 提取草稿，辅助判断哪些内容值得写入记忆（原 compact-with-memory 遗留工具，可按需使用）。

```bash
python scripts/pre_compact_extract.py --latest --check-memory
```
