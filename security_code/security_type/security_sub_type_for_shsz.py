#coding: utf-8

import enum
from security_code.security_type.security_type import *


SecuritySubTypeForSHSZ_MASK = 1000

class SecuritySubTypeForSHSZ(object):

    def __init__(self, v):
        self.v = v


    def get_type(self):
        return SecurityType(self.v // SecuritySubTypeForSHSZ_MASK)

    def __eq__(self, other):
        return self.v == other.v


    def __repr__(self):
        return "SecuritySubTypeForSHSZ({})".format(self.v)

# https://zhidao.baidu.com/question/1498424861826836539.html

国债现货 = SecuritySubTypeForSHSZ(BondType * SecuritySubTypeForSHSZ_MASK + 1)
企业债券 = SecuritySubTypeForSHSZ(BondType * SecuritySubTypeForSHSZ_MASK + 2)
可转换债券 = SecuritySubTypeForSHSZ(BondType * SecuritySubTypeForSHSZ_MASK + 3)
国债回购 = SecuritySubTypeForSHSZ(BondType * SecuritySubTypeForSHSZ_MASK + 4)


基金 = SecuritySubTypeForSHSZ(FundType * SecuritySubTypeForSHSZ_MASK + 1)

A股 = SecuritySubTypeForSHSZ(StockType * SecuritySubTypeForSHSZ_MASK + 1)
B股 = SecuritySubTypeForSHSZ(StockType * SecuritySubTypeForSHSZ_MASK + 2)


国债期货 = SecuritySubTypeForSHSZ(FutureType * SecuritySubTypeForSHSZ_MASK + 1)

if __name__ == "__main__":
    print(国债现货)
