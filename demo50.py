def return_mix(num, word):
    """(int, str) -> object

    Precondition: word contains at least 3 characters.
    """

    if word[2] == 'r':
        return (2 * num)
    elif num > 10:
        return (word + word)
    elif word[1:3] == "ab":
        return (2 == 3)

def numeric_phone(alphanumeric_phone, mapping):
    """ (str, list of str) -> int

    Preconditions:
    - len(mapping) <= 10
    - alphanumeric_phone contains only digits and uppercase letters
    - each letter in alphanumeric_phone is guaranteed to appear in mapping once
    - mapping may contain letters not in alphanumeric_phone

    Return a numeric phone number that corresponds to alphanumeric_phone.
    Each letter from alphanumeric_phone is replaced with the index of the item from
    mapping that contains the letter. Digits are not replaced.

    >>> numeric_phone('416310BELL', ['ABC', 'DEF', 'GHI', 'JKL', 'NO', 'PQRS', 'TUV', 'WXYZ'])
    4163100133
    """
    p = ''
    for i in alphanumeric_phone:
        if i.isdigit():
            p = p + i 
        else:
            for j in range(len(mapping)):
                if i in mapping[j]:
                    p = p + str(j) 
    return int(p)

def numeric_phone2(alphanumeric_phone, mapping):
    """ (str, list of str) -> int

    Preconditions:
    - len(mapping) <= 10
    - alphanumeric_phone contains only digits and uppercase letters
    - each letter in alphanumeric_phone is guaranteed to appear in mapping once
    - mapping may contain letters not in alphanumeric_phone

    Return a numeric phone number that corresponds to alphanumeric_phone.
    Each letter from alphanumeric_phone is replaced with the index of the item from
    mapping that contains the letter. Digits are not replaced.

    >>> numeric_phone('416310BELL', {'ABC': 0, 'DEF': 1, 'GHI': 2, 'JKL': 3, 'NO': 4, 'PQRS': 5, 'TUV': 6, 'WXYZ': 7})
    4163100133
    """
    p = ''
    for i in alphanumeric_phone:
        if i.isdigit():
            p = p + i 
        else:
            for k, v in mapping.items():
                if i in k:
                    p = p + str(v) 
    
    return int(p) 

if __name__ == '__main__':
    x = return_mix(-2, "cabinet")
    print x,type(x)

    x =  numeric_phone('416310BELL', ['ABC', 'DEF', 'GHI', 'JKL', 'NO', 'PQRS', 'TUV', 'WXYZ'])
    print x 
    
    y = numeric_phone2('416310BELL', {'ABC': 0, 'DEF': 1, 'GHI': 2, 'JKL': 3, 'NO': 4, 'PQRS': 5, 'TUV': 6, 'WXYZ': 7})
    print y 