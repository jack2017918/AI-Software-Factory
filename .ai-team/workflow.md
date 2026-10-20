# 多角色交接协议（Handoff Protocol）

## 状态机

```
BACKLOG → ASSIGNED → IN_PROGRESS → REVIEW → ACCEPTED | REJECTED → (返工 IN_PROGRESS)
```

只有 `ACCEPTED` 的上游产物，才能解锁下游角色开工。

## 标准流水线（功能类 Mission）

| 顺序 | 角色 | 解锁条件 | 交付物 |
| --- | --- | --- | --- |
| 0 | Coordinator | 人类下达 Mission | 任务拆解表、角色分配、验收清单 |
| 1 | Product Manager | Mission 已 ASSIGNED | `docs/prds/<mission>.md` |
| 2 | Architect | PRD `ACCEPTED` | `docs/architecture/<topic>.md`（含 API/数据/安全边界） |
| 3 | UI/UX Designer | PRD `ACCEPTED`（可与 Architect 并行） | 交互/样式规范（约定路径） |
| 4a | Frontend Coder | Architect + UI 关键点 `ACCEPTED` | 前端/插件代码 |
| 4b | Backend Coder | Architect 契约 `ACCEPTED` | API / 记忆层代码 |
| 5 | QA / E2E Tester | 最小可运行构建存在 | `tests/e2e/` 脚本 + 报告 |
| 6 | DevOps | 主路径测试通过或人类豁免 | Docker / CI / 环境变量模板 |

## Handoff 记录模板

每个角色完成时，追加到 `.ai-team/missions/<id>-handoffs.md`（或 Ruflo `rd/handoffs`）：

```markdown
## Handoff: <from> → <to>
- Mission: <id>
- Time: <ISO8601>
- Status: ACCEPTED | REJECTED
- Artifacts:
  - path/to/file
- Summary: <3–5 条要点>
- Open risks: <可选>
- Reject reason: <若 REJECTED>
```

## 门禁（硬规则）

1. **禁止**单 Agent 连续扮演 2 个以上角色并直接改代码而不写 Handoff。
2. **禁止** Frontend/Backend 在无 PRD 或无架构契约时新增业务模块。
3. E2E 失败：Handoff 回对应 Coder；修复经验写入 `rd/failures`（或 `missions/<id>-failures.md`）。
4. 人类负责人可随时 `REJECT` 并指定返工角色；Coordinator 不得跳过角色私自代劳。

## Coordinator 职责边界

| 可做 | 不可做 |
| --- | --- |
| 拆任务、指定执行角色、检查产物路径是否存在 | 代替 Frontend/Backend 写业务实现 |
| 汇总风险、建议并行 | 无验收就标 ACCEPTED |
| 触发 E2E / 收集失败 | 静默忽略失败继续下游 |
