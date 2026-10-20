# AI 研发团队：多角色协同编排（Phase 0）

更新时间：2026-10-20

## 决策

| 项 | 结论 |
| --- | --- |
| 目标 | 软件研发阶段实现**多角色真实协同**，而非单会话角色扮演 |
| 弃用 | **Cursor + `AGENTS.md` 单 Agent 推进**整条研发链路 |
| 主底座 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo)（Swarm + Memory + MCP + Browser/E2E 插件） |
| 角色素材 | 仓库内 `.ai-team/roles/` 为权威角色契约；可参考 agency-agents 的工程/产品/测试人格，但**不**作为运行时 |
| 暂缓 | 外贸 Sales Prompt → 业务 Skill 改写 |

`AGENTS.md` 仅保留为角色索引与人工查阅，**不是**执行入口。

## 为什么不是 Cursor + AGENTS.md

| 单 Agent（旧） | 多 Agent Swarm（新） |
| --- | --- |
| 一个会话切换「扮演」角色 | 多个 Agent 并行/串行，各有职责边界 |
| 上下文挤在一个窗口 | 共享记忆 + 明确产物交接 |
| 角色冲突靠提示词自律 | 编排层路由任务、验收门禁 |
| 适合问一句答一句 | 适合 Phase 1 起的完整交付流 |

## 拓扑

已安装选型：**Hierarchical Mesh**（`ruflo@3.57.2`，2026-10-20）。Coordinator 统一派活，专职角色在门禁通过后可点对点协作。并发上限 8，记忆后端 hybrid（SQLite + AgentDB，HNSW + 自学习开启）。

```
人类负责人（目标 / 审批 / 权限边界）
        │
        ▼
 Coordinator（任务拆解、路由、验收门禁、回滚）
   ├── Product Manager  → docs/prds/
   ├── Architect        → docs/architecture/
   ├── UI/UX Designer   → docs/design/（或规范片段）
   ├── Frontend Coder   → apps/extension/（或约定路径）
   ├── Backend Coder    → services/（或约定路径）
   ├── QA / E2E Tester  → tests/e2e/
   └── DevOps           → deploy/、CI 配置
```

并行规则：

- PRD 未验收前，禁止 Frontend/Backend 大规模编码。
- Architect 契约（API / 记忆方案）未落地前，Backend 不得擅自定库表。
- Frontend 与 Backend 可在契约冻结后并行。
- E2E 在 Popup + content script 最小可运行后启动；失败回传 Coder，不由 Coordinator 代写业务代码。

## 共享记忆命名空间（研发侧）

| Namespace | 内容 |
| --- | --- |
| `rd/decisions` | ADR、技术选型结论 |
| `rd/handoffs` | 角色间交接摘要 |
| `rd/failures` | 测试失败与修复经验（自迭代） |
| `rd/conventions` | 代码与目录约定 |

产品侧客户记忆（询盘/成交）**本阶段不建**。

## 与 Ruflo 的映射

| 本仓库角色 | Ruflo 能力（预期用法） |
| --- | --- |
| Coordinator | swarm / goals / workflows |
| 各专职角色 | 专用 agent 定义 + system prompt（源自 `.ai-team/roles/`） |
| 长效研发记忆 | agentdb / rag-memory |
| E2E | ruflo-browser（Playwright） |
| 质量门禁 | testgen / security-audit（按需开启） |

接入步骤见 `.ai-team/README.md`。未完成 `npx ruflo init` 前，**禁止**回退到单 Agent 用 `AGENTS.md` 冒充多角色完成 Phase 1 任务。

## 验收标准（Phase 0 完成定义）

1. `.ai-team/` 角色契约与交接协议齐全。
2. 已选定并记录 Ruflo 接入方式（CLI init 或 MCP）。
3. 存在一条可复现的「试运行 Mission」：Coordinator 拆 task → 至少 2 个专职角色产生独立产物 → 交接写入 `rd/handoffs`（或等价文件）。
4. `TASKS.md` 中 Phase 0 勾选完成；Phase 1 仅在 Phase 0 通过后启动。
