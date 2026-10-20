# Handoffs: phase0-smoke

## Handoff: Product Manager → Architect

- Mission: phase0-smoke
- Time: 2026-10-20T13:45:00+08:00
- Status: ACCEPTED
- From agent: Product Manager（独立上下文）
- Artifacts:
  - docs/prds/phase0-smoke.md
- Summary:
  - 本次成功定义为协同链路可分段验收，不交付插件。
  - In/Out 明确排除插件骨架、Playwright、Sales Skill、Vector DB 定稿。
  - 5 条 User Story 均带 Given/When/Then。
  - Phase 1 只作为边界：架构与长效记忆方案、Manifest V3 骨架、Popup/注入 E2E。
  - 第 6 节列出 5 个开放问题，未做技术选型。
- Open risks:
  - 研发记忆（Ruflo hybrid）与产品记忆的分界需 Architect 在附注中写清，但不在本次定 Vector DB。

## Handoff: Architect → Coordinator

- Mission: phase0-smoke
- Time: 2026-10-20T13:55:00+08:00
- Status: ACCEPTED
- From agent: Architect（独立上下文）
- Artifacts:
  - docs/architecture/phase0-smoke-notes.md
- Summary:
  - 已安装运行时与编排决策无冲突（hierarchical-mesh、maxAgents 8、hybrid、HNSW、自学习）。
  - 研发记忆只用 rd/decisions、rd/handoffs、rd/failures、rd/conventions；客户、询盘、成交本阶段不建。
  - Phase 1 先定义记忆类型与读写结果，产品侧 Vector DB 继续暂缓。
  - 插件骨架最小现象：点击图标出现扩展弹层；测试页出现一处注入标记。成交动作不属于骨架。
  - 自学习先改进研发协作，失败经验进 rd/failures；未经人确认的结果不当成产品行为。
- Open risks:
  - LearningBridge 会改变召回权重，权重变化不是产品行为。
