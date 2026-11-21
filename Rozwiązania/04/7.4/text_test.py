# ZADANIE 7.4 – PROGRAM GŁÓWNY
#
# Program sprawdza, ile razy litera 'e'
# występuje w podanym zdaniu.
# Do obliczeń wykorzystuje funkcję z modułu text_counter.py.


import text_counter
# Importujemy własny moduł text_counter.py.
# Dzięki temu możemy korzystać z funkcji count_letter().


def main():
    # Definiujemy główną funkcję programu.
    # Umieszczamy w niej instrukcje wykonywane po uruchomieniu programu.

    text = "You never get a second chance to make a first impression"
    # Zapisujemy zdanie, w którym będziemy szukać litery.

    letter = "e"
    # Określamy literę, której wystąpienia chcemy policzyć.

    result = text_counter.count_letter(text, letter)
    # Wywołujemy funkcję count_letter() z modułu text_counter.
    # Przekazujemy jej tekst oraz szukaną literę.
    # Wynik działania funkcji zapisujemy w zmiennej result.

    print(text)
    # Wyświetlamy tekst.

    print(f"The number of letter '{letter}': {result}")
    # Wyświetlamy literę oraz liczbę jej wystąpień.
    # f przed tekstem pozwala wstawiać wartości zmiennych w nawiasach {}.


if __name__ == "__main__":
    # Sprawdzamy, czy ten plik został uruchomiony bezpośrednio.
    # Jeśli tak, wykonujemy funkcję main().
    # Jeśli plik zostanie zaimportowany do innego programu,
    # funkcja main() nie uruchomi się automatycznie.

    main()
    # Uruchamiamy główną funkcję programu.