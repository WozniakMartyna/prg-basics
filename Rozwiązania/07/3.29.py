# ZADANIE 3.29:
# Funkcja tworząca tablicę 2D wypełnioną zerami.

# Funkcja przyjmuje dwa argumenty:
# x - liczba wierszy, y - liczba kolumn.
def create_2d_arr(x, y):

    # Tworzymy pustą listę, do której dodamy wiersze.
    array = []

    # Pętla wykonuje się x razy, czyli tworzy x wierszy.
    for i in range(x):

        # Tworzymy jeden wiersz składający się z y zer.
        row = [0] * y

        # Dodajemy gotowy wiersz do tablicy.
        array.append(row)

    # Zwracamy utworzoną tablicę.
    return array


# Tworzymy tablicę mającą 3 wiersze i 5 kolumn.
result = create_2d_arr(3, 5)

# Wyświetlamy każdy wiersz.
for row in result:
    print(row)

# WYNIK:
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
#
# NOTATKI:
# [0] * y - tworzy listę zawierającą y zer.
# append() - dodaje element na końcu listy.
# return - zwraca wynik działania funkcji.
# create_2d_arr(3, 5) - tworzy 3 wiersze i 5 kolumn.