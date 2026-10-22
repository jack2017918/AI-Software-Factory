# AI-Software-Factory 研发环境看板

## 状态说明：[ ] 待办 | [~] 进行中 | [x] 已完成

本仓库跟踪造软件的环境。产品实现看板在 `../AI-Foreign/TASKS.md`（父工作区 `AI-Foreign/TASKS.md`）。

### 环境底座

- [x] 多角色编排 `docs/architecture/ai-rd-multi-agent.md`
- [x] 角色契约与交接 `.ai-team/`
- [x] 协同冒烟 `docs/prds/phase0-smoke.md`
- [x] Ruflo `3.57.2`（hierarchical-mesh，最大并发 8，hybrid 记忆）
- [x] 与 AI-Foreign 分目录（资产隔离，不是写保护）
- [x] 跨目录写路径 `.ai-team/write-map.md` + 父工作区规则
- [x] `factory-*` Agent 映射 `.ai-team/agent-map.md`
- [x] `rd/*` 脚本 `scripts/rd-memory.py`（seed 既有 Handoff）
- [~] 产品 Mission `missions/v1.0.0-build.md`（T3 派工已有效，Status=ASSIGNED，未 ACCEPTED。`apps/web` 未交付。T5 未派）
- [x] 清除 T3 禁止句 `missions/v1.0.0-t3-clear-forbid.md`（Architect 与 Product Manager 均 ACCEPTED。未派 factory-frontend，未派 T5）
- [x] 工作台名称涟漪 `missions/v1.0.0-workbench-name-ripple.md`（依赖文件已对齐「Agent 外贸工作台」）
- [x] 工作台形态涟漪 `missions/v1.0.0-workbench-form-ripple.md`（依赖已对齐本机网页与 `apps/web`；未派 v1.0.0-build T3）
- [x] Cursor 多 Agent 演习 `cursor-drill` + `cursor-drill-parallel`

### 使用约定

- Cursor 打开父目录 `AI-Software/`。
- 产品需求、契约、本机网页工作台、后台与 `product/buyers` 写 AI-Foreign。
- 交接 Markdown 在本仓库，同时 upsert `rd/handoffs`。
