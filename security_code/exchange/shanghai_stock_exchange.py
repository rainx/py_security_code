#coding: utf-8

import pytz
import datetime
from security_code.exchange.base_exchange import BaseExchange,LunchTimeRange
from security_code.security_type.security_sub_type_for_shsz import *
import os
import yaml

class ShangHaiStockExchange(BaseExchange):
    name = "Shanghai Stock Exchange"
    short_name = "sse"
    full_name = "Shanghai Stock Exchange"
    time_zone = pytz.timezone("Asia/Shanghai")
    security_sub_type_list = []
    exchange_type = 'stock'  # stock, future .. ect..
    website = 'http://www.sse.com.cn/'

    other_names = [u'上海证券交易所', u'沪市']

    google_name = "SHA"
    yahoo_name = "SS"

    open_time_local = datetime.time(9, 30)
    close_time_local = datetime.time(15, 0)

    lunch_time_local = LunchTimeRange(datetime.time(11, 30), datetime.time(13, 0))

    def __init__(self, *args, **kwargs):
        super(ShangHaiStockExchange, self).__init__(*args, **kwargs)

    @classmethod
    def get_sub_type_by_code(cls, code):
        intcode = int(code)

        # if intcode in range(60000, 609999 + 1):
        #     return A股
        # elif intcode in range(900000, 900999 + 1):
        #     return B股
        # elif intcode in range(696, 19999 + 1)
        #     return 债券
        # elif intcode in range


if __name__ == '__main__':
    import logging
    logging.getLogger().setLevel(logging.INFO)
    logging.info(ShangHaiStockExchange.name)

    with open(os.path.join(os.path.dirname(__file__), "sse.yml")) as yaml_file:
        content = yaml.load(yaml_file.read())
        print(content['digit_1'])
        print(content['digit_1to3'])
