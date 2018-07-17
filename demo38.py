def process_file(reader):
    """ (file open for reading) -> int

    Read and process reader, which must start with a time_series header.
    Return the largest value after the header.  There may be multiple pieces
    of data on each line.
    """

    line = reader.readline()

    line = reader.readline()
    while line.startswith('#'):
        line = reader.readline()

    largest = -1

    for value in line.split():
        v = int(value[:-1])
        if v > largest:
            largest = v

    for line in reader:
        largest_in_line = -1

        for value in line.split():
            v = int(value[:-1])
            if v > largest_in_line:
                largest_in_line = v

        if largest_in_line > largest:
            largest = largest_in_line

    return largest

if __name__ == '__main__':
    with open('lynx.txt', 'r') as input_file:
        print(process_file(input_file))


