# ZADANIE:
# Napisz funkcję f(n), która zwraca n-tą wartość ciągu Fibonacciego.
#
# Ciąg Fibonacciego rozpoczyna się od:
# 0, 1, 1, 2, 3, 5, 8, 13, 21...
#
# Każda kolejna liczba jest sumą dwóch poprzednich.
#
# W tym zadaniu:
# pierwsza wartość to 0,
# druga wartość to 1.
#
# Przykłady:
# f(5) -> 3
# f(9) -> 21


def f(n):
    # Funkcja przyjmuje argument n.
    # Określa on, którą wartość ciągu chcemy otrzymać.
    #
    # Numerowanie zaczyna się od 1:
    # n = 1 oznacza pierwszą wartość, czyli 0.
    # n = 2 oznacza drugą wartość, czyli 1.
    #
    # Sprawdzamy, czy n jest równe 1.

    if n == 1:

        # Jeśli tak, zwracamy pierwszą wartość ciągu.

        return 0

    # Sprawdzamy, czy n jest równe 2.

    if n == 2:

        # Jeśli tak, zwracamy drugą wartość ciągu.

        return 1

    # Tworzymy dwie zmienne przechowujące
    # dwie poprzednie liczby ciągu.
    #
    # previous oznacza poprzednią liczbę.
    # current oznacza aktualną liczbę.
    #
    # Na początku ciąg wygląda tak:
    # 0, 1
    #
    # Dlatego przypisujemy:
    # previous = 0
    # current = 1

    previous = 0
    current = 1

    # Teraz obliczamy kolejne wartości.
    #
    # range(3, n + 1) oznacza:
    # rozpocznij od 3 i zakończ na n włącznie.
    #
    # Dlaczego zaczynamy od 3?
    # Ponieważ pierwsze dwie wartości już znamy:
    # 1. wartość = 0
    # 2. wartość = 1
    #
    # Kolejna, czyli trzecia wartość, to 0 + 1 = 1.

    for i in range(3, n + 1):

        # Obliczamy nową wartość jako sumę dwóch poprzednich.
        #
        # Przykład:
        # previous = 1
        # current = 2
        #
        # new_value = 1 + 2 = 3

        new_value = previous + current

        # Przesuwamy wartości o jedno miejsce.
        #
        # Dotychczasowa wartość current staje się previous.
        # Nowo obliczona wartość staje się current.
        #
        # Dzięki temu w następnym przejściu pętli
        # znów będziemy mieć dwie ostatnie liczby ciągu.

        previous = current
        current = new_value

    # Po zakończeniu pętli current zawiera n-tą wartość ciągu.
    # Zwracamy ją.

    return current


if __name__ == "__main__":

    print(f(1))  # Oczekiwany wynik: 0
    print(f(2))  # Oczekiwany wynik: 1
    print(f(5))  # Oczekiwany wynik: 3
    print(f(9))  # Oczekiwany wynik: 21