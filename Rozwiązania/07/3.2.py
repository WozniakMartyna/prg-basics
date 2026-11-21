# ZADANIE 2: Odwracanie kolejności elementów listy.

# Tworzymy listę z podanymi liczbami.
numbers = [15, 8, 31, 47, 2, 19]

# Tworzymy pustą listę, do której wpiszemy elementy w odwrotnej kolejności.
reversed_numbers = []

# len(numbers) zwraca liczbę elementów listy.
# Odejmujemy 1, ponieważ indeksy zaczynają się od 0.
i = len(numbers) - 1

# Pętla działa, dopóki indeks jest większy lub równy 0.
while i >= 0:

    # Dodajemy do nowej listy element o aktualnym indeksie.
    reversed_numbers.append(numbers[i])

    # Zmniejszamy indeks o 1, czyli cofamy się do poprzedniego elementu.
    i -= 1

# Wyświetlamy obie listy.
print("Lista początkowa:", numbers)
print("Lista odwrócona:", reversed_numbers)