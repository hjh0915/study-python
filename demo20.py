def find_two_smallest(L):
    """(list of float) -> tuple of (int, int)
    Return a tuple of the indices of the two smallest values in list L.
    >>> find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476])
    (6, 7)
    """

    smallest = min(L)
    min1 = L.index(smalllest)
    L.remove(smallest)
    next_smalllest = min(L)
    min2 = L.index(next_smalllest)
    L.insert(min1, smallest)
    if min1 <= min2:
        min2 += 1

    return (min1, min2)

def find_two_smallest(L):
    """(list of float) -> tuple of (int, int)
    Return a tuple of the indices of the two smallest values in list L.
    >>> find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476])
    (6, 7)
    """

    temp_list = sorted(L)
    smallest = temp_list[0]
    next_smalllest = temp_list[1]
    min1 = L.index(smallest)
    min2 = L.index(next_smalllest)

    return (min1, min2)

def find_two_smallest(L):
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

















