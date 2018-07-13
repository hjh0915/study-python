def binary_search(L, V):
    """(list, object) -> int

    Return the index of the first occurrence of value in L, or return
    -1 if value is not in L.

    >>> binary_search([1, 3, 4, 4, 5, 6, 8, 9, 10], 1)
    0
    >>> binary_search([1, 3, 4, 4, 5, 6, 8, 9, 10], 4)
    2
    >>> binary_search([1, 3, 4, 4, 5, 6, 8, 9, 10], 5)
    4
    >>> binary_search([1, 3, 4, 4, 5, 6, 8, 9, 10], 10)
    8
    >>> binary_search([1, 3, 4, 4, 5, 6, 8, 9, 10], -3)
    -1
    >>> binary_search([1, 3, 4, 4, 5, 6, 8, 9, 10], 11)
    -1
    >>> binary_search([1, 3, 4, 4, 5, 6, 8, 9, 10], 2)
    -1
    >>> binary_search([], -3)
    -1
    >>> binary_search([1], 1)
    0
    """

    i = 0
    j = len(L) - 1
    while i != j + 1:
        m = (i + j) // 2
        if L[m] < V:
            i = m + 1 
        else:
            j = m - 1

    if 0 <= i < len(L) and L[i] == V:
        return i
    else:
        return -1

def find_largest(n, L):
    """(int, list) -> list

    Reuturn the n largest values inL in order from smallest to largest.

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> find_largest(3, L)
    [4, 5, 7]
    """

    copy = sorted(L)
    return copy[-n:]

def find_min(L, b):
    """(list, int) -> int

    Precondition: L[b:] is not empty.
    Reutrn the index of the smallest value in L[b:].

    >>> find_min([3, -1, 7, 5], 0)
    1
    >>> find_min([3, -1, 7, 5], 1)
    1
    >>> find_min([3, -1, 7, 5], 2)
    3
    """

    smallest = b 
    i = b + 1
    while i != len(L):
        if L[i] < L[smallest]:
            smallest = i 

        i = i + 1

    return smallest

def selection_sort(L):
    """ (list) -> NoneType

    Recorder the items in L from smallest to largest.

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> selection_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """

    i = 0
    while i != len(L):
        smallest = find_min(L, i)
        L[i], L[smallest] = L[smallest], L[i]
        i = i + 1

def insert(L, b):
    """(list, int) -> NoneType

    Precondition: L[0:b] is already sorted.
    Insert L[b] where it belongs in L[0:b + 1].

    >>> L = [3, 4, -1, 7, 2, 5]
    >>> insert(L, 2)
    >>> L 
    [-1, 2, 3, 4, 7, 5]
    >>> insert(L, 4)
    >>> L
    [-1, 2, 3, 4, 7, 5]
    """

    i = b 
    while i != 0 and L[i - 1] >= L[b]:
        i = i - 1

    value = L[b]
    del L[b]
    L.insert(i, value)

def insertion_sort(L):
    """(list, int) -> NoneType

    Recorder the items in L from smallest to largest.

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> insertion_sort(L)
    >>> L 
    [-1, 2, 3, 4, 5, 7]
    """

    i = 0 
    while i != len(L):
        insert(L, i)
        i = i + 1




if __name__ == '__main__':
    #import doctest
    #doctest.testmod()

    print binary_search([1, 3, 4, 4, 5, 6, 8, 9, 10], 2)

    print find_largest(1, [3, 4, 7, -1, 2, 5])

    print find_min([3, -1, 7, 5], 1)

    print selection_sort([3, 4, 7, -1, 2, 5])

    L1 = [3, 4, 7, -1, 2, 5]
    insertion_sort(L1)
    print L1


    print insert([3, 4, 7, -1, 2, 5], 5)






   
    
