# -*- coding: utf8 -*-

#你要把这个文件，重命名为time_series.py
def skip_header(reader):
    """(file open for reading) -> str
    Skip the header in reader and return the first real piece of data.
    """
    line = reader.readline()
    while line.startswith('#'):
        line = reader.readline()

    return line

def process_file(reader):
    """(file open for reading) -> NoneType
    Read and print the data from reader, which must start with a single
    desciption line, then a sequence of lines beginning with '#', then a
    sequence of data.
    """
    line = skip_header(reader).strip()
    print(line)

    for line in reader:
        line = line.strip()
        print(line)


if __name__ == '__main__':

    with open('hopedale.txt', 'r') as input_file:
        process_file(input_file)
        


