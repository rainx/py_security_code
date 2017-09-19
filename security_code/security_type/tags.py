#coding: utf-8

import six
from enum import IntEnum

class SecurityTags(IntEnum):

    def __eq__(self, other):
        """
        字符串比较
        :param other:
        :return:
        """
        if type(other) is six.text_type or type(other) is six.binary_type:
            if type(other) is six.binary_type:
                other = other.decode("utf-8")
            return self.name.lower() == other.lower()
        else:
            return super(SecurityTags, self).__eq__(other)

    def __str__(self):
        if six.PY2:
            return self.name.lower()
        else:
            return super(SecurityTags, self).__str__()


    # base type , use area < 100

    BASE = 0  # NEVER USE THIS
    STOCK = 1
    INDEX = 2
    FUND = 3
    FUTURE = 4
    OPTION = 5
    BOND = 6
    PREFERRED_STOCK = 7

    # extends type

    # 股票相关

    A_SHARE = STOCK * 100 + 1
    B_SHARE = STOCK * 100 + 2
    ZHONGXIAO = STOCK * 100 + 3
    CHUANGYE = STOCK * 100 + 4

    # 基金

    ETF = FUND * 100 + 1
    LOF = FUND * 200 + 2


if __name__ == '__main__':
    print(SecurityTags.FUND)
    print(SecurityTags.FUND.name)
    print(SecurityTags.FUND.value)

    print (type(SecurityTags))
    print(SecurityTags.A_SHARE == SecurityTags.A_SHARE)
    print(SecurityTags.A_SHARE == "a_share")
    print(SecurityTags.A_SHARE == b"A_Share")
    print(SecurityTags.A_SHARE == 101)