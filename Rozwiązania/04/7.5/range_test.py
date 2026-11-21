
# ZADANIE 7.5 – PROGRAM GŁÓWNY
#
# Program pobiera liczbę od użytkownika
# i sprawdza, czy znajduje się ona w zakresie <2, 15>.
# Do sprawdzenia wykorzystuje funkcję z modułu number_range.


import number_range
# Importujemy własny moduł number_range.py.
# Dzięki temu możemy korzystać z funkcji is_in_range().


def main():
    # Definiujemy główną funkcję programu.

    number = int(input("A number: "))
    # Pobieramy liczbę od użytkownika.
    # input() odczytuje tekst, a int() zamienia go na liczbę całkowitą.

    x = 2
    # Ustalamy początek zakresu.

    y = 15
    # Ustalamy koniec zakresu.

    result = number_range.is_in_range(x, y, number)
    # Wywołujemy funkcję is_in_range() z modułu number_range.
    # Przekazujemy początek zakresu, koniec zakresu i sprawdzaną liczbę.
    # Wynik True lub False zapisujemy w zmiennej result.

    if result:
        # Jeśli result ma wartość True, wykonujemy poniższą instrukcję.

        answer = "yes"
        # Zapisujemy tekst "yes".

    else:
        # Jeśli result ma wartość False, wykonujemy tę część programu.

        answer = "no"
        # Zapisujemy tekst "no".

    print(f"Number {number} in the range <{x},{y}>: {answer}")
    # Wyświetlamy sprawdzaną liczbę, zakres i odpowiedź.
    # f przed tekstem pozwala wstawiać wartości zmiennych w nawiasach {}.


if __name__ == "__main__":
    # Sprawdzamy, czy plik został uruchomiony bezpośrednio.

    main()
    # Uruchamiamy główną funkcję programu.