# Komputer losuje liczbę od 1 do 6. Użytkownik próbuje odgadnąć wylosowany wynik. Program sprawdza, czy odpowiedź jest prawidłowa.

# Program pozwala użytkownikowi zgadywać wynik rzutu kostką.

# Importujemy moduł random, który umożliwia losowanie liczb.
import random

# RUCH KOMPUTERA
# Komputer losuje liczbę całkowitą od 1 do 6.
# randint(1, 6) losuje liczbę całkowitą od 1 do 6.
# random.randint() oznacza wywołanie funkcji randint() znajdującej się w module random.
# random.randint(1, 6) zwraca jedną losową liczbę z tego zakresu.
computer = random.randint(1, 6)

# RUCH UŻYTKOWNIKA
# Pobieramy liczbę wpisaną przez użytkownika.
# input() pobiera odpowiedź jako tekst.
# int() zamienia tekst na liczbę całkowitą.
you = int(input('Guess the dice number (1-6): '))

# Porównujemy liczbę użytkownika z liczbą komputera.
# Operator == sprawdza, czy obie liczby są równe.
# Wynikiem porównania jest True albo False.
you_won = you == computer

# Wyświetlamy liczbę wylosowaną przez komputer.
print(f'Computer rolled: {computer}')

# Wyświetlamy informację, czy użytkownik odgadł liczbę.
# F-string pozwala wstawić wartość zmiennej you_won do tekstu za pomocą {}.
print(f'You won: {you_won}')