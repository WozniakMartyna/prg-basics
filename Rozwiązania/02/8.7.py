# Program pobiera liczbę całkowitą i wyświetla ją w systemie binarnym oraz szesnastkowym.
# 
# Czym są systemy liczbowe?
# System dziesiętny – używamy go na co dzień. Ma 10 cyfr: od 0 do 9.
# System binarny – używa tylko dwóch cyfr: 0 i 1.
# System szesnastkowy – używa cyfr od 0 do 9 oraz liter od A do F.
# 
# W Pythonie możemy użyć gotowych funkcji:
# bin() – zamienia liczbę na zapis binarny.
# hex() – zamienia liczbę na zapis szesnastkowy.

# Pobieramy liczbę od użytkownika.
# input() pobiera wpisaną wartość jako tekst.
# int() zamienia tekst na liczbę całkowitą.
number = int(input('Enter number: '))

# Zamieniamy liczbę na system binarny.
# bin() zwraca zapis liczby w systemie binarnym.
# Przed wynikiem pojawia się oznaczenie 0b.
binary_number = bin(number)

# Zamieniamy liczbę na system szesnastkowy.
# hex() zwraca zapis liczby w systemie szesnastkowym.
# Przed wynikiem pojawia się oznaczenie 0x.
hexadecimal_number = hex(number)

# Wyświetlamy liczbę w systemie binarnym.
# F-string pozwala wstawiać wartości zmiennych do tekstu za pomocą {}.
print(f'Binary number: {binary_number}')

# Wyświetlamy liczbę w systemie szesnastkowym.
print(f'Hexadecimal number: {hexadecimal_number}')