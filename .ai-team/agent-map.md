# 角色 → 运行时 Agent

权威契约在 `roles/`。Ruflo / Cursor 子 Agent 用下面的 `name` 拉起，**不要**用 SPARC 通用人格冒充本表角色。

| 角色 | 契约 | Agent name | 类型文件 |
| --- | --- | --- | --- |
| Coordinator | `roles/00-coordinator.md` | `factory-coordinator` | `.claude/agents/factory/factory-coordinator.md` |
| Product Manager | `roles/01-product-manager.md` | `factory-product-manager` | `.claude/agents/factory/factory-product-manager.md` |
| Architect | `roles/02-architect.md` | `factory-architect` | `.claude/agents/factory/factory-architect.md` |
| UI/UX Designer | `roles/03-ui-ux-designer.md` | `factory-ui-designer` | `.claude/agents/factory/factory-ui-designer.md` |
| Frontend Coder | `roles/04-frontend-coder.md` | `factory-frontend` | `.claude/agents/factory/factory-frontend.md` |
| Backend Coder | `roles/05-backend-coder.md` | `factory-backend` | `.claude/agents/factory/factory-backend.md` |
| QA / E2E Tester | `roles/06-qa-e2e-tester.md` | `factory-qa-e2e` | `.claude/agents/factory/factory-qa-e2e.md` |
| DevOps | `roles/07-devops.md` | `factory-devops` | `.claude/agents/factory/factory-devops.md` |

每个 Agent 开工前：读自己的契约 + `write-map.md`；产品文件写 `AI-Foreign/`。
完成后：Handoff Markdown + `scripts/rd-memory.py upsert`。
