# -*- coding: utf8 -*-

def get_period(s):
    """
       提取产品周期
    
    >>> s = '债券2018年第235期三个月定开成长净值型'
    >>> '三个月'
    """
    start = s.index('期') + 1
    end = s.index('定开')
    return s[start:end]
    
def get_days(d):
    """
       


if __name__ == '__main__':
    print(get_period('债券2018年第235期三个月定开成长净值型'))
    
