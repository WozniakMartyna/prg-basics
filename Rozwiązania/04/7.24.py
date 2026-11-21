# ZADANIE:
# Napisz funkcję f(expression), która oblicza wyrażenie
# matematyczne zapisane jako tekst.
#
# Wyrażenie zawiera jednocyfrowe liczby oraz znaki + i -.
#
# Przykłady:
# f("2+3")       -> 5
# f("3+8+1")     -> 12
# f("2+3-4+5-0") -> 6


def f(expression):
    # eval() odczytuje tekst jako wyrażenie Pythona i oblicza jego wynik.
    #
    # Przykład:
    # eval("2+3")       -> 5
    # eval("2+3-4+5-0") -> 6
    #
    # Zwracamy obliczony wynik.

    return eval(expression)


if __name__ == "__main__":
    print(f("2+3"))        # Oczekiwany wynik: 5
    print(f("3+8+1"))      # Oczekiwany wynik: 12
    print(f("2+3-4+5-0"))  # Oczekiwany wynik: 6