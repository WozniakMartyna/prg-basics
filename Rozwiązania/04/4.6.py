# ZADANIE 4.6
# Należy napisać funkcję day_name(day_number),
# która zwraca pełną nazwę dnia tygodnia na podstawie numeru.
# 1 oznacza Monday, 2 oznacza Tuesday itd.,
# aż do 7, które oznacza Sunday.
# Na końcu należy sprawdzić funkcję dla numerów 5, 3 i 7.

# def tworzy funkcję day_name.
# day_number jest parametrem, czyli numerem dnia tygodnia.
def day_name(day_number):

    # Tworzymy zmienną, która będzie przechowywać nazwę dnia.
    # Pusta wartość oznacza, że numer nie pasuje do żadnego dnia.
    result = ''

    # if sprawdza, czy numer dnia jest równy 1.
    # == oznacza porównanie dwóch wartości.
    if day_number == 1:
        result = 'Monday'

    # elif sprawdza kolejne możliwe numery.
    elif day_number == 2:
        result = 'Tuesday'
    elif day_number == 3:
        result = 'Wednesday'
    elif day_number == 4:
        result = 'Thursday'
    elif day_number == 5:
        result = 'Friday'
    elif day_number == 6:
        result = 'Saturday'
    elif day_number == 7:
        result = 'Sunday'

    # Zwracamy nazwę dnia.
    # Jeśli podano numer spoza zakresu 1-7, wynikiem będzie pusty tekst.
    return result

# Testujemy funkcję dla numeru 5.
print(day_name(5))

# Testujemy funkcję dla numeru 3.
print(day_name(3))

# Testujemy funkcję dla numeru 7.
print(day_name(7))

# - Co robi ==? Sprawdza, czy dwie wartości są równe.
# - Czym różni się = od ==?
#   = przypisuje wartość, a == porównuje wartości.
# - Co robi return? Zwraca wynik funkcji.
# - Co się stanie dla numeru 8? Funkcja zwróci pusty tekst.
# - Można też użyć listy z nazwami dni i pobierać element
#   według numeru, ale wtedy trzeba pamiętać, że indeksy listy
#   zaczynają się od 0, a numery dni w zadaniu od 1.