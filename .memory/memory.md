# 项目记忆

更新时间：2026-10-20

## 来源

早期对话已归档：

- `archive/AI-Software.md`：产品愿景、角色映射、Ruflo 评估
- `archive/AI-Software-2.md`：用 Cursor 组队的旧做法（单 Agent + `AGENTS.md` 已弃用）

产品文档已迁到并列仓库 AI-Foreign，不在本仓库的 `docs/prds/v1.0.0.md`。

## 产品愿景

面向外贸行业、帮助国内工厂、以**成交转化**为目标的自我迭代软件系统。

核心能力：

- 长期记忆（客户偏好、沟通历史、行业标签；Vector DB + Graph RAG）
- 多角色 Agent 协同
- 特定场景 Skill（询盘意图、动态报价与话术、浏览器插件嵌入外贸平台）

目标用户：国内工厂外贸团队。业务通道：Email / WhatsApp / Alibaba 国际站等。

产品侧核心 Skill（**尚未开工，明确暂缓 Sales Prompt 改写**）：

1. 多模态意图识别：分析询盘，用 BANT 判断购买意向
2. 动态报价与话术自迭代
3. Chrome 插件交互：嵌入外贸平台
4. 成交结果反馈循环

## AI 研发团队（当前决策）

| 项 | 结论 |
| --- | --- |
| 执行模式 | **多角色真实协同**（Ruflo Swarm + `.ai-team/` 契约） |
| 弃用 | Cursor + `AGENTS.md` **单 Agent** 推进整条研发 |
| `AGENTS.md` | 仅角色索引，非执行入口 |
| 权威配置 | `.ai-team/README.md`、`workflow.md`、`roles/*`、`missions/*` |
| 架构文档 | `docs/architecture/ai-rd-multi-agent.md` |
| 对比结论 | Phase 0 选 **ruflo** 做运行时；agency-agents 仅可作角色文案参考，不单独当编排器 |
| 暂缓 | 外贸 Sales Prompt → Skill |

角色与契约：见 `AGENTS.md` 索引表 → `.ai-team/roles/`。

## 当前阶段：环境已与产品分库（2026-10-20）

本仓库是 AI-Software-Factory。产品 AI-Foreign 在并列目录 `../AI-Foreign`。

- [x] Phase 0：编排、Ruflo 接入、`phase0-smoke` 关闭
- [x] 产品说明书、架构契约、工作台说明已迁入 AI-Foreign
- 下一步若改产品，在 AI-Foreign 里做前端工作台与 `product/buyers` 持久化
- 本仓库交接记录仍在 `.ai-team/missions/`（含当时的产品交接，作为工厂侧审计）

V1.0.0 必做：找客户、意向分档、基于记忆的 Email/WhatsApp/LinkedIn 触达草稿（确认后才发出）、采购商记忆关闭后再打开仍在。主管看板与货代履约不在本版。不承诺百雀官方指标。产品侧向量库仍后定，「记住了」的读写结果本版验收。

## Ruflo 安装结果（已核对）

| Setting | Value |
| --- | --- |
| Preset | default |
| Topology | hierarchical-mesh |
| Max Agents | 8 |
| Memory Backend | hybrid |
| HNSW | Enabled |
| Neural Learning | Enabled |
| Self-Learning | LearningBridge + Graph + Scopes |
| Embeddings | Xenova/all-MiniLM-L6-v2（首次使用时再配置） |
| Skills / Commands / Agents / Hooks | 21 / 16 / 17 / 7 |
| Cognitum 账号 | 未注册（可后补） |

配置落盘：`.claude-flow/config.yaml`、`.mcp.json`（MCP：`npx -y ruflo@latest mcp start`）。本机 PATH 上没有 `claude`，Claude Code 插件未实际安装；Cursor 走 MCP 即可。

## 仓库现状（2026-10-20）

本仓库：`.ai-team/`、`AGENTS.md`、`TASKS.md`、`.memory/`、`docs/architecture/ai-rd-multi-agent.md`、`docs/prds/phase0-smoke.md`、`docs/architecture/phase0-smoke-notes.md`、Ruflo 运行时、`archive/`。
产品文档与后续代码在 AI-Foreign。无产品应用代码。
