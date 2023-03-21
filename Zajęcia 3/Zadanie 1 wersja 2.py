def nwd(a,b):
    while b!=0:
        if b>a:
            b=a%b
            a=b


a=12
b=18
print(nwd(a,b))

a=28
b=24
print(nwd(a,b))