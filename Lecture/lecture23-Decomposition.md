---
date created: 2022-10-01 12:16
date updated: 2022-10-01 13:15
---

# Decomposition 分解

## Modules 模块

```python
// there is a link.py file in the dir
import link

from link import Link

from link import *

form link import Link as LL
```

### Running a module

`python module.py`  当这样运行时， python 将设置一个全局变量 `__name__` 到 `__main__`, 就像常常看到模块文件的底部有

```python
if __name__ == "__main__":
	# use the code in the module somehow
```

这部分代码只会在直接运行 module.py 文件的情况下执行

## Packages 包

![](./attachments/Pasted%20image%2020221001131302.png)

### 从包中导入

```python
# 导入整个路径
import sound.effect.echo
sound.effect.echo.echofilter(input, output, delay=0.1)

# 从路径导入模块
from sound.effect import echo
echo.echofilter(input, output, delay=0.1)
```

`pip install [package_name]` pip包管理器

## Modularity 模块化

设计原则: 隔离解决不同关注点的程序的不同部分

模块化组件可以独立开发和测试

分离抽象的方法:
- 函数
- 类
- 模块
- 包
## Modular design 模块设计
