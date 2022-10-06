---
date created: 2022-10-06 12:06
date updated: 2022-10-06 12:10
---

# 学习到了什么

## 编程范式

**命令式编程：** 使用语句来改变程序的状态。

```python
nums = [1, 2, 4]
for i in range(0, len(nums)):
    nums[i] = nums[i] ** 2
```

**函数式编程：** 表达式，而不是语句； 无副作用; 使用高阶函数。

```python
list(map(lambda x: x**2, [1, 2, 4]))
```

```lisp
(map (lambda (n) (expt n 2) '(1 2 4)))
```

## 编程范式 #2

**以数据为中心** 和 **面向对象的编程** 。

```python
t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
[b.label for b in branches(t)]
```

```python
innocent_bee = Bee(5)
horrible_ant = Ant(10)
innocent_bee.fend_off(horrible_ant)
```

**声明式编程：** 说明解决方案的目标或属性，而不是程序。

```re
(.+)@(.+)\.(.{3})
```

```BNF
calc_op: "(" OPERATOR calc_expr* ")"
```

```SQL
SELECT parent FROM parents, dogs
    WHERE child = name AND fur = "curly";
```

### 编程概念

- **数据存储** ：
  - 原始/简单类型：布尔值、数字、字符串
  - 复合类型：列表、链表、树
- **环境** environments：程序如何访问和修改命名对象的规则
- **高阶函数** Higher-order functions ：作为数据值的函数，函数上的函数
- **递归** Recursion ：递归处理问题，一般递归模式
- **可变性** Mutability ：可变对象、变异操作、变异危险
- **意外** Exceptions ：处理错误
- **效率** ：不同的程序有不同的时间/空间需求

### 软件工程

- 抽象，关注点分离
- 程序规范与实现
  - 语法规范（标题）与语义规范（文档字符串）。
  - 相同抽象行为的多个实现示例
- 测试：对于每个程序，都有一个测试。
- 编码风格（作品）

### 了解更多 Python！

- [更多内置数据类型](https://docs.python.org/3/library/datatypes.html) ：集合、双端队列、日期时间
- [生成器表达式](https://realpython.com/introduction-to-python-generators/#understanding-generators)
- [线程](https://docs.python.org/3/library/threading.html#module-threading) 、 [多处理](https://docs.python.org/3/library/multiprocessing.html) 、 [队列](https://docs.python.org/3/library/queue.html)
- [非本地/全局](https://realpython.com/python-scope-legb-rule/)

### 未来的 CS 课程

- CS61B：（常规）数据结构，静态类型的生产语言。
- CS61C：程序员眼中的计算架构和硬件。
- CS70：离散数学和概率论。
- CSC100：数据科学
- CS170、CS171、CS172、CS174：“理论”——分析与建构 算法，密码学，可计算性，复杂性，组合学， 使用概率算法和分析。
- CS161：安全
- CS162：操作系统。
- CS164：编程语言的实现
- CS168：互联网简介
- CS160、CS169：用户界面、软件工程
- CS176：计算生物学

### 未来的 CS 课程 #2

- CS182、CS188、CS189：神经网络、人工智能、机器学习
- CS184：图形
- CS186：数据库
- CS191：量子计算
- CS195：计算的社会意义
- EECS 16A、16B：设计信息系统和设备
- EECS 126：概率和随机过程
- EECS149：嵌入式系统
- EECS 151：数字设计
- CS194：专题。 （例如）计算摄影和图像 操纵，密码学，网络战。
- 加上这些科目的研究生课程等等。
- 请不要忘记 CS199 和研究项目

### 加上EE课程...

- EE105：微电子器件和电路。
- EE106：机器人
- EE118、EE134：光学工程、光伏器件。
- EE120：信号和系统。
- EE123：数字信号处理。
- EE126：概率和随机过程。
- EE130：集成电路器件。
- EE137A：电源电路。
- EE140：线性集成电路（模拟电路、放大器）。
- EE142：通信集成电路。
- EE143：微加工技术。
- EE147：微机械系统（MEMS）。
- EE192：机电一体化设计。

### 练习编程

- 编程难题（HackerRank、LeetCode、Euler）
- 编程竞赛（代码出现，Kaggle）
- 黑客马拉松
- 更多范式和语言（Web 开发、嵌入式）
- 开源世界：走出去，构建一些东西！
- 个人项目
- 最重要的是：玩得开心！

## Python 的乐趣🎉 🐍

### 你可以用 Python 做什么？

几乎所有事！

- Webapp 后端 （Flask、Django）
- 网页抓取 （BeautifulSoup）
- 自然语言处理 (NLTK)
- 数据分析 （Numpy、Pandas、Matplotlib）
- 机器学习 （FastAi、PyTorch、Keras）
- 科学计算 (SciPy)
- 游戏 (Pygame)
- 程序生成 - L Systems、Noise、Markov

*除非你在使用递归时应该小心......

### 网页抓取和马尔可夫链

**网页抓取** ：通过遍历 HTML 从网页中获取数据。

**马尔可夫链** ：一种基于概率下一个标记生成序列的方法。

![马尔可夫图](https://sookocheff.com/post/nlp/ngram-modeling-with-markov-chains/following-transitions-from-I.png)

[👉🏽 演示：编写 Gobbledygooks](https://replit.com/@PamelaFox2/BeautifulSoupDemo)

进一步学习： [urllib2 模块](https://docs.python.org/3/howto/urllib2.html) ， [BeautifulSoup 文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) ， [使用马尔可夫链进行 N-Gram 建模](https://sookocheff.com/post/nlp/ngram-modeling-with-markov-chains/) ， 用于马尔可夫链的 CS70/EECS126

### 网络 API

**API** （应用程序编程接口）：一种访问功能或数据的方法 的另一个程序。

**Web API** ：一种访问在线 Web 服务的功能或数据的方法。 通常通过 HTTP 或通过 JavaScript。

[👉🏽 演示：电影混搭](https://replit.com/@PamelaFox2/BeautifulSoupDemo-MovieMarkov)

进一步学习： [urllib2 模块](https://docs.python.org/3/howto/urllib2.html) ， [电影数据库 API](https://developers.themoviedb.org/3) ， [可编程网络](https://www.programmableweb.com/)

### Turtle & L 系统

**Turtle** ：一个用于绘制图形的库（就像一支笔由一只乌龟控制）。

**L-system** ：一种并行重写系统和一种形式语法， 最初由生物学家开发，用于模拟植物的生长。

示例：公理： `A`, 规则： `A → AB`, `B → A`

`n = 0 : A n = 1 : AB n = 2 : ABA n = 3 : ABAAB`

[👉🏽 演示：L 树！](https://replit.com/@PamelaFox2/LTreeDemo)

进一步学习： [海龟模块](https://docs.python.org/3/library/turtle.html) ， [教程：海龟和弦乐和 L 系统](https://runestone.academy/runestone/books/published/thinkcspy/Strings/TurtlesandStringsandLSystems.html) ， [算法植物学：使用 L 系统的图形建模](http://paulbourke.net/fractals/lsys/) ， [L 系统示例](http://paulbourke.net/fractals/lsys/)

### 自然语言处理

NLP 包括语言建模、拼写校正、文本分类、情感分析、 信息检索、关系抽取、推荐系统、翻译问答、词向量、 和更多。

[👉🏽 演示：句子树！](https://replit.com/@PamelaFox2/NLPDemo#main.py)

进一步学习： [NLTK 书](http://www.nltk.org/book/ch08.html) ， [NLTK 情绪](https://realpython.com/python-nltk-sentiment-analysis/) 分析 [Dan Jurafsky 的讲座和书籍](https://web.stanford.edu/~jurafsky/) ， 伯克利课程：INFO 159、CS 288

### 演示：监督机器学习

![有监督的 ML 过程图](https://upload.wikimedia.org/wikipedia/commons/0/09/Supervised_machine_learning_in_a_nutshell.svg)

[👉🏽 演示：蜜蜂与黄蜂？](https://www.kaggle.com/vyombhatia/96-accuracy-with-7-lines-of-code)

进一步学习： [FastAI 文档](https://docs.fast.ai/) ， [Kaggle 机器学习教程](https://www.kaggle.com/learn/intro-to-machine-learning) ， [机器学习中的偏见](https://www.khanacademy.org/computing/ap-computer-science-principles/data-analysis-101#x2d2f703b37b450a3:machine-learning-and-bias) ， 伯克利课程：CS182、CS188、CS189
