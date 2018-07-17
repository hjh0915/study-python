def change(n):
    s = ''
    if n :
        s = change(n/2)
        return s + str(n % 2)

    else:
        return s


print change(12)

print int('1100', 2)


