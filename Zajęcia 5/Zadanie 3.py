def S(n):
    if n==0 or n==1:
        return 1
    elif n>1:
        wynik=2*S(n-1)-S(n-2)
        return wynik

n=int(input("Podaj n: "))
if n>=0:
    print(S(n))
else:
    print("Podano błędny argument")