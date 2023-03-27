def hanoi(n, A, B, C):
    if n == 1:
        print(f"Przenieś krążek z patyka {A} na patyk {B}.")
    else:
        hanoi(n-1, A, C, B)
        print(f"Przenieś największy krążek z patyka {A} na patyk {B}.")
        hanoi(n-1, C, B, A)

hanoi(3, 'A', 'B', 'C')