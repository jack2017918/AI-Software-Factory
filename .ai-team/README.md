# AI 研发作战室（多角色协同）

本目录是**软件研发多 Agent 团队**的权威配置，替代「Cursor 读 `AGENTS.md` 单会话扮演全角色」。

## 原则

1. **一人一责**：每个角色一份契约（`roles/`），只产出自己目录下的交付物。
2. **交接可审计**：角色切换必须通过 `workflow.md` 的 Handoff，禁止口头「你现在是前端」。
3. **Coordinator 不写业务代码**：只拆解、路由、验收、记录失败经验。
4. **运行时优先 Ruflo**：Swarm / Memory / MCP；本目录是契约源，Ruflo 是执行层。

## 目录

```
.ai-team/
  README.md           ← 本文件
  workflow.md         ← 交接与门禁
  roles/              ← 角色契约（注入 Swarm Agent）
  missions/           ← 可执行任务包
```

## Ruflo 接入（推荐顺序）

本机已完成 `npx ruflo@latest init wizard`（`ruflo@3.57.2`，2026-10-20）：preset `default`，拓扑 `hierarchical-mesh`，最大并发 `8`，记忆 `hybrid` + HNSW + 自学习，嵌入模型 `Xenova/all-MiniLM-L6-v2`。运行时配置见 `.claude-flow/config.yaml`，MCP 见 `.mcp.json`。

### A. 完整 CLI（生产向）

```bash
cd /path/to/AI-Software
npx ruflo@latest init wizard
# 或非交互：
# npx ruflo@latest init
```

init 后把 `roles/*.md` 映射为 Ruflo agent 定义（或粘贴进对应 agent system prompt），用层级拓扑拉起 Coordinator + 专职角色。

### B. MCP（任意 MCP 客户端）

```bash
npx -y ruflo@latest mcp start
```

客户端配置：command `npx`，args `["-y","ruflo@latest","mcp","start"]`。

### C. Claude Code 插件（若使用 Claude Code）

见上游文档：`/plugin marketplace add ruvnet/ruflo` 后安装 `ruflo-core` / `ruflo-swarm` / `ruflo-rag-memory` / `ruflo-browser`。

## 人类负责人怎么下任务

不要说：「按 AGENTS.md 帮我把 Phase 1 全做了。」

要说：

> 启动 Mission：`missions/phase0-smoke.md`。  
> 以 Coordinator 编排；PM 与 Architect 必须产出独立文件后再进入下一角色。

## 与 AGENTS.md 的关系

| 文件 | 用途 |
| --- | --- |
| `AGENTS.md` | 角色名录（只读索引） |
| `.ai-team/` | 执行契约、交接、Mission |
| `docs/architecture/ai-rd-multi-agent.md` | 架构决策 |

## 与产品仓库的关系

产品文档和代码放在并列仓库 AI-Foreign（本地 `../AI-Foreign`）。本目录的 Mission 可以指挥去改那个仓库，但不要把插件、`product/buyers` 或产品 PRD 写回 Factory。

## 暂不包含

- 外贸产品的插件、后台和采购商记忆（在 AI-Foreign）
- 把产品记忆写入 `rd/*`
