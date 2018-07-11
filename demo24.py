values = [4, 10, 3, 8, -6]
for num in values:
    num = num * 2
values
for i, num in enumerate(values):
    print "position: %s" % i
    num = num * 2
values = [4, 10, 3, 8, -6]
for i in range(len(values)):
    values[i] = values[i] * 2
values
values = [4, 10, 3, 8, -6]
for i in range(len(values)):
    print(i, values[i])
metals = ['Li', 'Na', 'K']
weights = [6.941, 22.887689, 39.67895]
for i in range(len(metals)):
    print(metals[i], weights[i])
outer = ['Li', 'Na', 'K']
inter = ['F', 'Cl', 'Br']
for metal in outer:
    for halogen in inner:
        print(metal + halogen)
outer = ['Li', 'Na', 'K']
inner = ['F', 'Cl', 'Br']
for metal in outer:
    for halogen in inner:
        print(metal + halogen)
history -f ./study/demo24.py
