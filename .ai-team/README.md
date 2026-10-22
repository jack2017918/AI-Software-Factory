# AI 研发作战室（多角色协同）

本目录是**软件研发多 Agent 团队**的权威配置。目标：自动把并列目录 `AI-Foreign/` 写成可运行产品。两个文件夹只隔离资产，不禁止跨目录写。

## 原则

1. **一人一责**：每个角色一份契约（`roles/`），产物路径以 `write-map.md` 为准。
2. **交接可审计**：角色切换必须通过 `workflow.md` 的 Handoff，并 upsert 到 `rd/handoffs`。
3. **Coordinator 不写业务代码**：只拆解、路由、验收、记失败。
4. **运行时用 factory-* Agent**：映射见 `agent-map.md`。不要用 SPARC 通用人格冒充。
5. **打开父工作区**：Cursor 打开 `AI-Software/`，这样 `AI-Foreign/` 与本目录都可写。

## 目录

```
.ai-team/
  README.md           ← 本文件
  write-map.md        ← 跨目录写路径（权威）
  workflow.md         ← 交接与门禁
  agent-map.md        ← 角色 → factory-* Agent
  roles/              ← 角色契约
  missions/           ← 可执行任务包
```

## 人类负责人怎么下任务

不要说：「按 AGENTS.md 帮我把 V1 全做了。」

要说：

> 启动 Mission：`missions/v1.0.0-build.md`。  
> 以 factory-coordinator 编排；产品文件写到 `AI-Foreign/`。

## Ruflo

本机已 init `ruflo@3.57.2`（hierarchical-mesh / hybrid）。MCP：`.mcp.json`。专职 prompt 在 `.claude/agents/factory/`。在 **本仓库目录** 跑 Ruflo，但写产品时改 `../AI-Foreign`（父工作区里是 `AI-Foreign/`）。

## 与产品仓

| 写什么 | 哪里 |
| --- | --- |
| 角色、Mission、Handoff、Ruflo、`rd/*` | 本目录 |
| PRD、契约、插件、后台、采购商记忆 | `../AI-Foreign`（父工作区 `AI-Foreign/`） |

跨目录写入是设计。不要把运行时拷进 Foreign，也不要把产品写回这里。
