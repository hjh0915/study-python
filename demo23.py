# -*- coding: utf8 -*-
def complement_01(DNA):
    """(str) -> (str)

    Return the complement of a DNA sequence

    >>> complement('AATTGCCGT')
    'TTAACGGCA'
    """

    #转换规则：A -> T, T -> A; G -> C, C-> G

    s = ''
    for i in DNA:
        if i == 'A':
            s = s + 'T'
        elif i == 'T':
            s = s + 'A'
        elif i == 'G':
            s = s + 'C'
        elif i == 'C':
            s = s + 'G'

    return s 

def complement_02(DNA):
    """(str) -> (str)

    Return the complement of a DNA sequence

    >>> complement('AATTGCCGT')
    'TTAACGGCA'
    """

    #转换规则：
    rule = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

    s = ''
    for i in DNA:
        #print '%s => %s' % (i, rule[i])
        s = s + rule[i]                    
    return s 

if __name__ =='__main__':

    #import doctest
    #doctest.testmod()
    print complement_01('AATTGCCGT')

    print complement_02('AATTGCCGT')






    

    