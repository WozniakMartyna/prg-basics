# ZADANIE: Zwróć nazwę dnia tygodnia na podstawie podanego numeru.
#
# Numer 1 oznacza Monday (poniedziałek).
# Numer 2 oznacza Tuesday (wtorek).
# ...
# Numer 7 oznacza Sunday (niedzielę).
#
# Tworzymy funkcję weekday(), która otrzymuje numer dnia
# i zwraca odpowiednią nazwę z listy.


# Definiujemy funkcję o nazwie weekday.
# def rozpoczyna definicję funkcji.
# n jest parametrem, czyli wartością przekazywaną do funkcji.
def weekday(n):

    # Tworzymy listę nazw siedmiu dni tygodnia.
    # Kolejność elementów jest ważna, ponieważ wykorzystamy indeksy.
    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    # Zwracamy nazwę dnia znajdującą się na odpowiedniej pozycji.
    # Indeksy listy zaczynają się od 0, ale numery dni od 1.
    # Dlatego odejmujemy 1 od otrzymanego numeru.
    #
    # Przykład:
    # n = 1 -> weekdays[0] -> Monday.
    # n = 4 -> weekdays[3] -> Thursday.
    # n = 7 -> weekdays[6] -> Sunday.
    #
    # return przekazuje wynik funkcji do miejsca, w którym ją wywołano.
    return weekdays[n - 1]


# Definiujemy funkcję main(), która zawiera główną część programu.
def main():

    # Wywołujemy funkcję weekday() z argumentem 1.
    # Wynik funkcji zostaje przekazany do print() i wyświetlony.
    print(weekday(1))

    # Argument 4 oznacza czwartek.
    print(weekday(4))

    # Argument 7 oznacza niedzielę.
    print(weekday(7))


# Ten warunek sprawdza, czy plik został uruchomiony bezpośrednio.
# __name__ jest specjalną zmienną Pythona.
# Jeżeli uruchamiamy ten plik bezpośrednio, __name__ ma wartość "__main__".
# Wtedy wywołujemy funkcję main().
if __name__ == "__main__":
    main()