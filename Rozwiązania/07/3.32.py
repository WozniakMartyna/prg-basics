# ZADANIE 3.32:
# Zamiana pierwszego i ostatniego wiersza tablicy 2D.

# Tworzymy przykładową tablicę 3 x 5.
array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

# Wyświetlamy tablicę przed zamianą.
print("Tablica przed zamianą:")

for row in array:
    print(row)

# Zamieniamy pierwszy i ostatni wiersz.
# Indeks 0 oznacza pierwszy wiersz, a -1 ostatni.
array[0], array[-1] = array[-1], array[0]

# Wyświetlamy tablicę po zamianie.
print("\nTablica po zamianie:")

for row in array:
    print(row)

# WYNIK:
# Tablica przed zamianą:
# [1, 2, 3, 4, 5]
# [6, 7, 8, 9, 10]
# [11, 12, 13, 14, 15]
#
# Tablica po zamianie:
# [11, 12, 13, 14, 15]
# [6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5]
#
# NOTATKI:
# array[0] - pierwszy wiersz tablicy.
# array[-1] - ostatni wiersz tablicy.
# a, b = b, a - zamienia wartości dwóch zmiennych miejscami.
# \n - znak nowej linii w tekście.