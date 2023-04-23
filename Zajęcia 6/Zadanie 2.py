def potega(n):
    wynik=1
    while n>0:
        wynik*=2
        n-=1
    return wynik

n=int(input("Podaj n: "))
print(potega(n))