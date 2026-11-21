# ZADANIE:
# Zmiana wartości na głównej przekątnej macierzy na 1.
# Na początku wszystkie elementy macierzy mają wartość 0.

# Tworzymy macierz 3x3, czyli 3 wiersze i 3 kolumny.
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Pętla przechodzi po indeksach od 0 do 2.
# range(3) generuje liczby: 0, 1, 2.
for i in range(3):

    # Ustawiamy wartość 1 na głównej przekątnej.
    # matrix[i][i] oznacza element, którego indeks wiersza
    # i indeks kolumny są takie same.
    #
    # i = 0 -> matrix[0][0] (pierwszy wiersz, pierwsza kolumna)
    # i = 1 -> matrix[1][1] (drugi wiersz, druga kolumna)
    # i = 2 -> matrix[2][2] (trzeci wiersz, trzecia kolumna)
    matrix[i][i] = 1


# Wyświetlamy zmodyfikowaną macierz.
# Pętla zewnętrzna przechodzi po wierszach.
for row in matrix:

    # Pętla wewnętrzna wyświetla elementy danego wiersza.
    for element in row:

        # end=" " pozostawia kursor w tej samej linii
        # i oddziela liczby spacjami.
        print(element, end=" ")

    # Przechodzimy do następnej linii po wydrukowaniu wiersza.
    print()