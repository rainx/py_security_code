#coding: utf-8
import pytz
import datetime
from collections import namedtuple


LunchTimeRange = namedtuple('LunchTimeRange', ['start', 'end'])

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