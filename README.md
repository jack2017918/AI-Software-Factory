# AI-Software-Factory

Multi-agent 自动化软件开发环境。它负责多角色协同、交接门禁和 Ruflo。它本身不是外贸产品。

初衷：在父工作区里自动把并列的 [AI-Foreign](https://github.com/jack2017918/AI-Foreign) 写成可运行产品。两个文件夹是为了根目录干净，**不是**为了禁止跨目录写代码。

本地产品路径：父工作区下 `../AI-Foreign`（打开 `AI-Software/` 时是 `AI-Foreign/`）。

## 这里有什么

| 路径 | 作用 |
| --- | --- |
| `.ai-team/write-map.md` | 跨目录写路径（权威） |
| `.ai-team/agent-map.md` | 角色 → `factory-*` Agent |
| `.ai-team/missions/v1.0.0-build.md` | 当前产品 Mission |
| `.claude/agents/factory/` | 专职 Agent 定义 |
| `scripts/rd-memory.py` | 读写 `rd/*` |
| `.memory/` | 工厂侧人类备忘 |

研发记忆只用 `rd/decisions`、`rd/handoffs`、`rd/failures`、`rd/conventions`。采购商记忆 `product/buyers` 属于 AI-Foreign。

## 怎么用

1. 用 Cursor 打开**父目录** `AI-Software/`，不要只打开本文件夹。
2. 启动 Mission：`.ai-team/missions/v1.0.0-build.md`。
3. 产品代码直接写进 `AI-Foreign/`。不要把插件放进本仓库。
4. 新环境灌研发记忆：`python3 scripts/rd-memory.py seed`，读回：`python3 scripts/rd-memory.py get --namespace rd/handoffs --key v1.0.0-build:coordinator-architect`。
