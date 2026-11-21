# ZADANIE 7.3 – PROGRAM GŁÓWNY
#
# Program pobiera od użytkownika numer miesiąca,
# a następnie wyświetla nazwę tego miesiąca.
# Do pobrania nazwy wykorzystuje funkcję month()
# z osobnego modułu months.py.


import months
# Importujemy własny moduł months.py.
# Dzięki temu możemy korzystać z funkcji zapisanej w tym pliku.


def main():
    # Definiujemy funkcję main(), czyli główną część programu.
    # Umieszczamy w niej instrukcje, które mają zostać wykonane.

    n = int(input("Enter month number: "))
    # input() pobiera tekst wpisany przez użytkownika.
    # int() zamienia ten tekst na liczbę całkowitą.
    # Wynik zapisujemy w zmiennej n.

    month_name = months.month(n)
    # Wywołujemy funkcję month() z modułu months.
    # Przekazujemy jej numer miesiąca zapisany w zmiennej n.
    # Zwrócona nazwa miesiąca zostaje zapisana w month_name.

    print(f"The name of month {n} is {month_name}")
    # Wyświetlamy wynik.
    # Litera f przed tekstem pozwala wstawiać wartości zmiennych
    # do tekstu za pomocą nawiasów klamrowych {}.


if __name__ == "__main__":
    # Ten warunek sprawdza, czy uruchamiamy ten plik bezpośrednio.
    # Jeśli tak, wykonujemy funkcję main().
    # Jeśli plik zostałby zaimportowany do innego programu,
    # funkcja main() nie uruchomiłaby się automatycznie.

    main()
    # Wywołujemy główną funkcję programu.