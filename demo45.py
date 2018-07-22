def test(L, D):
    for k in D:
        for i in range(len(L)):
            if L[i] == k:
                L[i] = D[k]

if __name__ == '__main__':

    L = [0,1]
    test(L, {0: 5, 5: 2})
    print L 

    L = [3, 1]
    test(L, {3: 5, 5: 2})
    print L 

    L = [3, 1]
    test(L, {3: 5, 5: 2, 1: 7, 7: 10})
    print L 
    