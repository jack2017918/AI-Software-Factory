# 跨目录写路径（从工作区根 `AI-Software/` 起算）

分目录 = 资产隔离。执行时 Factory 角色**应当**写入 Foreign。相对路径若省略仓库前缀，产品文件会错误落进 Factory。

`FACTORY` = `AI-Software-Factory/`  
`FOREIGN` = `AI-Foreign/`

## 产品 Mission（默认，含 v1.0.0-build）

| 角色 | 写入 |
| --- | --- |
| Product Manager | `FOREIGN/docs/prds/`、`FOREIGN/docs/plans/`、`FOREIGN/TASKS.md` |
| Architect | `FOREIGN/docs/architecture/` |
| UI/UX | `FOREIGN/docs/design/`、`FOREIGN/docs/prototype/` |
| Frontend | `FOREIGN/apps/web/` |
| Backend | `FOREIGN/apps/api/`（`product/buyers` 只在此后台） |
| QA / E2E | `FOREIGN/tests/e2e/` |
| DevOps | `FOREIGN/` 下 Docker / CI / `.env.example`（按 Mission） |

## 工厂自身（仅环境 Mission，如 phase0-smoke）

| 角色 | 写入 |
| --- | --- |
| Coordinator / 全员交接 | `FACTORY/.ai-team/missions/`、`FACTORY/TASKS.md` |
| 工厂元 PRD / 编排文档 | `FACTORY/docs/prds/`、`FACTORY/docs/architecture/` |
| 研发记忆 | Ruflo `rd/decisions`、`rd/handoffs`、`rd/failures`、`rd/conventions`（库在 `FACTORY/.swarm/`） |

## 硬规则

1. 产品 PRD、契约、插件、后台、采购商数据 **不得** 写进 `FACTORY/`。
2. `.ai-team/`、`.claude/`、`.claude-flow/`、`rd/*` **不得** 拷进 `FOREIGN/`。
3. Coordinator 验收看的是上表路径是否存在，而不是「有没有写在当前 cwd」。
4. Frontend 与 Backend 并行时：只改自己的 `apps/web` 或 `apps/api`，不改对方文件。
