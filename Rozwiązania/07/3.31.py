# ZADANIE 3.31:
# Znalezienie minimum i maksimum oraz ich położenia w tablicy 2D.

# Tworzymy tablicę z polecenia.
array = [
    [-38, 19],
    [5, 40],
    [-7, 11],
    [29, 16]
]

# Na początku przyjmujemy, że pierwszy element jest
# jednocześnie najmniejszym i największym elementem.
minimum = array[0][0]
maximum = array[0][0]

# Zapamiętujemy położenie minimum i maksimum.
min_row = 0
min_col = 0
max_row = 0
max_col = 0

# Przechodzimy przez wszystkie wiersze.
for i in range(len(array)):

    # Przechodzimy przez wszystkie kolumny aktualnego wiersza.
    for j in range(len(array[i])):

        # Pobieramy aktualny element.
        number = array[i][j]

        # Sprawdzamy, czy znaleźliśmy nową najmniejszą wartość.
        if number < minimum:
            minimum = number
            min_row = i
            min_col = j

        # Sprawdzamy, czy znaleźliśmy nową największą wartość.
        if number > maximum:
            maximum = number
            max_row = i
            max_col = j

# Wyświetlamy wyniki.
# Dodajemy 1 do indeksów, aby podać numery wierszy i kolumn
# w sposób bardziej naturalny dla użytkownika (od 1).
print("Minimum:", minimum)
print("Położenie minimum: wiersz", min_row + 1, "kolumna", min_col + 1)

print("Maksimum:", maximum)
print("Położenie maksimum: wiersz", max_row + 1, "kolumna", max_col + 1)

# WYNIK:
# Minimum: -38
# Położenie minimum: wiersz 1 kolumna 1
# Maksimum: 40
# Położenie maksimum: wiersz 2 kolumna 2
#
# NOTATKI:
# array[i][j] - pobiera element z konkretnego wiersza i kolumny.
# min_row i min_col - przechowują położenie minimum.
# max_row i max_col - przechowują położenie maksimum.
# Indeksy tablicy zaczynają się od 0, dlatego dodajemy 1 przy wyświetlaniu.