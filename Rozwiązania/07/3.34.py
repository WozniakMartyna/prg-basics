# ZADANIE 3.34:
# Tworzenie i wyświetlanie macierzy jednostkowej.

# Funkcja tworzy macierz jednostkową o wymiarach n x n.
def identity_matrix(n):

    # Tworzymy pustą macierz.
    matrix = []

    # Przechodzimy przez kolejne wiersze.
    for i in range(n):

        # Tworzymy pusty wiersz.
        row = []

        # Przechodzimy przez kolejne kolumny.
        for j in range(n):

            # Na przekątnej głównej (i == j) wpisujemy 1.
            # W pozostałych miejscach wpisujemy 0.
            if i == j:
                row.append(1)
            else:
                row.append(0)

        # Dodajemy gotowy wiersz do macierzy.
        matrix.append(row)

    return matrix


# Funkcja wyświetla macierz w czytelnej postaci.
def print_matrix(matrix):

    for row in matrix:
        for number in row:
            print(number, end=" ")
        print()  # Po każdym wierszu przechodzimy do nowej linii.


# Testujemy funkcję dla trzech rozmiarów.
for size in [3, 5, 8]:

    print("\nMacierz jednostkowa", size, "x", size)

    # Tworzymy macierz i przekazujemy ją do funkcji wyświetlającej.
    result = identity_matrix(size)
    print_matrix(result)


# PRZYKŁADOWY WYNIK DLA 3 x 3:
# 1 0 0
# 0 1 0
# 0 0 1
#
# NOTATKI:
# Macierz jednostkowa ma jedynki na przekątnej głównej,
# a pozostałe elementy są równe zero.
# i == j - sprawdza, czy numer wiersza jest równy numerowi kolumny.
# print_matrix(matrix) - funkcja otrzymuje macierz jako argument.
# end=" " - wyświetla elementy w tym samym wierszu.