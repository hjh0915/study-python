def replace_items(L, D):
    """ (list of int, dict of {int: int}) -> NoneType

    Some of the items in L may be keys in D. Replace those items with the
    associated values in D.

    >>> L = [1]
    >>> replace_items(L, {1: 2})
    >>> L
    [2]
    >>> L = [3]
    >>> replace_items(L, {1: 2})
    >>> L
    [3]
    >>> L = [1, 3, 1]
    >>> replace_items(L, {1: 2, 3: 4, 5: 6})
    >>> L
    [2, 4, 2]
    """

    for x in range(len(L)):
        if L[x] in D:
            L[x] = D[L[x]]

def test(L, D):
    for k in D:
        for i in range(len(L)):
            if L[i] == k:
                L[i] = D[k]

#import doctest
#doctest.testmod()

if __name__ == '__main__':
    L = [1]
    replace_items(L, {1: 2})
    print L
    
    L = [3]
    replace_items(L, {1: 2})
    print L
    
    L = [1, 3, 1]
    replace_items(L, {1: 2, 3: 4, 5: 6})
    print L

    L = [0,1]
    replace_items(L, {0:1, 1:2})
    print L 

    L2 = [3]
    test(L2, {1: 2})
    print L2




    


