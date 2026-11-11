# Rok ma 12 miesięcy i 4 kwartały:
# I kwartał: miesiące 1–3
# II kwartał: miesiące 4–6
# III kwartał: miesiące 7–9
# IV kwartał: miesiące 10–12

# Program określa, do którego kwartału należy podany miesiąc.

# input() pobiera numer miesiąca jako tekst.
# int() zamienia tekst na liczbę całkowitą.
month = int(input('Enter month number (1-12): '))

# Sprawdzamy, czy miesiąc należy do czwartego kwartału.
# if – sprawdza warunek. Jeśli warunek jest prawdziwy (True), wykonuje przypisany mu blok kodu.
if month >= 10 and month <= 12:
    quarter = 4

# Sprawdzamy, czy miesiąc należy do trzeciego kwartału.
# elif sprawdza kolejny warunek, ale tylko wtedy, gdy wcześniejszy warunek if lub elif był fałszywy (False). Pozwala sprawdzić kolejne przedziały miesięcy.
elif month >= 7 and month <= 9:
    quarter = 3

# Sprawdzamy, czy miesiąc należy do drugiego kwartału.
elif month >= 4 and month <= 6:
    quarter = 2

# Sprawdzamy, czy miesiąc należy do pierwszego kwartału.
elif month >= 1 and month <= 3:
    quarter = 1

# Jeśli miesiąc nie mieści się w zakresie od 1 do 12, jest nieprawidłowy.
# else – wykonuje kod, gdy żaden z wcześniejszych warunków nie był prawdziwy. Nie wymaga podania warunku.
else:
    quarter = 0

# Jeśli kwartał jest różny od 0, wyświetlamy wynik.
# != oznacza "różne od".
if quarter != 0:
    # f-string wstawia wartości zmiennych month i quarter do tekstu.
    print(f'Month {month} is in quarter {quarter}')
else:
    print('Incorrect month number')

# Sprawdzanie podanych miesięcy:
# Miesiąc = 12, wynik: "Month 12 is in quarter 4"
# Miesiąc = 10, wynik: "Month 10 is in quarter 4"
# Miesiąc = 9, wynik: "Month 9 is in quarter 3"
# Miesiąc = 1, wynik: "Month 1 is in quarter 1"