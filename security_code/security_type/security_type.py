import enum


class SecurityType(enum.IntEnum):
    BASE = 0
    STOCK = 1
    INDEX = 2
    FUND = 3
    FUTURE = 4
    OPTION = 5
    BOND = 6
    PREFERRED_STOCK = 7

StockType = SecurityType(SecurityType.STOCK)
IndexType = SecurityType(SecurityType.INDEX)
FundType = SecurityType(SecurityType.FUND)
FutureType = SecurityType(SecurityType.FUTURE)
OptionType = SecurityType(SecurityType.OPTION)
BondType = SecurityType(SecurityType.BOND)
PreferredStockType = SecurityType(SecurityType.PREFERRED_STOCK)


if __name__ == '__main__':
    p = print
    p(StockType == StockType)
    p(StockType == SecurityType.STOCK)
    p(StockType == SecurityType.FUND)
    p(StockType)
    p(StockType.value)
    import pickle
    o = pickle.dumps(StockType)
    p(o)
    r = pickle.loads(o)
    print(r)
    print(r == StockType)

