# ZADANIE:
# Automat przyjmuje monety o nominałach 1 zł, 2 zł i 5 zł.
# Napisz funkcję f(amount_to_pay), która oblicza minimalną liczbę
# monet potrzebnych do zapłacenia podanej kwoty.
#
# Przykłady:
# f(23) -> 6
# f(8)  -> 3
# f(2)  -> 1
# f(0)  -> 0


def f(amount_to_pay):
    # Na początku tworzymy zmienną coin_count.
    # Będzie ona przechowywać liczbę użytych monet.
    # Na początku nie użyliśmy jeszcze żadnej, więc wpisujemy 0.

    coin_count = 0

    # Najpierw używamy jak największej liczby monet 5-złotowych.
    #
    # Operator // oznacza dzielenie całkowite.
    # Zwraca wynik dzielenia bez części po przecinku.
    #
    # Przykład:
    # 23 // 5 = 4
    # Oznacza to, że w kwocie 23 zł mieszczą się cztery monety 5 zł.
    #
    # Operator += oznacza:
    # coin_count = coin_count + ...
    #
    # Czyli dodajemy liczbę monet 5-złotowych do naszego licznika.

    coin_count += amount_to_pay // 5

    # Operator % oznacza resztę z dzielenia.
    #
    # Przykład:
    # 23 % 5 = 3
    # Po zabraniu czterech monet po 5 zł zostają nam 3 zł.
    #
    # Zapisujemy pozostałą kwotę z powrotem do amount_to_pay.

    amount_to_pay = amount_to_pay % 5

    # Teraz analogicznie wykorzystujemy monety 2-złotowe.
    #
    # Jeśli zostały nam 3 zł:
    # 3 // 2 = 1, czyli możemy użyć jednej monety 2 zł.
    #
    # Pozostała kwota:
    # 3 % 2 = 1 zł.

    coin_count += amount_to_pay // 2
    amount_to_pay = amount_to_pay % 2

    # Na końcu wykorzystujemy monety 1-złotowe.
    #
    # Ponieważ pozostała kwota może wynosić tylko 0 albo 1,
    # dodajemy ją bezpośrednio do liczby monet.
    #
    # Przykład:
    # Jeśli zostało 1 zł, potrzebujemy jednej monety.
    # Jeśli zostało 0 zł, nie potrzebujemy już żadnej.

    coin_count += amount_to_pay

    # return zwraca wynik działania funkcji.
    # Dzięki temu możemy później przypisać wynik do zmiennej
    # albo wyświetlić go za pomocą print().

    return coin_count


if __name__ == "__main__":

    print(f(23))  # Oczekiwany wynik: 6
    print(f(8))   # Oczekiwany wynik: 3
    print(f(2))   # Oczekiwany wynik: 1
    print(f(0))   # Oczekiwany wynik: 0