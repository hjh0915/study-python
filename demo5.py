# -*- coding: utf8 -*-

def elec_fee(a, b):
    """
       此函数是用于计算电费
       参数a: 用电度数
       参数b: 电单价
    """
    return a*b

if __name__ == '__main__':
    print elec_fee(247, 0.60)
