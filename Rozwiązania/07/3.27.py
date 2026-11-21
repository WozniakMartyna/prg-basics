# ZADANIE 3.27:
# Utworzenie i wyświetlenie tablicy dwuwymiarowej 2 x 4.

# Tworzymy listę zawierającą dwa wiersze.
# Każdy wiersz ma po cztery elementy.
array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

# Pętla zewnętrzna przechodzi przez kolejne wiersze.
for row in array:

    # Wyświetlamy cały aktualny wiersz.
    print(row)

# Możemy też wyświetlić każdy element osobno.
print("Elementy pojedynczo:")

for i in range(len(array)):  # Indeks kolejnego wiersza.
    for j in range(len(array[i])):  # Indeks kolumny w tym wierszu.
        print(array[i][j], end=" ")

    print()  # Przechodzimy do nowej linii po każdym wierszu.

# WYNIK:
# [1, 2, 3, 4]
# [5, 6, 7, 8]
#
# Elementy pojedynczo:
# 1 2 3 4
# 5 6 7 8
#
# NOTATKI:
# array[i][j] - pobiera element z wiersza i i kolumny j.
# len(array) - zwraca liczbę wierszy.
# len(array[i]) - zwraca liczbę elementów w wybranym wierszu.
# end=" " - powoduje, że print() nie przechodzi od razu do nowej linii.