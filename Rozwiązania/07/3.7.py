# ZADANIE 7: Znalezienie najdłuższego imienia na liście.

# Tworzymy listę imion.
names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

# Na początku zakładamy, że najdłuższe jest pierwsze imię.
longest_name = names[0]

# Przechodzimy przez wszystkie imiona na liście.
for name in names:

    # len(name) zwraca liczbę znaków w imieniu.
    # Jeżeli aktualne imię jest dłuższe od zapisanego,
    # zapisujemy je jako nowe najdłuższe imię.
    if len(name) > len(longest_name):
        longest_name = name

# Wyświetlamy najdłuższe imię i liczbę jego znaków.
print("Najdłuższe imię:", longest_name)
print("Liczba znaków:", len(longest_name))

# DODATKOWE NOTATKI:
#
# len() - zwraca liczbę znaków w tekście lub liczbę elementów listy.
# Przykład: len("Alojzy") zwróci 6.
#
# Możemy porównywać długości tekstów za pomocą operatorów:
# > oznacza większy niż,
# < oznacza mniejszy niż,
# == oznacza równy.
#
# Jeżeli dwa imiona mają taką samą długość, nasz program
# pozostawi pierwsze znalezione imię.