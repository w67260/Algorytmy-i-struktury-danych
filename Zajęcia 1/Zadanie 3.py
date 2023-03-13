tablica=[1,2,3,4,5,6,7,8]
x=int(input("Podaj liczbę do sprawdzenia: "))
if x in tablica:
    print(f'Wartość {x} jest w tablicy')
else:
    print(f'Brak wartości {x} w tablicy')