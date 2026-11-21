# ZADANIE 7.5 – MODUŁ NUMBER_RANGE
#
# Moduł zawiera funkcję, która sprawdza,
# czy podana liczba znajduje się w określonym zakresie.
#
# Funkcja zwraca True, jeśli liczba należy do zakresu,
# lub False, jeśli znajduje się poza nim.


def is_in_range(x, y, number):
    # Definiujemy funkcję is_in_range().
    # Parametr x oznacza początek zakresu.
    # Parametr y oznacza koniec zakresu.
    # Parametr number oznacza liczbę, którą sprawdzamy.

    return x <= number <= y
    # Sprawdzamy, czy number jest większe lub równe x
    # ORAZ jednocześnie mniejsze lub równe y.
    #
    # Operator <= oznacza "mniejsze lub równe".
    # Jeśli oba warunki są prawdziwe, funkcja zwraca True.
    # W przeciwnym razie zwraca False.