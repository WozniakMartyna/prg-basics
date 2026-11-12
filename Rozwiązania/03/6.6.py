# W tym zadaniu obliczamy opłatę za parking na podstawie liczby godzin postoju.
# Od 1 do 2 godzin opłata wynosi 5 PLN, od 3 do 6 godzin 15 PLN, a powyżej 6 godzin 20 PLN.

# input() pobiera liczbę godzin wpisaną przez użytkownika.
# Ponieważ input() zwraca tekst, używamy int(), aby zamienić go na liczbę całkowitą.
hours = int(input('Enter the number of parking hours: '))

# Sprawdzamy, do którego przedziału należy liczba godzin.
# Operator and oznacza "i" – oba warunki muszą być prawdziwe.
if hours >= 1 and hours <= 2:
    fee = 5
elif hours >= 3 and hours <= 6:
    fee = 15
elif hours > 6:
    fee = 20
else:
    # Jeżeli liczba godzin jest mniejsza niż 1, uznajemy ją za nieprawidłową.
    fee = 0

# Sprawdzamy, czy podano prawidłową liczbę godzin.
if hours >= 1:
    # f przed cudzysłowem oznacza f-string.
    # Dzięki nawiasom klamrowym {} możemy wstawić wartość zmiennej fee bezpośrednio do tekstu.
    print(f'Parking fee: {fee} PLN')
else:
    print('Incorrect number of parking hours')