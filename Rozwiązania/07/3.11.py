# ZADANIE 11: Sortowanie listy za pomocą algorytmu Bubble Sort.

# Definiujemy funkcję sortującą listę rosnąco.
def bubblesort(array):

    # Tworzymy kopię listy, żeby nie zmieniać oryginalnej listy przekazanej do funkcji.
    result = array.copy()

    # len(result) zwraca liczbę elementów listy.
    # Każde przejście pętli zewnętrznej umieszcza kolejną największą
    # wartość na właściwym miejscu.
    for i in range(len(result)):

        # Flaga informuje, czy podczas przejścia wykonaliśmy zamianę.
        swapped = False

        # Porównujemy sąsiednie elementy.
        # Odejmujemy i + 1, ponieważ na końcu listy elementy są już posortowane.
        for j in range(len(result) - i - 1):

            # Jeżeli lewy element jest większy od prawego,
            # zamieniamy je miejscami.
            if result[j] > result[j + 1]:

                # Python pozwala zamienić wartości bez dodatkowej zmiennej.
                result[j], result[j + 1] = result[j + 1], result[j]

                # Zapisujemy informację, że wykonaliśmy zamianę.
                swapped = True

        # Jeżeli nie było żadnej zamiany, lista jest już posortowana.
        # Nie ma potrzeby wykonywania kolejnych przejść.
        if not swapped:
            break

    # Zwracamy posortowaną kopię listy.
    return result


# Przygotowujemy trzy przykładowe listy.
numbers1 = [5, 2, 8, 1, 9]
numbers2 = [12, 4, 7, 3, 10, 1]
numbers3 = [20, 15, 10, 5, 0]

# Wywołujemy funkcję i wyświetlamy wyniki.
print("Lista 1:", bubblesort(numbers1))
print("Lista 2:", bubblesort(numbers2))
print("Lista 3:", bubblesort(numbers3))

# Sprawdzamy, czy oryginalna lista pozostała bez zmian.
print("Oryginalna lista 1:", numbers1)

# DODATKOWE NOTATKI:
#
# Bubble Sort (sortowanie bąbelkowe) - algorytm sortowania,
# który porównuje sąsiednie elementy i zamienia je miejscami,
# jeżeli są w złej kolejności.
#
# copy() - tworzy kopię listy.
# Dzięki temu oryginalna lista nie zostaje zmieniona.
#
# Dwie pętle:
# - zewnętrzna odpowiada za kolejne przejścia po liście,
# - wewnętrzna porównuje sąsiednie elementy.
#
# result[j] - element znajdujący się pod indeksem j.
# result[j + 1] - element znajdujący się bezpośrednio za nim.
#
# Zamiana:
# result[j], result[j + 1] = result[j + 1], result[j]
# Pozwala zamienić dwa elementy miejscami bez dodatkowej zmiennej.
#
# swapped - zmienna typu bool (True lub False).
# Informuje, czy podczas przejścia wykonano zamianę.
#
# break - przerywa działanie pętli.
# Jeżeli nie było żadnej zamiany, lista jest już posortowana.
#
# range(len(result) - i - 1):
# Ograniczamy zakres, ponieważ po każdym przejściu
# największy z nieposortowanych elementów trafia na koniec.
#
# Sortowanie rosnące oznacza kolejność od najmniejszej
# do największej wartości.