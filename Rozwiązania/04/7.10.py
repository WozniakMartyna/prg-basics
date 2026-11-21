# ZADANIE:
# Napisz funkcję f(x, y), która zlicza ujemne liczby parzyste
# znajdujące się w przedziale od x do y.
#
# Obie granice przedziału są uwzględniane.
#
# Przykłady:
# f(-7, 8)  -> 3
# f(-1, 11) -> 0


def f(x, y):
    # Tworzymy zmienną count.
    # Będzie przechowywać liczbę znalezionych liczb spełniających warunek.
    # Na początku nie znaleźliśmy żadnej, więc wpisujemy 0.

    count = 0

    # range(x, y + 1) tworzy ciąg liczb od x do y.
    #
    # Dlaczego dodajemy 1 do y?
    # Ponieważ ostatnia wartość podana w range() NIE jest uwzględniana.
    #
    # Przykład:
    # range(-3, 3) daje: -3, -2, -1, 0, 1, 2.
    #
    # range(-3, 4) daje: -3, -2, -1, 0, 1, 2, 3.
    #
    # Dzięki y + 1 uwzględniamy również samą górną granicę przedziału.
    #
    # Zmienna number przyjmuje kolejno każdą liczbę z tego zakresu.

    for number in range(x, y + 1):

        # Sprawdzamy dwa warunki:
        #
        # number < 0
        # Liczba musi być mniejsza od zera, czyli ujemna.
        #
        # number % 2 == 0
        # Liczba musi być parzysta.
        # Reszta z dzielenia liczby parzystej przez 2 wynosi 0.
        #
        # and oznacza, że oba warunki muszą być spełnione jednocześnie.

        if number < 0 and number % 2 == 0:

            # Jeśli oba warunki są prawdziwe,
            # zwiększamy licznik o 1.
            #
            # count += 1 oznacza to samo co:
            # count = count + 1

            count += 1

    # Po zakończeniu pętli zwracamy liczbę znalezionych wartości.

    return count


if __name__ == "__main__":

    print(f(-7, 8))   # Oczekiwany wynik: 3
    print(f(-1, 11))  # Oczekiwany wynik: 0

# if __name__ == "__main__": oznacza: wykonaj poniższy kod tylko wtedy, gdy ten plik został uruchomiony bezpośrednio, a nie zaimportowany jako moduł.