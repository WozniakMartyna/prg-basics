# ZADANIE 3: Podnoszenie każdego elementu listy do kwadratu.

# Tworzymy listę liczb.
numbers = [8, 2, 5, 1, 9]

# Tworzymy pustą listę na wyniki.
squared_numbers = []

# Pętla for przechodzi kolejno przez wszystkie elementy listy.
for number in numbers:

    # ** oznacza potęgowanie.
    # number ** 2 podnosi aktualną liczbę do kwadratu.
    squared_numbers.append(number ** 2)

# Wyświetlamy listę wynikową.
print("Lista początkowa:", numbers)
print("Elementy podniesione do kwadratu:", squared_numbers)