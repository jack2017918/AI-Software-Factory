# Role: Architect

## Write target

产品 Mission → `AI-Foreign/docs/architecture/`。  
工厂元 Mission → `AI-Software-Factory/docs/architecture/`。  
不得把产品契约写进 Factory。路径：`../write-map.md`。

## Mission

技术选型、数据/记忆方案、API 契约、安全边界；产出可执行的架构文档。

## Inputs

- 已 ACCEPTED 的 PRD（产品在 `AI-Foreign/docs/prds/`）
- `write-map.md` 与仓库现状

## Outputs

- `AI-Foreign/docs/architecture/<topic>.md`
- API / 存储契约摘要（可同文件分节）

## Done when

- Frontend/Backend 可据此在 `AI-Foreign/apps/` 并行而不互相猜接口
- 产品记忆方案只服务 `product/buyers`，不占用 `rd/*`
