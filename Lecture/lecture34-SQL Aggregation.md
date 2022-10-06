---
date created: 2022-10-05 17:14
---

## Aggregate function 聚合函数
### 聚合函数

到目前为止，所有 SQL 表达式一次都引用了一行中的值。

`SELECT [columns] FROM [table] WHERE [expression];`

中的聚合函数 `[columns]`子句从一组行中计算一个值。

从 [这张太阳系物体表](https://gist.github.com/pamelafox/30acd9ca938c8a62fb92) 开始，找到最大的：

`SELECT MAX(mean_radius) FROM solar_system_objects;`

查看所有 [SQLite 聚合函数](https://www.sqlite.org/lang_aggfunc.html) 。

### 混合聚合函数和单个值

聚合函数还选择表中的某些行来提供列的值 未汇总的。 如果是 `MAX`或者 `MIN`, 这一行是 `MAX`或者 `MIN` 的值。z


`SELECT body, MAX(mean_radius) FROM solar_system_objects;`

`SELECT body, MAX(surface_gravity) FROM solar_system_objects;`

`SELECT body, MIN(mean_radius) FROM solar_system_objects;`

否则，单个值只会从任意行中选择：

`SELECT SUM(mass) FROM solar_system_objects;`
## Groups 组合

### 行 分组

表中的行可以使用 `GROUP BY`，并且对每个组执行聚合。

`SELECT [columns] FROM [table] GROUP BY [expression];`

组数是表达式的唯一值的数量。

根据这个 [动物表](https://gist.github.com/pamelafox/f6cd534b5042923e2d8463a485663eb0) ， 求每条腿的最大重量：

`SELECT legs, max(weight) FROM animals GROUP BY legs;`

### 过滤组 Filtering

一个 `HAVING`子句过滤聚合的组集

`SELECT [columns] FROM [table] GROUP BY [expression] HAVING [expression];`

求超过一种动物共有的体重/腿比：

`SELECT weight/legs, count(*) FROM animals     GROUP BY weight/legs HAVING COUNT(*) > 1;`
