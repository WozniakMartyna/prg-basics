# ZADANIE: Zmodyfikuj wybrane elementy listy.
#
# Początkowa lista zawiera wartości: 1, 2, 3, 4, 5.
# Kolejno wykonujemy:
# 1. Odejmujemy 1 od pierwszego elementu.
# 2. Dodajemy 4 do ostatniego elementu.
# 3. Mnożymy środkowy element przez 2.
# Po każdej zmianie wyświetlamy całą listę.


# Tworzymy listę pięciu liczb całkowitych.
arr = [1, 2, 3, 4, 5]

# Wyświetlamy listę przed wprowadzeniem zmian.
print("Array:", arr)


# 1. Zmniejszamy pierwszy element o 1.
# arr[0] oznacza pierwszy element listy, czyli 1.
# arr[0] - 1 oblicza nową wartość: 1 - 1 = 0.
# Znak = przypisuje obliczoną wartość z powrotem do arr[0].
arr[0] = arr[0] - 1

# Wyświetlamy listę po pierwszej zmianie.
print("Array:", arr)


# 2. Zwiększamy ostatni element o 4.
# len(arr) zwraca 5, a len(arr) - 1 wskazuje indeks 4.
# arr[4] to ostatni element listy, czyli 5.
# Dodajemy do niego 4 i zapisujemy wynik w tej samej pozycji.
arr[len(arr) - 1] = arr[len(arr) - 1] + 4

# Wyświetlamy listę po drugiej zmianie.
print("Array:", arr)


# 3. Mnożymy środkowy element przez 2.
# len(arr) // 2 oblicza indeks środkowego elementu.
# Dla listy z 5 elementami jest to 5 // 2 = 2.
# arr[2] oznacza trzeci element listy, który obecnie ma wartość 3.
# Mnożymy go przez 2 i zapisujemy wynik w jego dotychczasowym miejscu.
arr[len(arr) // 2] = arr[len(arr) // 2] * 2

# Wyświetlamy listę po trzeciej zmianie.
print("Array:", arr)