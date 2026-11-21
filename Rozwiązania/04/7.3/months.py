# ZADANIE 7.3 – MODUŁ MONTHS
# 
# Celem zadania jest utworzenie funkcji month(n),
# która zwraca nazwę miesiąca na podstawie jego numeru.
#
# Numery miesięcy:
# 1 - January
# 2 - February
# 3 - March
# 4 - April
# 5 - May
# 6 - June
# 7 - July
# 8 - August
# 9 - September
# 10 - October
# 11 - November
# 12 - December


def month(n):
    # Definiujemy funkcję month().
    # Parametr n oznacza numer miesiąca przekazany do funkcji.

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    # Tworzymy listę zawierającą nazwy wszystkich 12 miesięcy.
    # Elementy listy mają indeksy od 0 do 11.
    # Dlatego od numeru miesiąca odejmujemy 1.

    return months[n - 1]
    # Zwracamy nazwę miesiąca.
    # Przykładowo: dla n = 9 otrzymujemy months[8],
    # czyli "September".