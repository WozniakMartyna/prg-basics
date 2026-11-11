# Liczba parzysta dzieli się przez 2 bez reszty. Operator % oblicza resztę z dzielenia.
# Program sprawdza, czy podana liczba jest parzysta, czy nieparzysta.

# input() pobiera liczbę od użytkownika jako tekst.
# int() zamienia tekst na liczbę całkowitą.
number = int(input('Enter number: '))

# Operator % oblicza resztę z dzielenia.
# == sprawdza, czy reszta z dzielenia przez 2 wynosi 0.
# Jeśli reszta z dzielenia przez 2 wynosi 0, liczba jest parzysta.
if number % 2 == 0:
    # f-string pozwala wstawić wartość zmiennej number do tekstu za pomocą {}.
    print(f'{number} is even')
else:
    # Ten komunikat pojawia się, gdy liczba nie jest parzysta.
    print(f'{number} is odd')