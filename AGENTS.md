# 编码代理执行规则 (Agents Exec Rules)

*   **Rule A**: 绝不擅自更改 `DATABASE_SCHEMA.md` 中定义的表结构。如需新增字段，需向用户提出变更请求。
*   **Rule B**: 编写组件时，必须使用现成的 Tailwind 库类，保持界面干净且具有工程感。
*   **Rule C**: AI 在处理题库清洗脚本时，必须严格应用 `Question ID` 共享原则，不能把同一个题目的中文和英文拆分成两条 SQL 插入语句，必须是 `INSERT INTO questions (id, content_en, content_zh...)`。
