def P(i,j):
    if i>0 and j==0:
        return 0
    elif i==0 and j>0:
        return 1
    elif i>0 and j>0:
        wynik=(P(i-1,j)+P(i,j-1))/2
        return wynik

i=int(input("Podaj pierwszy wymiar tablicy (i): "))
j=int(input("Podaj drugi wymiar tablicy (j): "))
if i==0 and j==0:
    print("Błędne wymiary")
elif i>=0 and j>=0:
    print(P(i,j))
else:
    print("Błędne wymiary")