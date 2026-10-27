# AI Agent 开发流程 (AI Development Workflow)

1.  **需求理解阶段**: AI Agent 读取 `PROJECT_CONSTITUTION.md`，确认不违反三项核心规则。
2.  **代码生成阶段**: 前后端代码生成需完全遵循 `ARCHITECTURE.md` 规定的技术栈。
3.  **题库导入流水线**:
    *   AI 解析原始文档或网页。
    *   AI 提取题干、选项，分别生成 EN 和 ZH 内容。
    *   AI 组合为相同的 JSON 结构，分配唯一 UUID。
    *   写入数据库时状态强制设为 `Draft`。
4.  **代码审查**: AI 提交代码前，必须自我检查是否留有硬编码、是否实现了 API 参数化。
