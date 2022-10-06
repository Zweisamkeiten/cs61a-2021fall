---
date created: 2022-10-06 11:56
---

## How the web works

![](./attachments/Pasted%20image%2020221006115156.png)

Webpages are made up of three languages:

- **HTML**: Contains the content and uses tags to break it into semantic chunks (headings, paragraphs, etc)
- **CSS**: Contains style rules that apply properties to elements on a page.
- **JavaScript**: Contains code that dynamically accesses and updates the page content to make it more interactive.

### 服务器是做什么的？

最基本的服务器只提供 HTML 和多媒体文件 从文件系统。

服务器端代码对于任何需要访问的东西也很有用 持久数据或需要额外的安全层 在客户端允许。

- 用户认证
- 数据库获取/更新
- 缓存

## 服务器端 Python

### 简单的 HTTP 服务器

来自标准库， [http 模块](https://docs.python.org/3/library/http.server.html) 可以运行基本服务器。 但 **不** 建议用于生产。

运行一个简单的文件服务器：

`python -m http.server 8000`

[Simple Python 3 HTTP server for logging all GET and POST requests](https://gist.github.com/Zweisamkeiten/2ab8ccdb8007f09b450b0ac2b824655d)
使用HTTP server 记录所有 GET POST 日志的代码

### Flask framework

一个外部包， [Flask](https://flask.palletsprojects.com/en/2.0.x/) 是一个轻量级框架 用于服务器请求和响应。

[本教程 # 使用 Flask 和 Replit 创建 Python Web 应用程序](https://nickymarino.com/2021/04/13/create-python-web-apps-with-flask-and-replit/) 

Flask 也可以操作数据库

### Django 框架

一个外部库，Django 是一个相当重量级 自我完备的的库 服务器端代码框架。 包括用于数据库交互的 ORM。

用 Django 编写的应用程序：

-   Coursera（最初，现在是 Scala+Play）
-   Instagram
-   Pinterest（最初，现在是 Flask）
-   Eventbrite
