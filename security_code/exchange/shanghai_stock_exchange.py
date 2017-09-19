#coding: utf-8

import pytz
import datetime
from security_code.exchange.base_exchange import BaseExchange,LunchTimeRange
from security_code.exchange.exceptions import InvalidCodeException
import os
import yaml
import six

sse_content = None
with open(os.path.join(os.path.dirname(__file__), "sse.yml")) as yaml_file:
    sse_content = yaml.load(yaml_file.read())

if sse_content is None:
    raise Exception("can not find sse.yaml")

sse_digit_1 = sse_content['digit_1']
sse_digit_1to3 = sse_content['digit_1to3']

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
    def get_types_by_code(cls, code):
        pass

    @classmethod
    def get_x_type_by_code(cls, code):
        code = cls.to_str_code(code)

        first_char = code[:1]
        if first_char in sse_digit_1:
            return sse_digit_1[first_char]
        else:
            if int(first_char) not in range(0, 10):
                raise InvalidCodeException("not in 0 to 10")
            else:
                return None

    @classmethod
    def get_xxx_type_by_code(cls, code):
        code = cls.to_str_code(code)
        three_chars = code[:3]
        if three_chars in sse_digit_1to3:
            return sse_digit_1to3[three_chars]
        else:
            return None



    @classmethod
    def to_str_code(cls, code):
        if type(code) is six.text_type or type(code) is six.binary_type:
            return code
        else:
            return "{:0=6}".format(code)




if __name__ == '__main__':
    from security_code.security_type.tags import SecurityTags
    import logging
    logging.getLogger().setLevel(logging.INFO)
    logging.info(ShangHaiStockExchange.name)

    logging.info("testing 000001")
    logging.info(ShangHaiStockExchange.get_x_type_by_code("000001"))
    logging.info(ShangHaiStockExchange.get_xxx_type_by_code('000001'))
    logging.info("testing 600000")
    logging.info(ShangHaiStockExchange.get_x_type_by_code("600000"))
    logging.info(ShangHaiStockExchange.get_xxx_type_by_code('600000'))
    logging.info("testing 999999")
    logging.info(ShangHaiStockExchange.get_x_type_by_code("999999"))
    logging.info(ShangHaiStockExchange.get_xxx_type_by_code('999999'))
    logging.info("test: 600000 is SecurityTags.A_SHARE ")
    logging.info(ShangHaiStockExchange.has_tag("600000", SecurityTags.A_SHARE))
    logging.info("test: 000001 is SecurityTags.INDEX ")
    logging.info(ShangHaiStockExchange.has_tag("000001", SecurityTags.INDEX))
