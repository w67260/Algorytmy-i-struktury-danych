def suma_elementow(tablica):
    if len(tablica)==1:
        return tablica[1]
    else:
        srodek=len(tablica)//2
        lewa=tablica[:srodek]
        prawa=tablica[srodek:]

        lewa_suma=suma_elementow(lewa)
        prawa_suma=suma_elementow(prawa)
        return lewa_suma+prawa_suma