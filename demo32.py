# -*- coding: utf8 -*-

def f(x): 
    x = 2*x
    return x

x = 1
print f(x+1)
print f(x+2)
print f(x + 1) + f(x + 2)
print x  # x=1

# n! = 1*2*3*4....*n
# n! = 1*2*3*4 ...*(n-1)*n = (n-1)! * n

def fact(n):
    if n == 1:
        return 1
    #函数自己调用自己
    return n * fact(n-1)

print fact(5)
print fact(100)

def fact2(n):
    #累乘，注意与累加的区别 s=0, s=''
    m = 1
    for x in range(1, n+1):
        m = m * x

    return m

print fact2(100)
