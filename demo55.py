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
    x = definition_file.readline().strip()
    while x != '':
        d[x] = []
        y = definition_file.readline().strip()
        while y != '':
            d[x].append(y)
            y = definition_file.readline().strip()
        x = definition_file.readline().strip()
     
    return d 

if __name__ == '__main__':
    f = open('definition_file.txt', 'r')

    print populate_dictionary(f)

    