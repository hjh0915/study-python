def merge_files(file_one, file_two):
    """ (file open for reading, file open for reading) -> list of str

    Precondition: both file_one and file_two are in alphabetic order;
    both file_one and file_two contain at least one line; each line
    contains one lowercase word.

    Return the combination of the lines from file_one and file_two as a list of
    strings that is in alphabetic order.

    >>> f1 = open('f1.txt')
    >>> f2 = open('f2.txt')
    >>> merge_files(f1, f2)
    ['dryden\n', 'plante\n', 'plante\n', 'potvin\n', 'roy\n', 'sawchuk\n', 'wregget\n']
    """

    merged_lines = []
    line1 = file_one.readline()
    line2 = file_two.readline()

    while line1 != '' and line2 != '':
        if line1 < line2:
            merged_lines.append(line1)
            line1 = file_one.readline()
        else:
            merged_lines.append(line2)
            line2 = file_two.readline()

    if file_one == '':
        merged_lines.append(line2)
        lastlines = file_two.readlines()
    else:
        merged_lines.append(line1)
        lastlines = file_one.readlines()
    
    merged_lines.extend(lastlines)

    return merged_lines 


if __name__ == '__main__':
    f1 = open('f1.txt')
    f2 = open('f2.txt')

    print merge_files(f1, f2)


