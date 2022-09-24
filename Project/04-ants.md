---
date created: 2022-09-21 13:46
date updated: 2022-09-21 13:46
---

构造函数 `ContainerAnt.__init__`实现如下：

```
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ant_contained = None
```

> 正如我们在 Hog 中看到的， `args`绑定到所有位置参数 （这些都是不带关键字传递的所有参数），以及 `kwargs`被束缚 到所有关键字参数。 这确保了两组参数都传递给 Ant 构造函数。
>
> 实际上，这意味着构造函数与 其父类的构造函数（ `Ant.__init__`) 但是这里我们也设置了 `self.ant_contained = None`.
