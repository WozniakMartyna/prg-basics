# Program pobiera numer miesiąca i określa, ile dni ma dany miesiąc.
# Przyjmujemy, że luty zawsze ma 28 dni.

# input() pobiera numer miesiąca jako tekst.
# int() zamienia tekst na liczbę całkowitą.
month = int(input('Enter month number (1..12): '))

# Sprawdzamy, czy miesiąc ma 31 dni.
# Operator or oznacza "lub" – wystarczy jeden prawdziwy warunek.
# Operator == sprawdza, czy wartości są równe.
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    # if sprawdza pierwszą grupę miesięcy.
    days = 31  # Te miesiące mają 31 dni.

# Sprawdzamy, czy miesiąc ma 30 dni.
elif month == 4 or month == 6 or month == 9 or month == 11:
    # elif sprawdza kolejne grupy, jeśli wcześniejsze warunki były fałszywe.
    days = 30  # Te miesiące mają 30 dni.

# Sprawdzamy, czy wybrano luty.
elif month == 2:
    days = 28  # Luty ma w tym zadaniu zawsze 28 dni.

# Jeśli numer miesiąca nie należy do zakresu 1–12, jest nieprawidłowy.
else:
    # else obsługuje nieprawidłowy numer miesiąca.
    days = 0

# Jeśli liczba dni jest większa od zera, wyświetlamy wynik.
if days > 0:
    # f-string pozwala wstawić wartości zmiennych month i days do tekstu za pomocą {}.
    print(f'Month {month} has {days} days')
else:
    print('Incorrect month number')