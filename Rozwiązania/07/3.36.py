# ZADANIE 3.36:
# Zamiana tablicy dwuwymiarowej na jednowymiarową.

# Tworzymy przykładowe tablice dwuwymiarowe.
array1 = [
    [1, 2, 3],
    [4, 5, 6]
]

array2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Funkcja zamienia tablicę 2D na listę 1D.
def flatten_array(array):

    # Tworzymy pustą listę wynikową.
    result = []

    # Przechodzimy przez wszystkie wiersze.
    for row in array:

        # Przechodzimy przez wszystkie elementy aktualnego wiersza.
        for number in row:

            # Dodajemy element do listy wynikowej.
            result.append(number)

    return result


# Zamieniamy obie tablice i wyświetlamy wyniki.
print("Pierwsza tablica:", flatten_array(array1))
print("Druga tablica:", flatten_array(array2))

# WYNIK:
# Pierwsza tablica: [1, 2, 3, 4, 5, 6]
# Druga tablica: [7, 8, 9, 10, 11, 12]
#
# NOTATKI:
# flatten_array() - funkcja spłaszcza tablicę dwuwymiarową.
# Pętla zewnętrzna przechodzi przez wiersze.
# Pętla wewnętrzna przechodzi przez elementy danego wiersza.
# append() - dodaje element do listy wynikowej.
# Kolejność elementów zostaje zachowana.