# AI-Software-Factory

Multi-agent 自动化软件开发环境资产。它负责多角色研发协同、交接门禁和 Ruflo 运行时。它本身不是外贸产品。

产品在并列仓库 [AI-Foreign](https://github.com/jack2017918/AI-Foreign)。本地若与本目录并列，路径是 `../AI-Foreign`。

## 这里有什么

| 路径 | 作用 |
| --- | --- |
| `.ai-team/` | 研发角色契约、交接、Mission |
| `AGENTS.md` | 角色索引，不是单 Agent 执行入口 |
| `docs/architecture/ai-rd-multi-agent.md` | 研发编排决策 |
| `docs/prds/phase0-smoke.md` | 研发协同冒烟，不是产品需求 |
| `.claude/`、`.claude-flow/`、`.mcp.json` | Ruflo 运行时 |
| `.memory/` | 工厂侧项目记忆 |
| `archive/` | 早期对话记录 |

研发记忆只用 `rd/decisions`、`rd/handoffs`、`rd/failures`、`rd/conventions`。采购商记忆 `product/buyers` 属于 AI-Foreign，不写入本仓库。

## 怎么用

在本目录下使用 Ruflo。不要把产品插件代码放进这里。
