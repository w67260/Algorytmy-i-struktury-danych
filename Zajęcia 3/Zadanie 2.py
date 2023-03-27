def wynik(i):
    if i < 3:
        return 1
    elif i % 2 == 0:
        return wynik(i-3) + wynik(i-1) + 1
    else:
        return wynik(i-1) % 7

for i in range(2, 9):
    result = wynik(i)
    wywolania = result - 1 if i >= 3 and i % 2 == 0 else 0
    print(f"{i} | {result} | {wywolania}")