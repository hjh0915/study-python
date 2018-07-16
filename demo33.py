file = open('file_example.txt', 'r')
contents = file.read()
print(contents)
file.close()

with open('file_example.txt', 'r') as file:
    contents = file.read()
    print(contents)

with open('file_example.txt', 'r') as example_file:
    first_ten_chars = example_file.read(10)
    the_rest = example_file.read()

print("The first 10 characters:", first_ten_chars)
print("The rest of the file:", the_rest)

with open('file_example.txt', 'r') as example_file:
    lines = example_file.readlines()

print lines




