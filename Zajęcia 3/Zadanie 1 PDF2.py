def silnia(n):
    if(n==0):
        return 1
    return silnia(n-1)*n

print("Podaj n: ")
a=int(input())
print(silnia(a))