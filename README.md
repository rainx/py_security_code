Py Security Code
====

获取股票代码对应的详细信息


Installation
---

```
pip install py-security-code
```

Usage
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




