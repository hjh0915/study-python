def count_letter_case_mutate(L):
    """ (list of list of str) -> NoneType

    Precondition: each str in L is non-empty and contains only alphabetic characters

    Replace each item in L with a two-item tuple in which the first item is
    the number of words in the list at the corresponding index of L that start with
    a lowercase letter and the second item is the number of words in the list at the
    corresponding index of L that start with an uppercase letter

    >>> data = [['apple', 'Banana'], ['PeAr'], [], ['PEACH', 'apRICot', 'plum']]
    >>> count_letter_case_mutate(data)
    >>> data
    [(1, 1), (0, 1), (0, 0), (2, 1)]
    """
    for i in range(len(L)):
        lowerletters = 0 
        upperletters = 0
        for word in L[i]:
            if word[0].isupper():
                upperletters = upperletters + 1
            else:
                lowerletters = lowerletters + 1
        L[i] = (lowerletters, upperletters)

if __name__ == '__main__':
    data = [['apple', 'Banana'], ['PeAr'], [], ['PEACH', 'apRICot', 'plum']]
    count_letter_case_mutate(data)
    print data 




