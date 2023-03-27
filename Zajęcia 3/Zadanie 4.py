def DecToBin(n):
    if n == 0:
        return 0
    else:
        bin = DecToBin(n // 2)
        reszta = n % 2
        bin = (bin * 10) + reszta
        return bin

a=int(input("Podaj liczbę do zamiany: "))
print(DecToBin(a))