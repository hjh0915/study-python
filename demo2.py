x = {'胡': 572, '志': 1051,'刚': 846}
x
y = {'hu': 572, 'zhi': 1051,'gang': 846}
y
y['hu']
x['胡']
del y['zhi']
print(y)
y['hu'] = 576
print(y)
y['zhi'] = 1093
y
y.keys()
y.values()
z = {1,2,3}
z
type(z)
type(y)
z = {'a': [1, 2, 3], 'b': 89}
x
z
z['a'][1]
z['b']
z['b'][2]
dir(z)
z.__doc__
print z.__doc__
s = "hello"
dir(s)
print s.__doc__
s
s.upper()
s.upper().lower()
s2 = 'Hello World'
s2.lower()
s.lower()
s.upper()
dir(s.rindex)
s.index('l')
s
s2 = ' '*5 + 'hello'
s2
del s2[' ']
del s2[0]
s.upper()
s
s
s2
s2.lstrip()
s2.strip()
s3 = ' '*5 + 'hello' + ' ' * 5
s3
s3.lstrip()
s3.rstrip()
s3.strip()
s3
family name = 'hu'
family_name = 'hu'
first_name = 'jun hua'
x = 'hello, %s %s'
y = 'family_name' + 'first_name'
print(x % y)
print(x % family_name % first_name)
print(x % (family_name,first_name))
family_name = 'hu'
first_name = 'jun hua'
x = 'Hello, %s %s'
print(x % (family_name,first_name))
x1 = 3
y1 = 25
x2 = 2
y2 = 40
x1 * y1 + x2 * y2
x1 * y1
x2 * y2
75 + 80
games = ['watch TV','go shopping']
foods = ['fish','lemon','meat']
favorites = ['wach TV','go shopping','fish','lemon','meat']
print(favorites)
favorites = games + foods
print(favorites)
%history -f ./study/demo2.py
