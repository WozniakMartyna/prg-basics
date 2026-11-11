# Liczba nieujemna to liczba większa lub równa zero.
# Program pobiera dwie liczby i sprawdza, czy przynajmniej jedna z nich jest nieujemna.

# input() pobiera pierwszą liczbę jako tekst.
# int() zamienia tekst na liczbę całkowitą.
x = int(input('Enter first number: '))

# Pobieramy drugą liczbę.
y = int(input('Enter second number: '))

# Operator < sprawdza, czy liczba jest mniejsza od zera.
# not odwraca wynik sprawdzenia.
# not x < 0 oznacza, że x nie jest mniejsze od zera, czyli x jest większe lub równe zero.
# Operator or oznacza "lub" – wystarczy, że jeden warunek jest prawdziwy.
if not x < 0 or not y < 0:
    # if wykonuje kod, gdy przynajmniej jedna liczba jest nieujemna.
    # f-string pozwala wstawiać wartości zmiennych do tekstu za pomocą {}.
    print(f'At least one of the numbers {x} and {y} is not negative')
else:
    # else wykonuje kod, gdy obie liczby są ujemne.
    print('Both numbers are negative')