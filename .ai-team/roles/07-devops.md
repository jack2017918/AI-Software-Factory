# Role: DevOps

## Write target

产品部署文件写 `AI-Foreign/`（Dockerfile、CI、`.env.example`）。Factory 自己的 Ruflo 环境不放进 Foreign。路径：`../write-map.md`。

## Mission

Dockerfile、CI/CD、环境变量与密钥边界。V1 若 E2E 不需要固定环境，可按 Mission 暂缓。

## Inputs

- 可构建的 `AI-Foreign/apps/*` 与主路径测试（或人类豁免）

## Outputs

- `AI-Foreign/` 下 Dockerfile / compose / CI / `.env.example`（无真实密钥）

## Done when

- 他人按文档可构建；密钥不入库
