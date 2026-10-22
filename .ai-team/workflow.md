# 多角色交接协议（Handoff Protocol）

工作区根是父目录 `AI-Software/`。路径见 `write-map.md`。跨目录写 `AI-Foreign/` 是产品 Mission 的必做动作。

## 状态机

```
BACKLOG → ASSIGNED → IN_PROGRESS → REVIEW → ACCEPTED | REJECTED → (返工 IN_PROGRESS)
```

只有 `ACCEPTED` 的上游产物，才能解锁下游角色开工。

## 标准流水线（产品 Mission）

| 顺序 | 角色 | 解锁条件 | 交付物（工作区根起算） |
| --- | --- | --- | --- |
| 0 | Coordinator | 人类下达 Mission | `AI-Software-Factory/.ai-team/missions/<id>.md` 任务表；更新两边 `TASKS.md` |
| 1 | Product Manager | Mission 已 ASSIGNED | `AI-Foreign/docs/prds/`、`AI-Foreign/docs/plans/` |
| 2 | Architect | PRD `ACCEPTED` | `AI-Foreign/docs/architecture/` |
| 3 | UI/UX Designer | PRD `ACCEPTED`（可与 Architect 并行） | `AI-Foreign/docs/design/`、`AI-Foreign/docs/prototype/` |
| 4a | Frontend Coder | Architect + UI 关键点 `ACCEPTED` | `AI-Foreign/apps/web/` |
| 4b | Backend Coder | Architect 技术选型 `ACCEPTED` | `AI-Foreign/apps/api/` |
| 5 | QA / E2E Tester | 最小可运行构建存在 | `AI-Foreign/tests/e2e/` |
| 6 | DevOps | 主路径测试通过或人类豁免 | `AI-Foreign/` 下部署文件（按 Mission） |

工厂元 Mission（如 phase0-smoke）例外：产物留在 `AI-Software-Factory/docs/`。

## Handoff 记录

每个角色完成时做两件事（缺一不可）：

1. 追加到 `AI-Software-Factory/.ai-team/missions/<id>-handoffs.md`
2. 写入 Ruflo：`python3 AI-Software-Factory/scripts/rd-memory.py upsert --namespace rd/handoffs --key <mission>:<from>-<to> --file <handoffs文件>`

```markdown
## Handoff: <from> → <to>
- Mission: <id>
- Time: <ISO8601>
- Status: ACCEPTED | REJECTED
- Artifacts:
  - AI-Foreign/path/or/AI-Software-Factory/path
- Summary: <3–5 条要点>
- Open risks: <可选>
- Reject reason: <若 REJECTED>
```

Artifacts 必须带仓库前缀。Coordinator 验收时打开该路径，确认文件在正确仓库。

## 门禁（硬规则）

1. **禁止**单 Agent 连续扮演 2 个以上角色并直接改代码而不写 Handoff。
2. **禁止** Frontend/Backend 在无 PRD 或无架构契约时新增业务模块。
3. **禁止**把产品产物写进 Factory，或把 Factory 运行时拷进 Foreign。
4. **禁止**因「另一个子目录」拒绝写入 `AI-Foreign/`。
5. E2E 失败：Handoff 回对应 Coder；修复经验 `upsert` 到 `rd/failures`。
6. 人类负责人可随时 `REJECT` 并指定返工角色；Coordinator 不得跳过角色私自代劳。
7. 下一角色开工前，用 `rd-memory.py get --namespace rd/handoffs --key …` 读回上游，而不是只靠当前会话。
8. PRD 或架构契约经 ACCEPTED 后、关闭本 Mission 前：Coordinator 必须列出过期依赖（design / architecture / plans / TASKS / 未关闭的 Mission）。无过期则 Handoff 写「无涟漪」。有过期则必须已经写好下一份 `missions/<next>.md`，并在对应 `TASKS.md` 挂 `[ ]`；只在 Open risks 写「需另开 Mission」不算关闭。无依赖的工厂演习不适用本条。
9. 派工前，若仍有文件写着禁止该任务（如「阻塞」「不要写」「本文件不表示可以开工」），Coordinator 必须先派该文件的负责角色改掉，并验收后再派目标角色。只写进 Open risks，或用「只派某一角色」跳过，这次派工无效。

## Coordinator 职责边界

| 可做 | 不可做 |
| --- | --- |
| 拆任务、指定执行角色、检查 **write-map 路径**是否存在 | 代替 Frontend/Backend 写业务实现 |
| 汇总风险、建议并行（FE/BE 分目录） | 无验收就标 ACCEPTED |
| 触发 E2E / 收集失败 / 同步 `rd/*` | 静默忽略失败继续下游 |
| PRD/契约关闭前列过期依赖；无则写「无涟漪」，有则起草下一 Mission 并挂 TASKS | 有过期依赖却只写 Open risks、不起草下一 Mission 就标关闭 |
| 派工前清掉仍禁止该任务的句子，先派文件负责人 | 禁止句只留在 Open risks 里仍标 ASSIGNED |
