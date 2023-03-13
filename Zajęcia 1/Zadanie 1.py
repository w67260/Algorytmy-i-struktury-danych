import math

a=int(input("Podaj a: "))
b=int(input("Podaj b: "))
c=int(input("Podaj c: "))
Delta=b*b-4*a*c
if Delta>0:
    x1=(-b-math.sqrt(Delta))/2*a
    x2=(-b+math.sqrt(Delta))/2*a
    print(f'x1={x1}, x2={x2}')
elif Delta==0:
    x = -b / 2 * a
    print(f'x={x}')
else:
    print("Brak miejsc zerowych")