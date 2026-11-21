# ZADANIE 3.35:
# Transponowanie macierzy, czyli zamiana wierszy na kolumny.

# Funkcja przyjmuje macierz i zwraca jej transpozycję.
def transpose_matrix(m):

    # Liczba wierszy w oryginalnej macierzy.
    rows = len(m)

    # Liczba kolumn w oryginalnej macierzy.
    columns = len(m[0])

    # Tworzymy pustą macierz wynikową.
    # Po transpozycji liczba wierszy i kolumn się zamienia.
    result = []

    # Każda kolumna oryginalnej macierzy stanie się wierszem.
    for j in range(columns):

        # Tworzymy nowy wiersz macierzy wynikowej.
        row = []

        # Pobieramy elementy z kolejnych wierszy oryginału.
        for i in range(rows):
            row.append(m[i][j])

        # Dodajemy nowy wiersz do macierzy wynikowej.
        result.append(row)

    return result


# Funkcja wyświetla macierz.
def print_matrix(matrix):

    for row in matrix:
        print(row)


# Pierwsza macierz: 3 x 3.
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Druga macierz: 2 x 5.
matrix2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

# Trzecia macierz: 1 x 4.
matrix3 = [
    [5, 6, 7, 8]
]

# Testujemy funkcję na każdej macierzy.
print("Macierz 3 x 3 po transpozycji:")
print_matrix(transpose_matrix(matrix1))

print("\nMacierz 2 x 5 po transpozycji:")
print_matrix(transpose_matrix(matrix2))

print("\nMacierz 1 x 4 po transpozycji:")
print_matrix(transpose_matrix(matrix3))


# WYNIK:
# Macierz 3 x 3:
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]
#
# Macierz 2 x 5:
# [1, 6]
# [2, 7]
# [3, 8]
# [4, 9]
# [5, 0]
#
# Macierz 1 x 4:
# [5]
# [6]
# [7]
# [8]
#
# NOTATKI:
# Transpozycja zamienia wiersze na kolumny.
# len(m) - liczba wierszy.
# len(m[0]) - liczba kolumn w pierwszym wierszu.
# m[i][j] - element z wiersza i i kolumny j.
# Po transpozycji macierz 2 x 5 staje się macierzą 5 x 2.