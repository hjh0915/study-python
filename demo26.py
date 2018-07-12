def linear_search_01(lst, value):
    """(list, object) -> int

    Return the index of the first occurrence of value in lst, or return 
    -1 if value is not in lst.

    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    0
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
    """

    i = 0 

    while i != len(lst) and lst[i] != value:
        i = i + 1 

    if i == len(lst):
        return -1
    else:
        return i

def linear_search_02(lst, value):
    """(list, object) -> int

    ...Exactly the same doctring goes here...
    """

    for i in range(len(lst)):
        if lst[i] == value:
            return i 

    return -1

def linear_search_03(lst, value):
    """(list, object) -> int

    ...Exactly the same doctring goes here...
    """

    lst.append(value)
    i = 0
    while lst[i] != value:
        i = i + 1

    lst.pop()

    if i == len(lst):
        return -1
    else:
        return i  


if __name__ == '__main__':
    print linear_search_01([2, 5, 8], 5)

    print linear_search_02([2, 5, 8], 8)

    print linear_search_03([2, 5, 8], 9)

    print [2, 5, 8].index(8)




    