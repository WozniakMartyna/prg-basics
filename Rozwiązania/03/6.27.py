# W instrukcji podano gotowy kod, który wyświetla:
# 7 8 9
# 4 5 6
# 1 2 3

# Wyświetlanie układu klawiatury numerycznej
# Zamiana pętli for na pętlę while

i = 6  # Początkowa wartość zmiennej i

while i >= 0:  # Pętla działa, dopóki i jest większe lub równe 0
    j = 1  # Na początku każdego wiersza ustawiamy j na 1

    while j <= 3:  # Pętla wykonuje się dla wartości j: 1, 2 i 3
        # f przed tekstem oznacza f-string.
        # Wartość działania i+j zostanie wstawiona w miejsce {}.
        # end=' ' oznacza, że liczby będą w jednym wierszu, oddzielone spacją.
        print(f'{i+j}', end=' ')

        j += 1  # Zwiększamy j o 1

    print()  # Przechodzimy do nowego wiersza
    i -= 3  # Zmniejszamy i o 3