# ZADANIE 9: Porównywanie dwóch list.

# Definiujemy funkcję przyjmującą dwie listy.
def compare(array1, array2):

    # Najpierw sprawdzamy, czy obie listy mają taką samą długość.
    # Jeżeli długości są różne, listy nie mogą być identyczne.
    if len(array1) != len(array2):
        return False

    # Przechodzimy po indeksach pierwszej listy.
    for i in range(len(array1)):

        # Porównujemy elementy znajdujące się na tych samych pozycjach.
        if array1[i] != array2[i]:

            # Jeśli choć jeden element jest inny, zwracamy False.
            return False

    # Jeżeli nie znaleźliśmy różnic, listy są identyczne.
    return True


# Przygotowujemy cztery pary list z polecenia.
array1 = ["water", "book", "sky"]
array2 = ["water", "book", "sky"]

array3 = [True, False]
array4 = [True, False, True]

array5 = [5, 3, 1]
array6 = [5, 3, 1]

array7 = [3, 2, 1]
array8 = [3, 2]

# Wywołujemy funkcję dla każdej pary i wyświetlamy wyniki.
print(compare(array1, array2))
print(compare(array3, array4))
print(compare(array5, array6))
print(compare(array7, array8))

# DODATKOWE NOTATKI:
#
# len(array1) - zwraca liczbę elementów pierwszej listy.
#
# != oznacza "różne od".
# == oznacza "równe".
#
# return False - kończy funkcję i zwraca informację,
# że listy nie są identyczne.
#
# return True - zwraca informację, że listy są identyczne.
#
# Dlaczego najpierw porównujemy długości?
# Listy o różnej liczbie elementów nie mogą być identyczne.
#
# Funkcja porównuje również kolejność elementów.
# [1, 2, 3] i [3, 2, 1] nie są identyczne.