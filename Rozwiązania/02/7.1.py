# Program sprawdza, czy osoba ma nie więcej niż 26 lat.

# Program sprawdza, czy osoba jest zwolniona z podatku ze względu na wiek.

# Pobieramy wiek użytkownika.
# input() pobiera wpisaną wartość jako tekst.
# int() zamienia tekst na liczbę całkowitą.
age = int(input('Enter age: '))

# Sprawdzamy, czy wiek jest mniejszy lub równy 26.
# Operator <= oznacza "mniejsze lub równe".
# Wynik porównania będzie True albo False.
no_tax = age <= 26

# Wyświetlamy informację o zwolnieniu z podatku.
# f przed tekstem oznacza f-string. Dzięki {} możemy wstawić wartość zmiennej do tekstu.
# Wartość zmiennej no_tax zostanie wstawiona w miejscu {}.
print(f'Exemption from paying taxes: {no_tax}')