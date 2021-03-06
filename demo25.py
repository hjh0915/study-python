# -*- coding: utf8 -*-
def print_table(n):

    """(int) -> NoneType

    Print the multiplication table for numbers 1 through n inclusive.

    >>> print_table(5)
        1     2     3     4     5
    1   1     2     3     4     5 
    2   2     4     6     8     10
    3   3     6     9     12    15
    4   4     8     12    16    20
    5   5     10    15    20    25
    """
    
    numbers = list(range(1, n + 1))

    #处理第一行
    s = ''
    for i in numbers:
        s = s + '\t' + str(i)
    print(s)

    for i in numbers:
        s = str(i)
        for j in numbers:
            s = s + '\t' + str(i * j)
        print(s)

def multiply_form(n):
    numbers = list(range(1, n + 1))

    for i in numbers:
        s = ''
        for j in numbers:
            s = s + ' '*4 + ('{0:d}x{1:d}={2:2d}'.format(i, j, i*j))
        print(s) 

def multiply_triangle(n):
    for i in range(1, 10):
        s = ''
        for j in range(1, i + 1):
            s = s + ' '*4 + ('{0:d}x{1:d}={2:2d}'.format(i, j, i*j))
        print(s) 

def multiply_reverse(n):
    for i in range(9, 0, -1):
        s = ''
        for j in range(1, i + 1):
            s = s + ' '*4 + ('{0:d}x{1:d}={2:2d}'.format(i, j, i*j))
        print(s)
            
def multiply_01(n):
    i = 1
    while i < 10:
        s = ''
        j = 1 
        while j <= i:
            s = s + ' '*4 + ('{0:d}x{1:d}={2:2d}'.format(i, j, i*j))
            j = j + 1
        i = i + 1
        print(s)

def multiply_02(n):
    i = 9
    while i >= 1:
        s = ''
        j = 1
        while j <= i:
            s = s + ' '*4 + ('{0:d}x{1:d}={2:2d}'.format(i, j, i*j))
            j = j + 1
        i = i - 1
        print(s) 



    
           

if __name__ == '__main__':

    print(print_table(5))

    print(multiply_form(9))
    
    print(multiply_triangle(9))

    print(multiply_reverse(9))

    print(multiply_01(9))

    print(multiply_02(9))








