cursor-drill 工厂元 Mission 编排拓扑：Coordinator 作为唯一调度入口。
Coordinator 并行派发两个专职角色，各自以独立 sub-agent 执行，互不阻塞。
两路 sub-agent 在同一 Mission 内同步推进，由 Coordinator 汇总与收口。
跨角色传递的上下文与 Handoff 不写入产品侧记忆，统一落在研发命名空间。
记忆命名空间固定为 rd/handoffs，供编排链路与角色接力读写。
