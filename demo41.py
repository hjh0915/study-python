# -*- coding: utf8 -*-

def change(n):
    """(int) -> str
    从十进制的数字转为二进制的字符串
    """

    #对于n，每次对n除以2，余数放入字符串
    #商继续除以2，所得余数继续放入字符串
    #直到商小于1为止

    s = ''
    i = n 
    while i > 0:
        s = str(i % 2) + s 
        i = i / 2

    return s 

if __name__ == '__main__':
    print change(12)

    print change(11)

        
