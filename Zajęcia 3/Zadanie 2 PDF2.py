def reverse_array(tablica):
    if len(tablica) == 0 or len(tablica) == 1:
        return tablica
    else:
        return [tablica[-1]] + reverse_array(tablica[:-1])

tablica = [1, 2, 3, 4, 5]
print(reverse_array(tablica))