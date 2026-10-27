# 原创题库编写与审核规范 (Content Guidelines)

## 1. 原创题生成原则
*   题干必须基于实际场景（Scenario-based），而非单纯死记硬背。
*   干扰项（Distractors）必须是常见错误（如单位换算错误、混淆近似法规）。

## 2. 审核生命周期
1.  **Draft**: 人工或 AI 生成的初始版本，存在于隔离库中。
2.  **AI Reviewed**: 经过另一 AI Agent 的格式交叉检查，确认中英文对应正确，且 JSON 格式无误。
3.  **Technically Verified**: **最关键步骤**。必须人工/专家介入，或提供明确的法条/规范（如 BS 7671, Water Supply Regulations 1999）出处截屏/链接。
4.  **Published**: 正式向学员开放。

## 3. 敏感领域强制核实
对于以下内容，AI 生成的判断不可轻信，必须附带 `source_reference`：
*   安全间距（如 Zone 0, 1, 2）
*   水压与温度法定限制（如 TMV 设定温度，Legionella 防治要求）
*   承重限制与施工安全法规（如梯子使用角度，受限空间定义）
