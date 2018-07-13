import bisect
def bin_sort(values):
    """(list) -> list

    Return a sorted version of the values.  (The does not mutate values.)
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> bin_sort(L)
    >>> L
    [-1,  2, 3, 4, 5, 7]
    """

    result = []
    for v in values:
        bisect.insort_left(result, v)

    return result

def merge(L1, L2):
    """(list, list) -> list 

    Merge sorted lists L1 and L2 into a new list and return that new list.
    >>>merge([1, 3, 4, 6], [1, 2, 5, 7])
    [1, 1, 2, 3, 4, 5, 6, 7]
    """

    newL = []
    i1 = 0 
    i2 = 0

    while i1 != len(L1) and i2 != len(L2):
        if L1[i1] <= L2[i2]:
            newL.append(L1[i1])
            i1 += 1
        else:
            newL.append(L2[i2])
            i2 += 1
        
    newL.extend(L1[i1:])
    newL.extend(L2[i2:])

    return newL

def mergesort(L):
    """ (list) -> NOneType

    Recorder the items in L from smallest to largest.

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> mergesort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """

    workspace = []
    for i in range(len(L)):
        workspace.append([L[i]])

    i = 0 
    while i < len(workspace) - 1:
        L1 = workspace[i]
        L2 = workspace[i + 1]
        newL = merge(L1, L2)
        workspace.append(newL)
        i += 2

    if len(workspace) != 0:
        L[:] = workspace[-1][:]

    return L 

if __name__ == '__main__': 
    print bin_sort([3, 4, 7, -1, 2, 5])

    print merge([1, 3, 4, 6], [1, 2, 5, 7])

    print mergesort([3, 4, 7, -1, 2, 5])


