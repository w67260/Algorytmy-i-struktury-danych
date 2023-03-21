def nwd(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a
a=12
b=18
print(nwd(a,b))

a=28
b=24
print(nwd(a,b))