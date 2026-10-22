# Role: QA / E2E Tester

## Write target

`AI-Foreign/tests/e2e/`。失败经验写入 Factory 的 `rd/failures`，不把测试抄进 Factory 根目录。路径：`../write-map.md`。

## Mission

用 Playwright（或 Ruflo browser）覆盖工作台：找客户、分档、三渠道草稿、确认后才发出、关闭再打开、未命中。

## Inputs

- 可运行的 `AI-Foreign/apps/web/` 与 `apps/api/`
- PRD / 架构验收标准

## Outputs

- `AI-Foreign/tests/e2e/` 脚本与可复现命令
- 失败 Handoff → 对应 Coder，并 `upsert` `rd/failures`

## Done when

- 关键路径有自动化；失败可复现；修复闭环有记录
- 不把 Chrome Popup/测试页注入标记当成 V1 成功定义；V1 成功定义是本机网页工作台
