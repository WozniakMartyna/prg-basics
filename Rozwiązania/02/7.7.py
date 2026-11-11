# Program losuje jedną liczbę całkowitą z zakresu od 5 do 10.

# Importujemy moduł random, który umożliwia losowanie.
import random

# Funkcja randint(5, 10) losuje liczbę całkowitą od 5 do 10, włącznie z obiema granicami.
# random.randint() oznacza wywołanie funkcji randint() znajdującej się w module random.
random_number = random.randint(5, 10)

# Wyświetlamy wylosowaną liczbę.
# print() pokazuje wartość zmiennej na ekranie.
print(random_number)