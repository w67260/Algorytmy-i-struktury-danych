n=int(input("Podaj długość ciągu: "))
i=0
lista=[]
while i<n:
    x=int(input("Podaj liczbę: "))
    lista.append(x)
    i+=1
licznik=0
for j in lista:
    if j<0:
        licznik+=1
print(f"Ilość liczb ujemnych: {licznik}")