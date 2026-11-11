# Program losuje wynik rzutu kostką i sprawdza, czy wylosowana liczba to 1 lub 6.

# Importujemy moduł random, który umożliwia losowanie.
import random

# Losujemy liczbę całkowitą od 1 do 6.
# randint(1, 6) losuje liczbę całkowitą od 1 do 6.
# random.randint() oznacza wywołanie funkcji randint() znajdującej się w module random.
dice_roll = random.randint(1, 6)

# Sprawdzamy, czy wynik rzutu jest równy 1 LUB 6.
# == sprawdza równość.
# or oznacza "lub" – wystarczy jeden prawdziwy warunek.
special_number = dice_roll == 1 or dice_roll == 6

# Wyświetlamy wylosowaną liczbę.
print(f'Dice rolled: {dice_roll}')

# Wyświetlamy informację, czy wylosowano liczbę specjalną.
# F-string pozwala wstawić wartość zmiennej do tekstu za pomocą {}.
print(f'Special number (1 or 6): {special_number}')