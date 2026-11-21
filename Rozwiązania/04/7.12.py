# ZADANIE:
# Napisz funkcję f(n), która zwraca napis składający się z n gwiazdek.
# Każda gwiazdka ma być oddzielona znakiem ukośnika /.
#
# Przykłady:
# f(4) -> "*/*/*/*"
# f(1) -> "*"
#
# Dla n = 0 zwracamy pusty napis "".


def f(n):
    # Funkcja przyjmuje jeden argument n.
    # n określa, ile gwiazdek ma znaleźć się w wyniku.
    #
    # Najpierw tworzymy listę gwiazdek.
    #
    # Zapis ["*"] oznacza listę zawierającą jeden element – tekst "*".
    #
    # Operator * użyty z listą oznacza jej powielenie.
    #
    # Przykład:
    # ["*"] * 4
    # daje listę:
    # ["*", "*", "*", "*"]
    #
    # Jeśli n wynosi 0, otrzymamy pustą listę [].

    stars = ["*"] * n

    # Teraz korzystamy z metody join().
    #
    # join() łączy elementy listy w jeden napis.
    #
    # Zapis:
    # "/".join(stars)
    #
    # oznacza:
    # połącz wszystkie elementy listy, wstawiając między nimi znak "/".
    #
    # Przykład:
    # ["*", "*", "*", "*"]
    #
    # Po połączeniu otrzymamy:
    # "*/*/*/*"
    #
    # Ważne:
    # Znak "/" nie pojawi się na początku ani na końcu wyniku.
    # Zostanie wstawiony tylko POMIĘDZY elementami.
    #
    # Wynik działania join() zwracamy za pomocą return.

    return "/".join(stars)


if __name__ == "__main__":

    print(f(4))  # Oczekiwany wynik: */*/*/*
    print(f(1))  # Oczekiwany wynik: *
    print(f(0))  # Oczekiwany wynik: pusty napis

# if __name__ == "__main__": oznacza: wykonaj poniższy kod tylko wtedy, gdy ten plik został uruchomiony bezpośrednio, a nie zaimportowany jako moduł.