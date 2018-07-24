def count_letter_case(L):
    """ (list of list of str) -> list of tuple of int

    Precondition: each str in L is non-empty and contains only alphabetic characters

    Count the number of words in each sublist of L that start with lowercase and uppercase
    letters. Return a new list where each element is a two-item tuple in which
    the first item is the number of words in the list at the corresponding index of L
    that start with a lowercase letter and the second item is the number of words in the
    list at the corresponding index of L that start with an uppercase letter.

    >>> count_letter_case([['apple', 'Banana'], ['PEAR'], [], ['PEACH', 'apRICot', 'plum']])
    [(1, 1), (0, 1), (0, 0), (2, 1)]
    """
    s = []
    for words in L:
        lowerletters = 0
        upperletters = 0
        for word in words:
            if word[0].isupper():
                upperletters = upperletters + 1
            else:
                lowerletters = lowerletters + 1
        s.append((lowerletters, upperletters))
    return s 

if __name__ == '__main__':
    x = count_letter_case([['apple', 'Banana'], ['PEAR'], [], ['PEACH', 'apRICot', 'plum']])
    print x 


