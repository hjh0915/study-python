# -*- coding: utf8 -*-
def complement(DNA):
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

if __name__ =='__main__':

    import doctest
    doctest.testmod()

    print complement('AATTGCCGT')






    

    