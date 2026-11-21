# ZADANIE 3.33:
# Zamiana pierwszej i ostatniej kolumny tablicy 2D.

# Tworzymy tablicę o 3 wierszach i 5 kolumnach.
array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

# Wyświetlamy tablicę przed zamianą.
print("Tablica przed zamianą:")

for row in array:
    print(row)

# Przechodzimy przez wszystkie wiersze.
for i in range(len(array)):

    # Zamieniamy pierwszy element wiersza z ostatnim.
    # Indeks 0 oznacza pierwszą kolumnę, a -1 ostatnią.
    array[i][0], array[i][-1] = array[i][-1], array[i][0]

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
# [5, 2, 3, 4, 1]
# [10, 7, 8, 9, 6]
# [15, 12, 13, 14, 11]
#
# NOTATKI:
# array[i][0] - pierwszy element aktualnego wiersza.
# array[i][-1] - ostatni element aktualnego wiersza.
# len(array) - liczba wierszy tablicy.
# Zamiana odbywa się osobno w każdym wierszu.