# Mission: phase0-smoke — 多角色协同冒烟

状态：`[x]` 已关闭（2026-10-20 Coordinator 验收）  
负责人：人类发起 → Coordinator 编排  
执行方式：Cursor 子 Agent 分角色落盘（PM、Architect 各自独立上下文）；Ruflo 运行时已 init（hierarchical-mesh / hybrid）。

## 目标

验证「多角色协同」链路可跑通，**不**交付 Chrome 插件业务功能。

## 范围 In

1. Coordinator 拆解本 Mission，写入本文件下方「任务拆解」节。
2. Product Manager 产出：`docs/prds/phase0-smoke.md`（内容可为「协同冒烟专用」最小 PRD，说明后续 Phase 1 边界即可）。
3. Architect 产出：`docs/architecture/ai-rd-multi-agent.md` 的一页「执行附注」（或新建 `docs/architecture/phase0-smoke-notes.md`），确认拓扑与记忆 namespace无冲突。
4. 两次 Handoff 记录写入：`.ai-team/missions/phase0-smoke-handoffs.md`。

## 范围 Out

- Chrome Extension 骨架、Playwright 业务用例
- 外贸 Sales / 成交 Skill
- 产品侧 Vector DB 选型定稿（留给 Phase 1 Architect 任务）

## 验收清单

- [x] 存在独立的 PM 产物文件
- [x] 存在独立的 Architect 产物或附注文件
- [x] `phase0-smoke-handoffs.md` 含 PM→Architect（或 Coordinator 验收）至少 2 条 Handoff
- [x] 全程未使用「单会话按 AGENTS.md 扮全角色写完」的方式

## 任务拆解

（由 Coordinator 填写）

| ID | 角色 | 任务 | 状态 |
| --- | --- | --- | --- |
| T1 | Coordinator | 确认角色契约与 workflow 门禁 | ACCEPTED |
| T2 | Product Manager | 写 `docs/prds/phase0-smoke.md` | ACCEPTED |
| T3 | Architect | 写 `docs/architecture/phase0-smoke-notes.md` | ACCEPTED |
| T4 | Coordinator | 验收并关闭 Mission | ACCEPTED |

## Ruflo 执行提示

```text
Mission: phase0-smoke
Topology: hierarchical
Agents: coordinator, product-manager, architect
Memory ns: rd/handoffs, rd/decisions
Constraint: no single-agent roleplay; separate artifacts per role
```
