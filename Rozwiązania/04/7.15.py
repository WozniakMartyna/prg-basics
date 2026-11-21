# ZADANIE:
# Czujnik przy drzwiach zapisuje znaki:
# "+" – osoba weszła do pomieszczenia,
# "-" – osoba wyszła z pomieszczenia.
#
# Napisz funkcję f(detector), która zwraca True,
# jeśli w którymkolwiek momencie w pomieszczeniu
# znajdowały się co najmniej 3 osoby.
#
# Przykłady:
# f("+-+++-+---")   -> True
# f("+-+-+-+-")     -> False
# f("+-++-+--")     -> False
# f("+-++-++-+---") -> True


def f(detector):
    # Funkcja przyjmuje jeden argument: detector.
    # Jest to napis (str), np. "+-++-".
    #
    # Każdy znak oznacza jedno zdarzenie:
    # "+" – liczba osób zwiększa się o 1,
    # "-" – liczba osób zmniejsza się o 1.
    #
    # Tworzymy zmienną people, która przechowuje
    # aktualną liczbę osób w pomieszczeniu.
    #
    # Na początku pomieszczenie jest puste.

    people = 0

    # Tworzymy zmienną max_people.
    # Będzie przechowywać największą liczbę osób,
    # jaka pojawiła się w pomieszczeniu w trakcie pomiaru.
    #
    # Na początku największa liczba wynosi 0.

    max_people = 0

    # Pętla for przechodzi kolejno przez każdy znak napisu detector.
    #
    # Przykład:
    # Dla napisu "+-+" pętla wykona się trzy razy:
    # najpierw dla "+", potem dla "-", a na końcu dla "+".

    for event in detector:

        # Sprawdzamy, czy aktualny znak oznacza wejście.

        if event == "+":

            # Osoba weszła, więc zwiększamy liczbę osób o 1.
            #
            # people += 1 oznacza to samo co:
            # people = people + 1

            people += 1

        # Jeśli znak nie jest "+", sprawdzamy, czy jest "-".

        elif event == "-":

            # Osoba wyszła, więc zmniejszamy liczbę osób o 1.

            people -= 1

        # Po każdym zdarzeniu sprawdzamy,
        # czy aktualna liczba osób jest większa
        # od dotychczasowej największej liczby.

        if people > max_people:

            # Jeśli tak, zapisujemy nowy rekord.

            max_people = people

    # Po przejściu przez wszystkie zdarzenia sprawdzamy,
    # czy największa liczba osób wyniosła co najmniej 3.
    #
    # >= oznacza "większe lub równe".
    #
    # Wynik porównania będzie True albo False,
    # dlatego możemy go bezpośrednio zwrócić.

    return max_people >= 3


if __name__ == "__main__":

    print(f("+-+++-+---"))    # Oczekiwany wynik: True
    print(f("+-+-+-+-"))      # Oczekiwany wynik: False
    print(f("+-++-+--"))      # Oczekiwany wynik: False
    print(f("+-++-++-+---"))  # Oczekiwany wynik: True


# if __name__ == "__main__": oznacza: wykonaj poniższy kod tylko wtedy, gdy ten plik został uruchomiony bezpośrednio, a nie zaimportowany jako moduł.