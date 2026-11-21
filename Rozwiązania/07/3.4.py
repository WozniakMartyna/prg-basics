# ZADANIE 4: Znajdowanie najmniejszej i największej liczby bez min() i max().

# Tworzymy listę liczb.
numbers = [-15, 8, -31, 47, -2, 19]

# Na początku zakładamy, że pierwszy element jest najmniejszy.
minimum = numbers[0]

# Na początku zakładamy, że pierwszy element jest największy.
maximum = numbers[0]

# Przechodzimy przez wszystkie elementy listy.
for number in numbers:

    # Jeżeli aktualna liczba jest mniejsza od minimum,
    # zapisujemy ją jako nowe minimum.
    if number < minimum:
        minimum = number

    # Jeżeli aktualna liczba jest większa od maximum,
    # zapisujemy ją jako nowe maksimum.
    if number > maximum:
        maximum = number

# Wyświetlamy znalezione wartości.
print("Najmniejsza liczba:", minimum)
print("Największa liczba:", maximum)