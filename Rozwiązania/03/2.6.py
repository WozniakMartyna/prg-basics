# Program pobiera liczbę i wyświetla odpowiedni komunikat.
# Program sprawdza, czy liczba jest dodatnia, ujemna czy równa zero.

# input() pobiera liczbę jako tekst.
# int() zamienia tekst na liczbę całkowitą.
number = int(input('Enter number: '))

# Sprawdzamy, czy liczba jest większa od zera.
# if – sprawdza warunek. Jeśli warunek jest prawdziwy (True), wykonuje przypisany mu blok kodu.
if number > 0:
    # f-string wstawia wartość zmiennej number do tekstu za pomocą {}.
    print(f'Number {number} is positive')

# Jeśli liczba nie jest większa od zera, sprawdzamy, czy jest mniejsza od zera.
# elif – sprawdza kolejny warunek, ale tylko wtedy, gdy wcześniejszy warunek if lub elif był fałszywy (False).
elif number < 0:
    print(f'Number {number} is negative')

# Jeśli liczba nie jest ani większa, ani mniejsza od zera, musi być równa zero.
# else – wykonuje kod, gdy żaden z wcześniejszych warunków nie był prawdziwy. Nie wymaga podania warunku
else:
    print('Number is 0')

# Sprawdzanie podanych liczb:
# Liczba = 7, wynik: "Number 7 is positive"
# Liczba = 1, wynik: "Number 1 is positive"
# Liczba = 0, wynik: "Number is 0"
# Liczba = -1, wynik: "Number -1 is negative"
# Liczba = -4, wynik: "Number -4 is negative"