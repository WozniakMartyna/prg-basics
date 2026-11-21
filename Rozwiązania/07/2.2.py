# ZADANIE:
# Wyświetlenie planszy do gry w kółko i krzyżyk.
# Plansza składa się z 3 wierszy i 3 kolumn.

# Tworzymy listę dwuwymiarową.
# Każda lista wewnętrzna reprezentuje jeden wiersz planszy.
tic_tac_toe_board = [
    ['X', 'O', 'X'],
    [' ', 'X', 'O'],
    ['O', ' ', 'X']
]

# Pętla zewnętrzna przechodzi po kolejnych wierszach planszy.
# Zmienna row przechowuje aktualny wiersz, czyli jedną listę.
for row in tic_tac_toe_board:

    # Pętla wewnętrzna przechodzi po elementach aktualnego wiersza.
    # Zmienna symbol przechowuje jeden znak: X, O lub spację.
    for symbol in row:

        # end=" " oznacza, że po wydrukowaniu znaku
        # Python nie przechodzi do następnej linii.
        # Zamiast tego dodaje spację.
        print(symbol, end=" ")

    # Ten print() wykonuje się po zakończeniu pętli wewnętrznej.
    # Przechodzi do nowej linii, aby kolejny wiersz planszy
    # został wyświetlony pod poprzednim.
    print()