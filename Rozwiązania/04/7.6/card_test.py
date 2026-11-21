
# ZADANIE 7.6 – PROGRAM GŁÓWNY
#
# Program testuje funkcję hide(), która ukrywa część
# numeru karty płatniczej.
# Funkcja znajduje się w osobnym module card.py.


import card
# Importujemy własny moduł card.py.
# Dzięki temu możemy korzystać z funkcji hide()
# zdefiniowanej w tym module.


def main():
    # Definiujemy główną funkcję programu.
    # Umieszczamy w niej instrukcje, które mają zostać wykonane.

    card_number = "5290312400019022"
    # Zapisujemy przykładowy 16-cyfrowy numer karty.
    # Używamy cudzysłowów, ponieważ numer traktujemy jako tekst.
    # Nie wykonujemy na nim działań matematycznych.

    masked_number = card.hide(card_number)
    # Wywołujemy funkcję hide() z modułu card.
    # Przekazujemy jej numer karty zapisany w zmiennej card_number.
    # Funkcja zwraca zamaskowany numer.
    # Wynik zapisujemy w zmiennej masked_number.

    print(masked_number)
    # Wyświetlamy zamaskowany numer karty.


if __name__ == "__main__":
    # Sprawdzamy, czy ten plik został uruchomiony bezpośrednio.
    # Jeśli tak, wykonujemy funkcję main().
    # Jeśli plik zostanie zaimportowany do innego programu,
    # funkcja main() nie uruchomi się automatycznie.

    main()
    # Uruchamiamy główną funkcję programu.