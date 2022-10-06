---
date created: 2022-10-05 13:34
date updated: 2022-10-05 15:04
---

## Creating tables

### Creating tables with SELECT

Creating a table with the results of a `SELECT`:

```sql
CREATE TABLE top_music_videos AS
    SELECT title, views FROM songs ORDER BY views DESC;
```

### Creating tables with UNION

使用 `SELECT` 创建一个完全新数据的行存入一个新表

```sql
CREATE TABLE musical_movies AS
    SELECT "Mamma Mia" as title, 2008 as release_year;
```

use `UNION` to merge the results of multiple `SELECT` statements:
使用 `UNION` 来合并多个 `SELECT` 语句的结果

```sql
CREATE TABLE musical_movies AS
    SELECT "Mamma Mia" as title     , 2008 as release_year UNION
    SELECT "Olaf's Frozen Adventure", 2017  UNION
    SELECT "Across the Universe"    , 2007  UNION
    SELECT "Moana"                  , 2016  UNION
    SELECT "Moulin Rouge"           , 2001;
```

### 最常见的创建方法

```sql
CREATE TABLE musical_movies (title TEXT, release_year INTEGER);

INSERT INTO musical_movies VALUES ("Mamma Mia", 2008);
INSERT INTO musical_movies VALUES ("Olaf's Frozen Adventure", 2017);
INSERT INTO musical_movies VALUES ("Across the Universe", 2007);
INSERT INTO musical_movies VALUES ("Moana", 2016);
INSERT INTO musical_movies VALUES ("Moulin Rouge", 2001);
```

## Joining tables

```sql
SELECT parent FROM parents, dogs
    WHERE child = name AND fur = "curly";
```

两个表可能共享一个列名（尤其是当它们是同一个表时！）。 点表达式和别名可以消除列值的歧义。

![](./attachments/Pasted%20image%2020221005145924.png)

```sql
CREATE TABLE grandparents AS
    SELECT a.parent AS grandog, b.child AS granpup
    FROM parents AS a, parents AS b
    WHERE b.parent = a.child;
```

## Numerical expressions

Multiple parts of a [`SELECT` statement](https://www.sqlite.org/lang_select.html) can include an **expr**ession.

`SELECT [result-column] FROM [table] WHERE [expr];`

`result-column` can expand to either `expr` AS `column-alias` or `*`.

Expressions can contain function calls and arithmetic operators.

- Combine values: `+`, `-`, `*`, `/`, `%`, `and`, `or`
- Transform values: `ABS()`, `ROUND()`, `NOT`, `-`
- Compare values: `<`, `<=`, `>`, `>=`, `<>`, `!=`, `=`

See all the possibilities for [expressions](https://www.sqlite.org/syntax/expr.html).

## String expressions

The `||` operator does string concatenation:级联

`SELECT (views || "M") as total_views FROM songs;`

There are basic functions for string manipulation操作 as well:

`SELECT SUBSTR(release_year, 3, 2) AS two_digit_year    FROM songs ORDER BY two_digit_year;`
