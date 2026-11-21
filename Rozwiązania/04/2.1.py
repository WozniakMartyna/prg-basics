
# Program for testing built-in functions
# Funkcje wbudowane to funkcje Pythona, których nie trzeba importować.

# max() zwraca największą wartość z podanych argumentów.
max_number = max(7, 5, 6, 3, 8, 2)
print('Max number of 7,5,6,3,8,2 is', max_number)

# min() zwraca najmniejszą wartość z podanych argumentów.
min_number = min(4, 7, 2, 3, 9, 8)
print('Min number of 4,7,2,3,9,8 is', min_number)

# len() zwraca długość tekstu, czyli liczbę znaków.
str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

# input() pobiera tekst wpisany przez użytkownika z klawiatury.
letter = input('Enter a letter: ')
print('The entered letter is', letter)

# int() zamienia tekst na liczbę całkowitą.
# "20303" jest tekstem, dlatego używamy int(), aby otrzymać liczbę.
number = int("20303")
print('The number is', number)

# bin() zamienia liczbę dziesiętną na tekstowy zapis binarny.
# Zapis binarny składa się z cyfr 0 i 1.
binary_number = bin(304)
print('Binary representation of 304 is', binary_number)

# hex() zamienia liczbę dziesiętną na tekstowy zapis szesnastkowy.
hex_number = hex(304)
print('Hexadecimal representation of 304 is', hex_number)

# ord() zwraca liczbę Unicode odpowiadającą podanemu znakowi.
euro_code = ord('€')
print('Unicode code of € is', euro_code)

# abs() zwraca wartość bezwzględną, czyli odległość liczby od zera.
absolute_number = abs(-17)
print('Absolute value of -17 is', absolute_number)


# max() - największa wartość.
# Można ją zastąpić np. ręcznym porównywaniem liczb instrukcją if.
#
# min() - najmniejsza wartość.
# Można ją zastąpić np. ręcznym porównywaniem liczb instrukcją if.
#
# len() - liczba znaków w tekście.
# Można policzyć znaki pętlą i własnym licznikiem.
#
# int() - zamienia wartość na liczbę całkowitą.
# float() - zamienia wartość na liczbę zmiennoprzecinkową.
#
# bin() - zamienia liczbę na zapis binarny.
# hex() - zamienia liczbę na zapis szesnastkowy.
#
# ord() - zamienia pojedynczy znak na jego kod Unicode.
# chr() - działa odwrotnie: zamienia kod Unicode na znak.
#
# abs() - zwraca wartość bezwzględną liczby.