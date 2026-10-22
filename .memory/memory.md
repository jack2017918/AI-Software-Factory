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

## 就绪度评估（2026-10-20 晚）

当时结论：契约层够用，自动化与持久记忆不够。卡点是「分目录被理解成禁止跨目录写」。

## 已解开的卡点（同日稍后）

分目录只隔离资产。Cursor 必须打开父目录 `AI-Software/`，Factory 角色**必须**写 `AI-Foreign/`。

- 路径权威：`.ai-team/write-map.md`；父级规则 `.cursor/rules/factory-drives-foreign.mdc`
- Agent 映射：`.ai-team/agent-map.md` + `.claude/agents/factory/factory-*.md`
- 产品 Mission：`.ai-team/missions/v1.0.0-build.md`
- 研发记忆：`scripts/rd-memory.py` seed 既有 Handoff 到 `rd/*`，可用同一 key 读回
- 仍未做：T3 `apps/web` 实现与验收、E2E、Ruflo Swarm 真拉起（可选第 8 步）。形态涟漪已关闭。2026-10-21 T3 已派给 factory-frontend（ASSIGNED），未 ACCEPTED，未派 T5。

## Cursor 多 Agent 操练（2026-10-21）

第 1–7 步已通过。空对话可用 `rd/handoffs` key `cursor-drill` / `cursor-drill-parallel` 读回。日常用法：人类只说「启动 Mission …」；Coordinator 派子 Agent；专职角色只写 write-map 路径；Handoff Markdown + `rd-memory.py upsert` 缺一不可。

## 人类拍板（2026-10-21）

V1 Agent 外贸工作台形态 = **本机网页**，不是 Chrome 扩展。2026-10-21 已写入 `AI-Foreign/docs/architecture/v1.0.0-tech-stack.md`（React + Vite + Tailwind，调用 `http://127.0.0.1:3921`，目录 `apps/web`）和 write-map。原型在 `AI-Foreign/docs/prototype/`，已验收。形态涟漪 `v1.0.0-workbench-form-ripple` 已关闭：plans / design / tech-stack / 角色契约已对齐本机网页与 `apps/web`。`v1.0.0-build` 的 T3 已派给 factory-frontend，key `v1.0.0-build:coordinator-frontend`，状态 ASSIGNED。T5 未派。

## 结论怎么写（2026-10-22，人类负责人）

人类负责人指出：结论性输出太繁杂，不易读懂。经过一年升级，这个问题没有明显改变，对此失望。本条用于以后每次收束回答。

- 先写结论，三五句内说完。
- 一句能说清的，不要拆成多层标题和长清单。
- 不重复已经说过的背景。
- 只留读者要做的下一步。

同文已 upsert：`rd/conventions` key=`conclusion-output`。

## 派工前清禁止句（2026-10-22）

人类负责人确认：本会话首句已说涟漪关闭、只派 T3，Coordinator 仍把「不要写 apps/web」和计划里的「阻塞」留在 Open risks，未派 Architect 与 Product Manager 修改。这就是 T3 在文档上继续阻塞的原因。此类遗漏人很难看见，必须靠门禁，不能靠事后发现。

纪律已写入 `workflow.md` 门禁第 9 条：派工前，文件里若还写着禁止该任务，先派该文件的负责角色改掉并验收；只写 Open risks，或用「只派某一角色」跳过，派工无效。`rd/conventions` key=`dispatch-clear-forbid`。
