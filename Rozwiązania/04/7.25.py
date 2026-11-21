# ZADANIE:
# Napisz funkcję f(x, y), która oblicza sumę liczb z przedziału
# od x do y (włącznie), które:
# - są podzielne przez 2,
# - są podzielne przez 3,
# - NIE są podzielne przez 4.
#
# Przykłady:
# f(1, 20)  -> 24
# f(10, 30) -> 48


def f(x, y):
    total = 0  # Zmienna przechowująca sumę. Na początku wynosi 0.

    # range(x, y + 1) uwzględnia również końcową wartość y.
    for number in range(x, y + 1):

        # % oznacza resztę z dzielenia.
        # Reszta 0 oznacza, że liczba dzieli się bez reszty.
        #
        # number % 2 == 0 -> liczba jest parzysta.
        # number % 3 == 0 -> liczba dzieli się przez 3.
        # number % 4 != 0 -> liczba NIE dzieli się przez 4.
        #
        # and oznacza, że wszystkie trzy warunki muszą być prawdziwe.

        if number % 2 == 0 and number % 3 == 0 and number % 4 != 0:
            total += number  # Dodajemy pasującą liczbę do sumy.

    return total  # Zwracamy obliczoną sumę.


if __name__ == "__main__":
    print(f(1, 20))   # Oczekiwany wynik: 24
    print(f(10, 30))  # Oczekiwany wynik: 48