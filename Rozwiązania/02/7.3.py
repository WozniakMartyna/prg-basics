# Program sprawdza, czy liczba wpisana przez użytkownika jest parzysta.

# Pobieramy liczbę od użytkownika.
# input() pobiera wartość jako tekst.
# int() zamienia tekst na liczbę całkowitą.
number = int(input('Enter number: '))

# Operator % oblicza resztę z dzielenia.
# Jeśli reszta z dzielenia przez 2 wynosi 0, liczba jest parzysta.
# Operator == sprawdza, czy dwie wartości są równe.
even = number % 2 == 0

# Wyświetlamy informację, czy liczba jest parzysta.
# F-string pozwala wstawić wartość zmiennej even do tekstu za pomocą {}.
print(f'Number is even: {even}')

# Sprawdzenie wymaganych liczb:
# 24 - liczba parzysta, even = True
# 8 - liczba parzysta, even = True
# 31 - liczba nieparzysta, even = False
# 5 - liczba nieparzysta, even = False