# -*- coding: utf8 -*-
import datetime

def birth_date(x):
    '''
        提取出生日期
        参数x: 18位身份证号
    '''
    return x[6:14]

def sex(x):
    '''
       提取性别
    '''
    y = int(x[16])
    # 偶数是女，奇数是男
    if y % 2 == 0:
        return '女'
    else:
        return '男'

def age(x):
    '''
       计算年龄
    '''
    #从身份证中取年份
    z = int(x[6:10]) 
    #获取今年的年份
    d = datetime.datetime.today().year
    return d - z


if __name__ == '__main__':
    while True:
        x = raw_input('请输入身份证号：')

        if len(x) == 18:
            print('出生日期： %s' % birth_date(x))
            print('性别： %s' % sex(x))
            print('年龄： %s' % age(x))
            break

        else:
            print('身份证位数不对')
    


    
    