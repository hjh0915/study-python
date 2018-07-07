def cheeseshop(kind, *arguments, **keywords):
    print "--Do you have any", kind, "?"
    print "--I'm sorry, we are all out of", kind
    for arg in arguments:
        print arg
    print "-" * 40
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]
cheeseshop
list(range(3, 6))
args = [3, 6]
list(range(*arg))
list(range(*args))
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(48)
f(0)
f(3)
def my_function():
    """Do you have anything?
    No,really,it dosen't do anything.
    """
    pass
print my_function._doc_
print my_function.__doc__
def my_function():
    """
    Do you have anything?
    No,really,it dosen't do anything.
    """
    pass
print my_function.__doc__
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
stack.pop()
stack
def f(x): return x % 3 == 0 or x % 5 == 0:
def f(x): return x % 3 == 0 or x % 5 == 0
filter(f, range(3, 25))
def cube(x): return x * x * x
map(cube, range(1, 11))
seq = range(8)
def add(x, y): return x + y
map(add, seq, seq)
def add(x, y): return x + y
reduce(add, range(1, 11))
range(8)
