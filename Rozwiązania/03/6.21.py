# Program oblicza, ile monet o nominałach 5, 2 i 1 zł potrzeba, aby wydać podaną kwotę.

# input() pobiera dane od użytkownika jako tekst.
# int() zamienia ten tekst na liczbę całkowitą.
amount = int(input('Enter the amount to give back: '))

# Operator // oznacza dzielenie całkowite.
# Obliczamy, ile monet 5 zł można wydać.
coins_5 = amount // 5

# Operator % oznacza resztę z dzielenia.
# Obliczamy, ile pieniędzy zostanie po wydaniu monet 5 zł.
amount = amount % 5

# Obliczamy liczbę monet 2 zł z pozostałej kwoty.
coins_2 = amount // 2

# Obliczamy, ile pieniędzy zostanie po wydaniu monet 2 zł.
amount = amount % 2

# Pozostała kwota to liczba potrzebnych monet 1 zł.
coins_1 = amount

# f-string to sposób tworzenia tekstu z wartościami zmiennych.
# Wartość zmiennej umieszczamy w nawiasach klamrowych {}.
# Dzięki temu zamiast nazwy zmiennej wyświetli się jej wartość.
print(f'5 PLN coins: {coins_5}')

# Tutaj f-string wstawia wartość zmiennej coins_2 do tekstu.
print(f'2 PLN coins: {coins_2}')

# Tutaj f-string wstawia wartość zmiennej coins_1 do tekstu.
print(f'1 PLN coins: {coins_1}')