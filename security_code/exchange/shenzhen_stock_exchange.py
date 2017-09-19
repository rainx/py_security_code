#coding: utf-8

import pytz
import datetime
from security_code.exchange.base_exchange import BaseExchange,LunchTimeRange, parse_code_range_to_dict
import six
import os
import yaml
from security_code.exchange.exceptions import InvalidCodeException


szse_content = None
with open(os.path.join(os.path.dirname(__file__), "szse.yml")) as yaml_file:
    szse_content = yaml.load(yaml_file.read())

if szse_content is None:
    raise Exception("can not find szse.yaml")

szse_digit_1 = szse_content['digit_1']
szse_digit_1to2 = szse_content['digit_1to2']
szse_digit_1to3 = parse_code_range_to_dict(szse_content['digit_1to3'], 3)

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

    @classmethod
    def to_str_code(cls, code):
        if type(code) is six.text_type or type(code) is six.binary_type:
            return code
        else:
            return "{:0=6}".format(code)

    @classmethod
    def get_x_type_by_code(cls, code):
        code = cls.to_str_code(code)

        first_char = code[:1]
        if first_char in szse_digit_1:
            return szse_digit_1[first_char]
        else:
            if int(first_char) not in range(0, 10):
                raise InvalidCodeException("not in 0 to 10")
            else:
                return None

    @classmethod
    def get_xx_type_by_code(cls, code):
        code = cls.to_str_code(code)
        two_chars = code[:2]
        if two_chars in szse_digit_1to2:
            return szse_digit_1to2[two_chars]
        else:
            return None

    @classmethod
    def get_xxx_type_by_code(cls, code):
        code = cls.to_str_code(code)
        three_chars = code[:3]
        if three_chars in szse_digit_1to3:
            return szse_digit_1to3[three_chars]
        else:
            return None

if __name__ == '__main__':
    from security_code.security_type.tags import SecurityTags

    import pprint
    import logging
    logging.getLogger().setLevel(logging.INFO)
    logging.info(ShenZhenStockExchange.name)

    import logging
    logging.getLogger().setLevel(logging.INFO)
    logging.info(ShenZhenStockExchange.name)

    logging.info("testing 000001")
    logging.info(ShenZhenStockExchange.get_x_type_by_code("000001"))
    logging.info(ShenZhenStockExchange.get_xx_type_by_code('000001'))
    logging.info(ShenZhenStockExchange.get_xxx_type_by_code('000001'))

    logging.info("testing 300001")
    logging.info(ShenZhenStockExchange.get_x_type_by_code("300001"))
    logging.info(ShenZhenStockExchange.get_xx_type_by_code('300001'))
    logging.info(ShenZhenStockExchange.get_xxx_type_by_code('300001'))

    logging.info("testing 002120")
    logging.info(ShenZhenStockExchange.get_x_type_by_code("002120"))
    logging.info(ShenZhenStockExchange.get_xx_type_by_code('002120'))
    logging.info(ShenZhenStockExchange.get_xxx_type_by_code('002120'))


    logging.info("test 000001 is INDEX?")
    logging.info(ShenZhenStockExchange.has_tag('000001', SecurityTags.INDEX))
    logging.info("test 300001 is CHUANGYE BAN")
    logging.info(ShenZhenStockExchange.has_tag('300001', SecurityTags.CHUANGYE))