# ZADANIE:
# Napisz funkcję f(number, even), która oblicza sumę cyfr liczby.
#
# Jeśli even == True, dodajemy tylko cyfry parzyste.
# Jeśli even == False, dodajemy tylko cyfry nieparzyste.
#
# Przykłady:
# f(3124, True)   -> 6
# f(3124, False)  -> 4
# f(20576, False) -> 12
# f(20576, True)  -> 8
# f(13115, True)  -> 0


def f(number, even):
    # Funkcja otrzymuje dwa argumenty:
    # number – liczba, której cyfry sprawdzamy.
    # even – wartość logiczna True albo False.
    #
    # True oznacza prawdę, a False oznacza fałsz.
    #
    # Tworzymy zmienną total, która będzie przechowywać sumę.
    # Na początku suma wynosi 0.

    total = 0

    # abs() zwraca wartość bezwzględną liczby.
    # Dzięki temu możemy obsłużyć również liczbę ujemną.
    #
    # str() zamienia liczbę na tekst.
    #
    # Przykład:
    # abs(-3124) -> 3124
    # str(3124)  -> "3124"
    #
    # Dzięki zamianie na tekst możemy przejść po każdej cyfrze
    # osobno za pomocą pętli for.

    for digit in str(abs(number)):

        # int() zamienia tekst przedstawiający cyfrę na liczbę.
        #
        # Przykład:
        # int("3") -> 3
        #
        # Jest to potrzebne, ponieważ chcemy wykonywać obliczenia.

        digit = int(digit)

        # Sprawdzamy, czy użytkownik chce sumować cyfry parzyste.
        #
        # Jeśli even == True, sprawdzamy:
        # digit % 2 == 0
        #
        # % 2 zwraca resztę z dzielenia przez 2.
        # Cyfra parzysta ma resztę 0.
        #
        # Jeśli even == False, sprawdzamy:
        # digit % 2 != 0
        #
        # != oznacza "różne od".
        # Cyfra nieparzysta ma resztę inną niż 0.
        #
        # Zapis if/else pozwala wybrać odpowiedni warunek.

        if even:
            if digit % 2 == 0:
                total += digit

        else:
            if digit % 2 != 0:
                total += digit

    # Zwracamy obliczoną sumę cyfr.

    return total


if __name__ == "__main__":

    print(f(3124, True))    # Oczekiwany wynik: 6
    print(f(3124, False))   # Oczekiwany wynik: 4
    print(f(20576, False))  # Oczekiwany wynik: 12
    print(f(20576, True))   # Oczekiwany wynik: 8
    print(f(13115, True))   # Oczekiwany wynik: 0