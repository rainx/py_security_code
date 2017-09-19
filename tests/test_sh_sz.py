#coding: utf-8
from __future__ import unicode_literals


from security_code import ShangHaiStockExchange, ShenZhenStockExchange, SecurityTags


def test_sz():
    assert ShenZhenStockExchange.get_x_type_by_code('000001')['name'] == 'A股'
    assert ShenZhenStockExchange.get_xx_type_by_code('000001')['name'] == 'A股证券'
    assert ShenZhenStockExchange.get_xxx_type_by_code('000001')['name'] == '主板 A 股'

    assert ShenZhenStockExchange.has_tag('000001', SecurityTags.A_SHARE)

    assert ShenZhenStockExchange.has_tag('300001', SecurityTags.CHUANGYE)

def test_sh():

    assert ShangHaiStockExchange.get_x_type_by_code('600000')['name'] == 'A股'
    assert ShangHaiStockExchange.get_xxx_type_by_code('600000')['name'] == 'A股证券'
    assert ShangHaiStockExchange.has_tag('600000', SecurityTags.A_SHARE)

