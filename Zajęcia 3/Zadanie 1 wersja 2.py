def nwd(a, b):
    if b == 0:
        return a
    else:
        return nwd(b, a % b)

a=12
b=18
print(nwd(a,b))

a=28
b=24
print(nwd(a,b))