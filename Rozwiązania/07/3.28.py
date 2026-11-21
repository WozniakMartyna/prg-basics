# ZADANIE 3.28:
# Obliczenie sumy elementów ostatniej kolumny tablicy 2D.

# Tworzymy tablicę podaną w poleceniu.
array = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

# Zmienna przechowuje obliczaną sumę.
total = 0

# Przechodzimy przez wszystkie wiersze.
for i in range(len(array)):

    # -1 oznacza ostatni element wiersza.
    total += array[i][-1]

# Wyświetlamy wynik.
print("Suma ostatniej kolumny:", total)

# WYNIK:
# Suma ostatniej kolumny: 17
#
# NOTATKI:
# array[i] - oznacza cały wiersz o indeksie i.
# array[i][-1] - oznacza ostatni element tego wiersza.
# total += ... - dodaje wartość do aktualnej sumy.
# Indeksy w Pythonie zaczynają się od 0.