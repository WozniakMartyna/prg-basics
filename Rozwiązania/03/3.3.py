# Zniżka przysługuje:
# dzieciom poniżej 18 lat,
# osobom, które mają 65 lat lub więcej.

# Program sprawdza, czy dana osoba ma prawo do zniżki.

# input() pobiera wiek jako tekst.
# int() zamienia tekst na liczbę całkowitą.
age = int(input('Enter your age: '))

# Operator < oznacza "mniejsze niż".
# Operator >= oznacza "większe lub równe".
# Operator or oznacza "lub" – wystarczy spełnienie jednego warunku.
if age < 18 or age >= 65:
    # if wykonuje kod, jeśli osoba kwalifikuje się do zniżki.
    print('Discount available')
else:
    # else wykonuje się, jeśli żaden z dwóch warunków nie jest prawdziwy.
    print('Discount not available')

# Sprawdzenie podanych wartości:
# Wiek: 72 – zniżka przysługuje, bo 72 >= 65.
# Wiek: 65 – zniżka przysługuje, bo 65 >= 65.
# Wiek: 64 – zniżka nie przysługuje, bo 64 < 65 i 64 >= 18.
# Wiek: 18 – zniżka nie przysługuje, bo 18 < 18 i 18 >= 65.
# Wiek: 17 – zniżka przysługuje, bo 17 < 18.