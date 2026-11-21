# ZADANIE:
# Napisz funkcję f(number1, number2, operator), która wykonuje
# działanie matematyczne zależnie od podanego operatora.
#
# Obsługiwane operatory:
# +   dodawanie
# -   odejmowanie
# *   mnożenie
# %   reszta z dzielenia
# **  potęgowanie
#
# Przykładowo:
# f(5, 3, "+")  -> 8
# f(5, 3, "-")  -> 2
# f(5, 3, "*")  -> 15
# f(5, 3, "%")  -> 2
# f(5, 3, "**") -> 125


def f(number1, number2, operator):
    # Funkcja przyjmuje trzy argumenty:
    #
    # number1 – pierwsza liczba,
    # number2 – druga liczba,
    # operator – tekst określający, jakie działanie wykonać.
    #
    # Operator podajemy jako napis, np. "+" albo "**".
    # Dlatego w wywołaniu funkcji zapisujemy go w cudzysłowie.
    #
    # Przykład:
    # f(5, 3, "+")
    #
    # W zależności od wartości operatora wybieramy odpowiednie działanie.
    #
    # if oznacza "jeżeli".
    # elif oznacza "w przeciwnym razie, jeżeli".
    # else oznacza "w przeciwnym razie".
    #
    # Python sprawdza warunki po kolei.
    # Wykonuje tylko blok, którego warunek jako pierwszy okaże się prawdziwy.

    if operator == "+":

        # Znak + oznacza dodawanie.
        # Przykład: 5 + 3 = 8

        return number1 + number2

    elif operator == "-":

        # Znak - oznacza odejmowanie.
        # Przykład: 5 - 3 = 2

        return number1 - number2

    elif operator == "*":

        # Znak * oznacza mnożenie.
        # Przykład: 5 * 3 = 15

        return number1 * number2

    elif operator == "%":

        # Znak % oznacza resztę z dzielenia.
        #
        # Przykład:
        # 5 % 3 = 2
        #
        # Ponieważ 5 podzielone przez 3 daje 1
        # i pozostaje reszta 2.

        return number1 % number2

    elif operator == "**":

        # Dwa znaki ** oznaczają potęgowanie.
        #
        # Przykład:
        # 5 ** 3 oznacza 5 do potęgi trzeciej.
        #
        # Czyli:
        # 5 * 5 * 5 = 125
        #
        # Uwaga:
        # Jeden znak * oznacza mnożenie,
        # a dwa znaki ** oznaczają potęgowanie.

        return number1 ** number2

    else:

        # Jeśli użytkownik poda operator, którego nie obsługujemy,
        # zwracamy informację, że działanie jest nieprawidłowe.
        #
        # None oznacza brak konkretnej wartości.
        # Nie jest to tekst "None", tylko specjalna wartość Pythona.
        #
        # Możemy jej użyć, gdy funkcja nie może zwrócić wyniku.

        return None


if __name__ == "__main__":

    # Testujemy wszystkie obsługiwane działania.

    print(f(5, 3, "+"))   # Oczekiwany wynik: 8
    print(f(5, 3, "-"))   # Oczekiwany wynik: 2
    print(f(5, 3, "*"))   # Oczekiwany wynik: 15
    print(f(5, 3, "%"))   # Oczekiwany wynik: 2
    print(f(5, 3, "**"))  # Oczekiwany wynik: 125

    # Dodatkowy test – nieobsługiwany operator.

    print(f(5, 3, "/"))   # Oczekiwany wynik: None