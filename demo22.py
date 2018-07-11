def find_two_smallest_01(L):
    """(list of float) -> tuple of (int, int)
    Return a tuple of the indices of the two smallest values in list L.
    >>> find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476])
    (6, 7)
    """
    x = min(L)
    min1 = L.index(x)
    L.remove(x)
    y = min(L)
    min2 = L.index(y)
    L.insert(min1,x)
    if min1 <= min2:
        min2 += 1
    
    return (min1, min2)

def find_two_smallest_02(L):
    """(list of float) -> tuple of (int, int)
    Return a tuple of the indices of the two smallest values in list L.
    >>> find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476])
    (6, 7)
    """
    list1 = sorted(L)
    a = list1[0]
    b = list1[1]
    min1 = L.index(a)
    min2 = L.index(b)
    return (min1, min2)

def find_two_smallest_03(L):
    """(list of float) -> tuple of (int, int)
    Return a tuple of the indices of the two smallest values in list L.
    >>> find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476])
    (6, 7)
    """

    if L[0] < L[1]:
        min1, min2 = 0, 1
    else:
        min1, min2 = 1, 0
    
    for i in range(2, len(L)):
        if L[i] < L[min1]:
            min2 = min1
            min1 = i
        elif L[i] < L[min2]:
            min2 = i 
    
    return (min1, min2)

if __name__ == '__main__':
    print find_two_smallest_01([809, 834, 477, 478, 307, 122, 96, 102, 324, 476])

    print find_two_smallest_02([809, 834, 477, 478, 307, 122, 96, 102, 324, 476])

    print find_two_smallest_03([809, 834, 477, 478, 307, 122, 96, 102, 324, 476])

