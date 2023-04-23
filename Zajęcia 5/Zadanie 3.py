def S(n):
    if n<2:
        return 1
    else:
        S=[0]*(n 1)
        S[0]=1
        S[1]=1
        for i in range(2, n+1):
            S[i]=2*S[i-1]*S[i-2]
        return S[n]

n=int(input("Podaj n: "))
if n>=0:
    print(S(n))
else:
    print("Podano błędny argument")