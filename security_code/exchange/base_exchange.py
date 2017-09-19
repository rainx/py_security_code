#coding: utf-8
import pytz
import datetime
import six
from collections import namedtuple


LunchTimeRange = namedtuple('LunchTimeRange', ['start', 'end'])

def parse_code_range_to_dict(data, str_length):
    new_data = {}
    for k,v in data.items():
        if ':' in k:
            b, e = k.split(":")
            keys = [("{:0" + str(str_length) + "d}").format(e) for e in range(int(b), int(e)+1)]
            # print(b, e, keys)
            for key in keys:
                new_data[key] = v
        else:
            new_data[k] = v

    return new_data


class BaseExchange(object):

    # some abs static property to override
    # property ref by :
    # https://en.wikipedia.org/wiki/List_of_stock_exchanges
    # https://en.wikipedia.org/wiki/Futures_exchange
    name = "__base_exchange__"
    short_name = "__be__"
    full_name = "__full_exchange_name__"
    time_zone = pytz.UTC
    security_type_list = []
    exchange_type = '__exhange_type__'  # stock, future .. ect..
    website = 'https://...'

    other_names = []

    google_name = ""
    yahoo_name = ""

    open_time_local = datetime.time(0, 0)
    close_time_local = datetime.time(0, 0)

    lunch_time_local = LunchTimeRange(datetime.time(0, 0), datetime.time(0, 0))



    def __init__(self, *args, **kwargs):
        # all dynamic properties
        self.market_cap = None
        self.monthly_trade_volume = None

    @classmethod
    def get_xxx_type_by_code(cls, code):
        pass

    @classmethod
    def has_tag(cls, code, tag):
        entry = cls.get_xxx_type_by_code(code)
        if entry is not None:
            if ('tags' in entry) and type(entry['tags']) is list:
                for one in entry['tags']:
                    if (six.PY2 and one == str(tag)) or (not six.PY2 and tag == one):
                        return True

        return False
