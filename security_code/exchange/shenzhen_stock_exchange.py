#coding: utf-8

import pytz
import datetime
from security_code.exchange.base_exchange import BaseExchange,LunchTimeRange
from security_code.security_type.security_sub_type_for_shsz import *

class ShenZhenStockExchange(BaseExchange):
    name = "ShenZhen Stock Exchange"
    short_name = "szse"
    full_name = "ShenZhen Stock Exchange"
    time_zone = pytz.timezone("Asia/Shanghai")
    security_sub_type_list = []
    exchange_type = 'stock'  # stock, future .. ect..
    website = 'http://www.szse.cn/'

    other_names = [u'深圳证券交易所', u'深市']

    google_name = "SHE"
    yahoo_name = "SZ"

    open_time_local = datetime.time(9, 30)
    close_time_local = datetime.time(15, 0)

    lunch_time_local = LunchTimeRange(datetime.time(11, 30), datetime.time(13, 0))

    def __init__(self, *args, **kwargs):
        super(ShenZhenStockExchange, self).__init__(*args, **kwargs)


if __name__ == '__main__':
    import logging
    logging.getLogger().setLevel(logging.INFO)
    logging.info(ShenZhenStockExchange.name)