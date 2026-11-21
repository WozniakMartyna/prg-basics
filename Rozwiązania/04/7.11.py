# ZADANIE:
# Napisz funkcję f(n1, n2, n3), która sprawdza,
# czy przynajmniej jedna z trzech podanych liczb jest ujemna.
#
# Funkcja ma zwrócić:
# True  – jeśli przynajmniej jedna liczba jest ujemna,
# False – jeśli żadna liczba nie jest ujemna.


def f(n1, n2, n3):
    # Funkcja przyjmuje trzy argumenty:
    # n1 – pierwsza liczba,
    # n2 – druga liczba,
    # n3 – trzecia liczba.
    #
    # Operator < oznacza "mniejsze niż".
    #
    # Przykłady:
    # -5 < 0  -> True
    #  5 < 0  -> False
    #  0 < 0  -> False
    #
    # Operator or oznacza logiczne "LUB".
    # Wystarczy, że JEDEN z warunków będzie prawdziwy,
    # aby cały wynik był True.
    #
    # Sprawdzamy więc:
    # Czy n1 jest mniejsze od zera LUB
    # czy n2 jest mniejsze od zera LUB
    # czy n3 jest mniejsze od zera?
    #
    # return zwraca wynik sprawdzenia.
    # Nie musimy używać tutaj instrukcji if,
    # ponieważ samo wyrażenie logiczne zwraca True albo False.

    return n1 < 0 or n2 < 0 or n3 < 0


if __name__ == "__main__":

    print(f(1, 2, -3))   # True – trzecia liczba jest ujemna.
    print(f(-1, 2, 3))   # True – pierwsza liczba jest ujemna.
    print(f(1, -2, -3))  # True – druga i trzecia są ujemne.
    print(f(1, 2, 3))    # False – żadna liczba nie jest ujemna.
    print(f(0, 2, 3))    # False – zero nie jest liczbą ujemną.