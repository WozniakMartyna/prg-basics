# Program zamienia nieujemną liczbę dziesiętną na zapis binarny.
# Wykorzystuje dzielenie przez 2 i zapisywanie reszt z dzielenia.

# input() pobiera liczbę jako tekst, a int() zamienia ją na liczbę całkowitą.
number = int(input('Enter a non-negative integer: '))

# Zachowujemy pierwotną liczbę, ponieważ zmienna number
# będzie zmieniana podczas kolejnych obliczeń.
original_number = number

# Na początku wynik jest pustym tekstem.
binary = ''

# Szczególny przypadek: liczba 0 w systemie binarnym również wynosi 0.
if number == 0:
    binary = '0'

else:
    # while powtarza instrukcje tak długo, jak number jest większe od 0.
    while number > 0:

        # % oznacza resztę z dzielenia.
        # Reszta z dzielenia przez 2 będzie zawsze równa 0 albo 1.
        remainder = number % 2

        # str() zamienia resztę na tekst.
        # Dodajemy ją na początku wyniku, ponieważ kolejne reszty
        # otrzymujemy od prawej strony zapisu binarnego.
        binary = str(remainder) + binary

        # // oznacza dzielenie całkowite – odrzuca część po przecinku.
        # Dzięki temu w kolejnej iteracji dzielimy mniejszą liczbę.
        number = number // 2

# f-string pozwala wstawić wartości zmiennych do wyświetlanego tekstu.
# {original_number} to liczba dziesiętna, a {binary} to jej zapis binarny.
print(f'{original_number}(10) = {binary}(2)')