# Program pobiera numer miesiąca i dzień, a następnie sprawdza, czy taki dzień istnieje w wybranym miesiącu.
# Zakładamy, że luty ma zawsze 28 dni.

# input() pobiera numer miesiąca jako tekst.
# int() zamienia tekst na liczbę całkowitą.
month = int(input('Enter month number (1..12): '))

# Pobieramy numer dnia.
day = int(input('Enter the day number of the month: '))

# Na początku zakładamy, że podany dzień jest niepoprawny.
day_ok = False

# Sprawdzamy miesiące, które mają 31 dni.
# or oznacza "lub" – wystarczy jeden prawdziwy warunek.
# == sprawdza, czy wartości są równe.
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    # if sprawdza warunek i wykonuje przypisany mu blok kodu, jeśli jest prawdziwy.
    # Sprawdzamy, czy dzień jest w przedziale od 1 do 31.
    # and oznacza "i" – oba warunki muszą być prawdziwe.
    if day >= 1 and day <= 31:
        day_ok = True

# Sprawdzamy miesiące, które mają 30 dni.
elif month == 4 or month == 6 or month == 9 or month == 11:
    # elif sprawdza kolejny warunek, jeśli poprzedni był fałszywy.
    # Dzień musi być większy lub równy 1 i mniejszy lub równy 30.
    if day >= 1 and day <= 30:
        day_ok = True

# Sprawdzamy, czy wybrano luty.
elif month == 2:
    # W lutym dzień musi być w przedziale od 1 do 28.
    if day >= 1 and day <= 28:
        day_ok = True
        
# Tworzymy komunikat z wykorzystaniem f-stringa.
# f przed tekstem pozwala wstawiać wartości zmiennych za pomocą {}.
message = f'Day {day} for the month {month}'

# Sprawdzamy, czy dzień został uznany za poprawny.
if day_ok:
    print(f'{message} is correct')
else:
    print(f'{message} is incorrect')