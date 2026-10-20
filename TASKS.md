# AI-Software-Factory 研发环境看板

## 状态说明：[ ] 待办 | [~] 进行中 | [x] 已完成

本仓库只跟踪造软件的环境。产品实现看板在并列仓库 AI-Foreign 的 `TASKS.md`。

### 环境底座

- [x] 多角色编排 `docs/architecture/ai-rd-multi-agent.md`
- [x] 角色契约与交接 `.ai-team/`
- [x] 协同冒烟 `docs/prds/phase0-smoke.md`
- [x] Ruflo `3.57.2`（hierarchical-mesh，最大并发 8，hybrid 记忆）
- [x] 与 AI-Foreign 分库（2026-10-20）：产品文档与后续代码不放在本仓库

### 使用约定

- 在本目录运行 Ruflo，维护 `.ai-team/` 与研发记忆 `rd/*`。
- 产品需求、契约、插件与 `product/buyers` 只改 AI-Foreign。
