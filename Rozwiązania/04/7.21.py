# ZADANIE:
# Napisz funkcję f(n1, n2, n3), która oblicza różnicę
# pomiędzy największą i najmniejszą z trzech liczb.
#
# Przykład:
# Dla liczb 4, 10, 2:
# największa liczba to 10,
# najmniejsza liczba to 2,
# różnica wynosi 10 - 2 = 8.


def f(n1, n2, n3):
    # Funkcja przyjmuje trzy liczby:
    # n1 – pierwsza liczba,
    # n2 – druga liczba,
    # n3 – trzecia liczba.
    #
    # max() zwraca największą wartość spośród podanych argumentów.
    #
    # Przykład:
    # max(4, 10, 2) -> 10

    biggest = max(n1, n2, n3)

    # min() zwraca najmniejszą wartość spośród podanych argumentów.
    #
    # Przykład:
    # min(4, 10, 2) -> 2

    smallest = min(n1, n2, n3)

    # Odejmujemy najmniejszą liczbę od największej.
    #
    # Operator - oznacza odejmowanie.
    #
    # 10 - 2 = 8

    return biggest - smallest


if __name__ == "__main__":

    print(f(4, 10, 2))    # Oczekiwany wynik: 8
    print(f(5, 5, 5))     # Oczekiwany wynik: 0
    print(f(-10, 5, 2))   # Oczekiwany wynik: 15
    print(f(-3, -8, -1))  # Oczekiwany wynik: 7