# -*- coding: utf8 -*-

import time_series

def smallest_value(reader):
    """(file open for reading) -> NoneType
    Read and process reader and return the smallest value after the 
    time_series header.
    """
    line = time_series.skip_header(reader).strip()
    smallest = int(line)

    for line in reader:
        value = int(line.strip())

        if value < smallest:
            smallest = value 
    return smallest

if __name__ == '__main__':
    #运行这个程序
    with open('hopedale.txt', 'r') as input_file:
        print(smallest_value(input_file))

    