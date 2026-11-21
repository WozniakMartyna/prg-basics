
# ZADANIE 7.2 – IF __NAME__ == "__MAIN__"
#
# Program prezentuje działanie funkcji main()
# oraz konstrukcji if __name__ == "__main__".
#
# Dzięki tej konstrukcji możemy zdecydować,
# które instrukcje wykonają się po bezpośrednim
# uruchomieniu pliku, a które nie wykonają się
# podczas importowania go jako modułu.


def add(a, b):
    # Funkcja add() przyjmuje dwie liczby: a oraz b.
    # Znak + dodaje do siebie obie liczby.
    # return zwraca obliczony wynik.
    return a + b


def subtract(a, b):
    # Funkcja subtract() przyjmuje dwie liczby.
    # Znak - odejmuje drugą liczbę od pierwszej.
    return a - b


def main():
    # Funkcja main() zawiera główną część programu.
    # Dzięki niej porządkujemy instrukcje programu.

    x = 10
    # Przypisujemy wartość 10 do zmiennej x.

    y = 5
    # Przypisujemy wartość 5 do zmiennej y.

    print(f"Add: {add(x, y)}")
    # Wywołujemy funkcję add() i wyświetlamy wynik dodawania.
    # f przed tekstem pozwala wstawiać wartości w nawiasach {}.

    print(f"Subtract: {subtract(x, y)}")
    # Wywołujemy funkcję subtract() i wyświetlamy wynik odejmowania.


if __name__ == "__main__":
    # Sprawdzamy, czy plik został uruchomiony bezpośrednio.
    # Jeśli tak, Python wykona instrukcje znajdujące się w tym bloku.
    # Jeśli plik zostanie zaimportowany do innego pliku,
    # ten blok nie zostanie wykonany.

    main()
    # Uruchamiamy funkcję główną programu.