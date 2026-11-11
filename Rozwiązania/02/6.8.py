# Program ma pobrać dwie litery i obliczyć, ile liter alfabetu znajduje się pomiędzy nimi.

# Pobieramy pierwszą literę od użytkownika.
# input() pobiera odpowiedź jako tekst.
first = input('Enter first letter: ')

# Pobieramy drugą literę od użytkownika.
last = input('Enter last letter: ')

# Funkcja ord() zamienia pierwszą literę na jej kod liczbowy.
first_letter_code = ord(first)

# Funkcja ord() zamienia drugą literę na jej kod liczbowy.
last_letter_code = ord(last)

# Obliczamy różnicę pomiędzy kodami liter.
# Funkcja abs() zwraca wartość bezwzględną, czyli dodatnią różnicę.
difference = abs(last_letter_code - first_letter_code)

# Odejmujemy 1, ponieważ nie liczymy liter początkowej i końcowej, tylko litery pomiędy nimi.
number_of_letters = difference - 1

# Jeśli litery są takie same lub są obok siebie, liczba liter pomiędzy nimi nie może być ujemna.
# max() wybiera większą z dwóch wartości: 0 lub obliczony wynik.
number_of_letters = max(0, number_of_letters)

# Wyświetlamy wynik.
# F-string pozwala wstawić wartości zmiennych do tekstu za pomocą {}.
print(f'Between {first} and {last} is {number_of_letters} letters')

# Sprawdzamy działanie programu dla przykładowych liter:
# A ma kod 65, D ma kod 68. Różnica wynosi 3. Odejmujemy 1, więc otrzymujemy 2 litery: B i C.
# B ma kod 66, M ma kod 77. Różnica wynosi 11. Odejmujemy 1, więc otrzymujemy 10 liter.
# K i K mają ten sam kod. Różnica wynosi 0, więc wynik to 0.