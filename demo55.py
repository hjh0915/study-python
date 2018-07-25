def populate_dictionary(definition_file):
    """ (file open for reading) -> dict of {str: list of str}

    Preconditions:
    - definition_file contains 0 or more entries with the following format:
    - 1 line containing a word
    - 0 or more lines with a definition of that word (one definition per line)
    - there will be one blank line between entries

    Return a dictionary where each key is a word and each value is the list of
    definitions of that word from definition_file. Even if a word has 0 definitions,
    it should appear as a key in the dictionary.
    """
    d = {}
    x = definiton_file.readline()
    while words != '':
        d[word] = []
        x = definition_file.readline()
        while x != '':
            d[word].append(x)
            x = definiton_file.readline()
    
    return d 

if __name__ == '__main__':
    import doctest
    doctest.testmod()