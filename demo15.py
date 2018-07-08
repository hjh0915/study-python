f = open('work_demo9.txt','r')
x = f.readlines()
y = x[1]
print [y[:11].strip(), y[11:19]]
print y.split()

z = y.split()
print z[1]