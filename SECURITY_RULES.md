# 安全规则 (Security Rules)

## 1. 认证与授权 (Authentication & Authorization)
*   使用 JWT (JSON Web Tokens) 进行跨端认证。
*   严格区分 `User`（普通学员）与 `Admin/Reviewer`（审核员）。只有 Admin 可以将题目状态修改为 `Technically Verified` 或 `Published`。

## 2. 题库防污染 (Data Integrity)
*   防 SQL 注入：所有的后端数据库查询必须使用 ORM 或参数化查询。
*   题库修改留痕：所有对题目的修改（特别是法规、安全相关）必须在 `CHANGELOG` 或题目历史表中记录修改人与核实来源。

## 3. 安全相关内容的特别校验
涉及到 Gas Safe, Part P, Water Regulations 的题目内容，其变更必须引入 "双人复核" (Two-person rule) 的逻辑（一人提交，另一人 Verify）。
