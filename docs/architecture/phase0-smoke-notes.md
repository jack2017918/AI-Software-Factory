# Phase 0 执行附注：拓扑与记忆 namespace

更新时间：2026-10-20

上游：已验收 PRD `docs/prds/phase0-smoke.md`；编排决策 `docs/architecture/ai-rd-multi-agent.md`；运行时 `.claude-flow/config.yaml`（Ruflo 3.57.2）。

本文件只确认 Phase 0 已安装运行时与既有编排是否一致，并回答 PRD 第 6 节交给 Architect 的五个问题。不选定产品侧 Vector DB，不设计插件实现，不展开外贸成交。

## 1. 与已安装运行时的对齐

| 项 | 编排决策 | 已安装运行时 | 是否冲突 |
| --- | --- | --- | --- |
| 拓扑 | Hierarchical Mesh；Coordinator 派活，门禁通过后专职角色可协作 | `swarm.topology: hierarchical-mesh` | 否 |
| 并发上限 | 最多 8 个 Agent | `swarm.maxAgents: 8` | 否 |
| 记忆后端 | hybrid（SQLite + AgentDB） | `memory.backend: hybrid` | 否 |
| 检索索引 | HNSW | `memory.enableHNSW: true` | 否 |
| 自学习 | 已开启 | `learningBridge.enabled: true`；`memoryGraph.enabled: true`；`agentScopes.enabled: true`（`defaultScope: project`） | 否 |

LearningBridge、Memory Graph、Agent Scopes 是编排文档里「自学习开启」的已安装机制，不是第二套拓扑，也不是产品侧记忆库。`autoScale: true` 与 `coordinationStrategy: consensus` 不提高 8 个 Agent 的上限，也不改角色契约与验收门禁。

**结论：无冲突。**

## 2. 研发侧记忆 namespace（PRD 问题 1、2）

确认继续使用编排文档中的四条研发 namespace，本阶段不新建、不改名：

| Namespace | 保留内容 | 跨 Mission |
| --- | --- | --- |
| `rd/decisions` | 已写下的 ADR 与技术选型结论 | 保留 |
| `rd/handoffs` | 已验收的角色交接摘要 | 保留 |
| `rd/failures` | 已记录的测试失败与修复经验 | 保留 |
| `rd/conventions` | 已约定的代码与目录约定 | 保留 |

### 问题 1：覆盖对象、保留与丢弃、如何验收「记住了」

- 本阶段记忆只覆盖研发协同对象：决策、交接、失败经验、目录约定。
- 客户、询盘、成交不进入任何 namespace。产品侧客户记忆（询盘/成交）本阶段不建。
- 必须跨 Mission 保留的，只有已经写入上表四条 namespace 的记录。
- 可以随任务结束丢弃的，是没有写入这些 namespace 的会话草稿、临时推理和未验收中间稿。
- 研发侧「记住了」的验收信号：下一次 Mission 用同一 namespace 和同一标识能读回已写入的内容；未写入的草稿读回为未命中。
- 产品侧「记住了客户 / 询盘 / 成交」本阶段不验收。

### 问题 2：运行时记忆与 Phase 1 长效记忆的分界

| 类别 | 归属 | 本阶段 |
| --- | --- | --- |
| 研发协同记忆 | `rd/decisions`、`rd/handoffs`、`rd/failures`、`rd/conventions`；载体是已初始化的 hybrid、HNSW 与自学习 | 确认使用 |
| 产品记忆 | 将来给外贸用户的客户、询盘、成交 | 不建 |

hybrid、HNSW、LearningBridge、Memory Graph、Agent Scopes 服务于研发协同记忆的保存与召回。它们不代替产品记忆，也不把召回结果写成外贸用户可见行为。Phase 1 设计长效记忆时，产品对象与 `rd/*` 分开命名；在产品记忆方案单独验收之前，不把客户、询盘、成交写入这四条 namespace。

## 3. 记忆类型与读写结果（PRD 问题 3）

Phase 1 先定义记忆类型与读写结果。产品侧 Vector DB 定稿继续暂缓。本文件不选定具体库，也不把某种向量库写成 Phase 1 必做项。

产品需要看到的验收信号：

1. 类型清单能区分「研发协同」与「产品对象」。产品对象可以列名，但没有记录。
2. 写入一条带类型的研发记忆后，另一次任务用同一 namespace 与同一标识能读回同一内容。
3. 读取不存在的标识时，结果是未命中，而不是另一类型的记录。
4. 客户、询盘、成交的读写结果是「未建立 / 无记录」。
5. 仓库中不出现已经关闭的产品侧 Vector DB 选型结论。

若上述信号可以靠现有 hybrid 记忆演示，就不提前定稿产品侧向量库。定稿条件仍留到产品记忆方案单独验收时再定。

## 4. 插件骨架的最小可感知结果（PRD 问题 4）

本附注只定用户能看见的通过现象，不设计插件实现。

- Popup 唤起：用户点击扩展图标后，出现扩展自身的弹层，且该弹层不属于当前网页。
- 页面注入：在约定的一张测试页上，出现扩展注入的一处可见标记。

明确不属于骨架：

- 真实外贸站点适配、询盘采集、客户建档。
- Sales Prompt、成交 Skill，以及发信、报价、跟进等成交动作。
- 产品侧客户记忆的写入。
- 超出「唤起弹层」和「测试页一处可见标记」的站点范围与权限。
- Playwright 对上述两件事的验证。那是 Phase 1 的验收手段，不是骨架功能。

## 5. 自学习的 Phase 1 边界（PRD 问题 5）

Phase 1 自学习先改进研发协作质量：失败与修复经验写入 `rd/failures`，供后续研发任务检索。本阶段不把自学习用于改进外贸用户可见行为，也不把记忆命中率本身当成产品目标。

| 结果 | 能否进入下一轮 |
| --- | --- |
| 已经写入 `rd/decisions`、`rd/handoffs`、`rd/failures`、`rd/conventions`，且经过角色验收的记录 | 可以进入下一轮研发任务 |
| LearningBridge 的权重、Memory Graph 的相似召回，以及未写入上述 namespace 的推断 | 不能当成产品行为 |
| 任何会改变外贸用户可见行为的学习结果 | 必须由人确认之后才可以 |

未经人确认的学习结果只作为研发检索材料，不自动成为产品行为。

## 6. 冲突与风险

**无冲突。**

`.claude-flow/config.yaml` 的 hierarchical-mesh、maxAgents 8、hybrid、HNSW，以及 LearningBridge / Memory Graph / Agent Scopes，与 `docs/architecture/ai-rd-multi-agent.md` 的拓扑、并发上限和研发侧四条 namespace 一致。

需要守住的边界（不是冲突）：

- `agentScopes.defaultScope` 为 `project`。研发记忆停在本项目；客户、询盘、成交不写入 `rd/*`。
- LearningBridge 与 Memory Graph 会改变召回权重。权重变化不是产品行为，遵守第 5 节。
- 产品侧 Vector DB 仍未定稿。第 3 节的验收信号不依赖具体库名。
