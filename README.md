Py Security Code
====

获取股票代码对应的详细信息


安装（Installation）
---


```python
pip install http+git@github.com:rainx/py_security_code.git
```
or 
```
pip install py-security-code
```

使用说明（Usage）
---

导入

```python
from security_code import ShenZhenStockExchange, ShangHaiStockExchange, SecurityTags
```

获取代码的信息，根据前3， 2， 1字节的信息

```python
In [7]: ShenZhenStockExchange.get_xxx_type_by_code('000001')
Out[7]: {'name': '主板 A 股', 'tags': ['a_share', 'stock']}

In [8]: ShenZhenStockExchange.get_xx_type_by_code('000001')
Out[8]: {'name': 'A股证券'}

In [9]: ShenZhenStockExchange.get_x_type_by_code('000001')
Out[9]: {'name': 'A股'}

```

判断代码是否属于某个标签

```python
In [10]: ShenZhenStockExchange.has_tag('000001', SecurityTags.A_SHARE)
Out[10]: True

In [11]: ShenZhenStockExchange.has_tag('000001', SecurityTags.STOCK)
Out[11]: True

In [12]: ShenZhenStockExchange.has_tag('000001', SecurityTags.INDEX)
Out[12]: False
```

提交PR
----

非常欢迎提交PR给本仓库，本仓库需要如下几方面的帮助：

1. 针对后续各个交易所的公告信息，修正和追加新的信息到  sse.yml , szse.yml 等文件
1. 追加标签，目前针对 xxx(1to3)级别的信息，会对代码段进行打标签，由于我本人不是金融专业，所以很多标签没有整理，建议增加更丰富的标签。
1. 提供更多的市场(尤其是数字编号的市场)支持，如港交所等... 




