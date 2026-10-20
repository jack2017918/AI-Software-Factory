# PRD：phase0-smoke 多角色协同冒烟

## 1. 背景与目标

产品长期面向外贸工厂，以成交为目标，依靠长期记忆、多角色 Agent、场景 Skill 与 Chrome 插件做成可自迭代的软件。当前 Mission 是 phase0-smoke：只验证多角色协同链路能跑通，不交付插件业务功能。Phase 0 已具备 `.ai-team/` 角色契约，以及 Ruflo 3.57.2（hierarchical-mesh、最多 8 个 Agent、hybrid 记忆、HNSW、自学习）。本文件把该目标写成可验收的产品边界，供下一角色接手；架构、插件骨架与成交能力均不在本次交付内。

## 2. 范围

### In

- 用一份独立 PRD 说明：本次成功等于「协同链路可被单独验收」，不等于插件或成交功能上线。
- 给出可测试的 User Story 与验收标准，使验收人只看仓库产物即可判断通过或失败。
- 写明 Phase 1 的产品边界：下一阶段才做架构与长效记忆方案、扩展骨架、以及 Popup / 注入的端到端验证。
- 列出交给 Architect 的开放问题，且不下技术结论。

### Out

- Chrome Extension 骨架（含 React、Vite、Tailwind、Manifest V3）、Popup、页面注入。
- 用 Playwright 验证 Popup 唤起与页面注入。
- 外贸 Sales Prompt / 成交 Skill。
- 产品侧 Vector DB 选型定稿。
- 系统架构、长效记忆方案、实现代码、架构附注与交接记录。

## 3. User Story

### US-1 协同链路可以分开验收

- 作为人类发起者，我希望每个角色只交自己的产物，以便确认协同是分段完成的。
- Given 角色契约已在 `.ai-team/`，且 Ruflo 3.57.2 已按 hierarchical-mesh、最多 8 个 Agent、hybrid 记忆、HNSW、自学习初始化。
- When 按 phase0-smoke 分别启动 Product Manager，并在本 PRD 被接受后再启动 Architect。
- Then 本阶段产品侧只新增 `docs/prds/phase0-smoke.md`；不存在由同一次会话扮演全部角色写完的交付。

### US-2 阅读范围即可判断能不能做

- 作为后续角色，我希望 In / Out 足够明确，以便不会把冒烟做成插件项目。
- Given 本文第 2 节已列出 In 与 Out。
- When 对照本次新增或修改的文件。
- Then 允许存在的产品产物只有本 PRD；插件骨架、Playwright 用例、Sales Prompt、成交 Skill、Vector DB 定稿均判为超出范围。

### US-3 每条故事都能给出通过或失败

- 作为验收人，我希望故事不依赖主观感受。
- Given 本文 User Story 均写有角色、Given、When、Then。
- When 用仓库里是否存在约定文件、以及文件是否写入被禁止的实现内容来核对。
- Then 每条故事都可以标记通过或失败，且失败时能指出越界内容属于哪一条 Out。

### US-4 Phase 1 保持未开工

- 作为阶段负责人，我希望本 Mission 结束时下一阶段仍然只是边界，而不是半成品。
- Given 当前 Mission 仍是 phase0-smoke。
- When 检查仓库中与插件、测试、成交相关的新增产物。
- Then 看不到 React + Vite + Tailwind 的 Manifest V3 骨架，也看不到覆盖 Popup 唤起或页面注入的 Playwright 用例。

### US-5 Architect 收到问题而不是方案

- 作为 Architect，我希望产品只交代要决定什么，以便架构与记忆方案仍由本角色设计。
- Given 本文第 6 节为开放问题列表。
- When Architect 开始 Phase 0 的架构确认，或准备 Phase 1 设计。
- Then 能直接引用这些问题；本文未指定长效记忆介质、Vector DB、插件结构或注入实现。

## 4. 验收标准

- [ ] 存在且仅新增 `docs/prds/phase0-smoke.md`（相对本角色任务而言不改其他文件）。
- [ ] 背景与目标为一段，并写明：验证协同链路，不交付插件业务功能。
- [ ] In / Out 覆盖本文件第 2 节；Out 至少包含插件骨架、Playwright、Sales Prompt / 成交 Skill、Vector DB 定稿。
- [ ] User Story 为 5 条，且每条都能按 Given / When / Then 独立判定。
- [ ] 验收人无需阅读实现代码即可完成本清单。
- [ ] Phase 1 只出现在边界说明中，本次仓库不落地架构方案、扩展骨架与 E2E。
- [ ] 开放问题没有替 Architect 选定技术。

## 5. Phase 1 边界说明

本次不做什么：

- 不设计系统架构，不设计长效记忆方案。
- 不搭建 Chrome Extension，不引入 React、Vite、Tailwind 或 Manifest V3 工程。
- 不用 Playwright 验证 Popup 唤起或页面注入。
- 不编写外贸 Sales Prompt 或成交 Skill。
- 不把产品侧 Vector DB 选型写成定稿。

下一阶段才做什么：

- Architect 设计系统架构与长效记忆方案。
- 前端搭建 React + Vite + Tailwind 的 Chrome Extension Manifest V3 骨架。
- E2E 用 Playwright 验证 Popup 能唤起，以及页面注入可用。

仍暂缓、且本 PRD 不排入 Phase 1 必做项：外贸 Sales Prompt / 成交 Skill；产品侧 Vector DB 选型定稿。Phase 1 可以描述记忆要服务的产品对象与验收方式，但选型结论不在本文件关闭。

## 6. 交接给 Architect 的开放问题

1. 长效记忆要覆盖哪些产品对象（例如客户、询盘、协作结论），哪些必须跨 Mission 保留，哪些可以随任务结束丢弃？产品侧如何验收「记住了」？
2. 已经初始化的 Ruflo hybrid 记忆、HNSW 与自学习，和 Phase 1 要设计的长效记忆，在产品上如何分界？哪些属于研发协同记忆，哪些属于将来给外贸用户用的产品记忆？
3. 产品侧 Vector DB 定稿仍暂缓。Phase 1 的长效记忆方案是否应先定义记忆类型与读写结果，而把具体库留到定稿条件满足之后？若 Architect 认为必须更早选型，产品需要看到的验收信号是什么？
4. Phase 1 的插件骨架对用户的可感知结果是什么：Popup 唤起与页面注入各算通过的最小现象是什么？哪些站点、权限或成交相关动作明确不属于骨架？
5. 自学习在 Phase 1 应改进哪类后续决策（协作质量、记忆命中或两者都不是）？哪些学习结果允许进入下一轮任务，哪些必须由人确认后才能当成产品行为？
