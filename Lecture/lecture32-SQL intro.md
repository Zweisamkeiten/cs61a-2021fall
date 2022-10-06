---
date created: 2022-10-05 13:19
date updated: 2022-10-05 13:33
---

## 数据库

DBMS(Database management systems)

MySQL, Oracle, PostgreSQL, MS SQL Server, MongoDB, Redis

特点

- 用结构化的方式存储数据
- 更新数据
- 查询数据
- 优化以上所有操作

关系型数据库: 关系型数据库由带有数据的表组成，且通常表之间相互关联

### Table

**Table** 是记录的集合, 包含多行，行内是每一列都有一个值

column 列 有名称和类型

## SQL

SQL 是一种声明式编程语言，用于关系型数据库, 同时它有许多变种, SQLite, 是SQL的轻量级实现

包含以下语句

- 查询一个表中的数据行 (`SELECT ...`)
- 创建新表 (`CREATE ...`)
- 插入数据到表中 (`INSERT ...`)
- 更新表中已有的行 (`UPDATE ...`)
- 删除表中的数据 (`DELETE ...`)

## 查询表 Querying tables

![](./attachments/Pasted%20image%2020221005133219.png)
**SELECT * FROM a, b** 就是求 a,b 的笛卡尔积
![](./attachments/Pasted%20image%2020221005133238.png)
![](./attachments/Pasted%20image%2020221005133249.png)
The `SELECT` statement supports a wide array of optional clauses. See the full description in the [SQLite SELECT documentation](https://www.sqlite.org/lang_select.html).
