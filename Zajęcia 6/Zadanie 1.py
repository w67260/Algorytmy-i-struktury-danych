def wartosc_bezwzgledna(x):
    if x<0:
        wynik=x*(-1)
    else:
        wynik=x
    return wynik

x=int(input("Podaj x: "))
print(wartosc_bezwzgledna(x))
