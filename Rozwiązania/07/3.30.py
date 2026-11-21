# ZADANIE 3.30:
# Utworzenie tabliczki mnożenia 5 x 5.

# Tworzymy pustą tablicę.
table = []

# Pętla zewnętrzna odpowiada za kolejne wiersze.
for i in range(1, 6):

    # Tworzymy pusty wiersz.
    row = []

    # Pętla wewnętrzna odpowiada za kolejne kolumny.
    for j in range(1, 6):

        # Mnożymy numer wiersza przez numer kolumny.
        row.append(i * j)

    # Dodajemy wypełniony wiersz do tablicy.
    table.append(row)

# Wyświetlamy tabliczkę mnożenia.
for row in table:

    # Każdy element wyświetlamy w polu o szerokości 4 znaków.
    # Dzięki temu liczby są równo ustawione.
    for number in row:
        print(f"{number:4}", end="")

    print()  # Nowy wiersz po wyświetleniu całego rzędu.

# WYNIK:
#    1   2   3   4   5
#    2   4   6   8  10
#    3   6   9  12  15
#    4   8  12  16  20
#    5  10  15  20  25
#
# NOTATKI:
# range(1, 6) - generuje liczby od 1 do 5.
# i * j - oblicza iloczyn numeru wiersza i kolumny.
# f"{number:4}" - wyświetla liczbę w polu szerokości 4 znaków.
# Dwie pętle for pozwalają przejść przez wiersze i kolumny.