def wynik(i,licznik):
    licznik+=1
    if i<3:
        return 1
    else:
        if i%2==0:
            return wynik(i-3)+wynik(i-1)+1, licznik
        else:
            return wynik(i-1)%7, licznik

licznik=0
i=int(input("Podaj i: "))
wynik=wynik(i,licznik)
print(f"Wynik: {wynik}, licznik: {licznik}")