import time_series

def find_largest(line):
    """(str) -> int

    Reuturn the largest value in line, which is a whitespace-delimited string
    of integers that each end with a '-'.

    >>> find_largest('1. 3. 2. 5. 2')
    5
    """
    largest = -1 
    for value in line.split():
        v = int(value[:-1])

        if v > largest:
            largest = v 
    
    return largest 

def process_file(reader):
    """(file open for reading) -> int

    Read and process reader, which must start with a time_series header.
    Return the largest value after the header. There may be multiple pieces
    of data on each line.
    """

    line = time_series.skip_header(reader).strip()
    largest = find_largest(line)

    for line in reader:
        large = find_largest(line)
        if large > largest:
            largest = large
    
    return largest 

if __name__ == '__main__':
    with open('lynx.txt', 'r') as input_file:
        print(process_file(input_file))



