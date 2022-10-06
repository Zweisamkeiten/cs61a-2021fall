---
date created: 2022-10-03 20:08
date updated: 2022-10-03 22:29
---

# 正则表达式

## 声明式语言 Declarative languages

**命令式**语言:

- 程序是对计算过程的描述
- 解释器执行 执行/计算 规则

**声明式**语言:

- 程序是对期望结果的描述
- 解释器计算得出如何生成结果
- Ex:
  - RE 正则表达式 `Good (?:morning|evening)`
  - Backus-Naur Form:
    - `?calc_expr: NUMBER | calc_op`
    - `calc_op: "(" OPERATOR calc_expr* ")"`
  - SQL: `select max(longitude) from cities where longitude >= 115`

### domain-specific 特定领域的语言

许多声明式语言都用于特定领域： 目的为解决特定领域的问题， 而不是作为一般用途的多领域语言

| 语言               | 领域           |
| ---------------- | ------------ |
| RE 正则            | 模式匹配字符串      |
| Backus-Naur Form | 分析字符串生成分析树   |
| SQL              | 查询和修改数据库的数据表 |
| HTML             | 描述网页内容的语义结构  |
| CSS              | 通过选择器为网页增加样式 |
| Prolog           | 描述和查询逻辑关系    |

## 正则表达式语法 Regular expression syntax

### 模式匹配

```python
def is_email_address(str):
    parts = str.split('@')
    if len(parts) != 2:
        return False
    domain_parts = parts[1].split('.')
    return len(domain_parts) >= 2 and len(domain_parts[-1]) == 3
```

等价于
`(.+)@(.+)\.(.{3})`
与普通的表达，编程员可以仅描述的图案 使用共同的语法和一个经常的表达引擎数字如何 做模式匹配。
![](./attachments/Pasted%20image%2020221003213907.png)
![](./attachments/Pasted%20image%2020221003213916.png)
![](./attachments/Pasted%20image%2020221003213929.png)
![](./attachments/Pasted%20image%2020221003214306.png)
![](./attachments/Pasted%20image%2020221003214334.png)
![](./attachments/Pasted%20image%2020221003214743.png)

## 在 Python 中使用正则表达式

### Raw strings 原字符串

常规 Python 字符串中 `\` 反斜杠表示转义

```python
>>> print("I have\na newline in me.")
I have
a newline in me 
```

但是反斜杠在正则表达式中有特殊含义。因此使用 `r` 前缀 prefixing the string with an `r`: 表示

```python
pattern = r"\b[ab]+\b"
```

![](./attachments/Pasted%20image%2020221003215101.png)

Match匹配对象也带有已匹配的信息，`.group()` method 可以访问

```python
x = "This string contains 35 characters."
mat = re.search(r'\d+', x)
mat.group(0)               # 35
```

### group 匹配

![](./attachments/Pasted%20image%2020221003215816.png)
![](./attachments/Pasted%20image%2020221003215852.png)
![](./attachments/Pasted%20image%2020221003215909.png)

## 模糊的正则表达

正则表达虽然匹配，但是得到的结果不同，造成模糊
![](./attachments/Pasted%20image%2020221003220031.png)
![](./attachments/Pasted%20image%2020221003220311.png)
python 的匹配是贪婪的, 从左至右尽可能的多匹配
![](./attachments/Pasted%20image%2020221003220436.png)
通过增加问号❓，来取消贪婪匹配，而选择最小匹配
![](./attachments/Pasted%20image%2020221003220541.png)

- [Very long regular expressions](https://blog.codinghorror.com/regex-use-vs-regex-abuse/) can be difficult for other programmers to read and modify. 🤯  很长的正则是难以阅读和修改的
  See also: [Write-only](https://en.wikipedia.org/wiki/Write-only_language)
- Since regular expressions are declarative, it's not always clear how efficiently they'll be processed. 🐌 Some processing can be so time-consuming, it can [take down a server.](https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS) 声明式的表达式效率较差，导致程序减慢
- Regular expressions can't parse everything! [Don't write an HTML parser with regular expressions.](https://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags) 正则表达式无法解析任何。

捕获组的第一个运用：`用来拆分匹配到的数据`。
![](./attachments/Pasted%20image%2020221003222750.png)
捕获组的第二个运用：`反向引用`。
`(\d{2})\1`，把`\d{2}`匹配到的内容先保存到捕获组1中，然后再对捕获组1进行引用，当`(\d{2})`匹配到的是12的时候，`\1`就表示12，当`(\d{2})`匹配到的是34的时候，`\1`就是34。

捕获组其实是分为编号捕获组`Numbered Capturing Groups`和命名捕获组`Named Capturing Groups`的，我们上面说的捕获组，默认指的是编号捕获组。命名捕获组，也是捕获组，只是语法不一样。命名捕获组的语法如下：`(?<name>group)` 或 `(?'name'group)`，其中`name`表示捕获组的名称，`group`表示捕获组里面的正则。

