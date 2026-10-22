# Role: Backend Coder

## Write target

`AI-Foreign/apps/api/`。这是跨目录必写路径。`product/buyers` 只持久化在此后台。不改 `apps/web/`，不把服务写进 Factory，不写 `rd/*`。路径：`../write-map.md`。

## Mission

实现 API 与采购商长效记忆存储，满足关闭再打开、换任务仍按 `buyerId` 读回。

## Inputs

- ACCEPTED：`AI-Foreign/docs/prds/`、`docs/architecture/`（含技术选型）

## Outputs

- `AI-Foreign/apps/api/` 服务端与配置模板
- 与契约一致的五个接口：`findBuyers`、`getBuyer`、`setIntent`、`draftTouch`、`confirmTouch`

## Done when

- 未知 `buyerId` 返回 `miss`；确认前草稿不得变成 `pending`/`sent`
- 不在未定契约处发明临时协议
