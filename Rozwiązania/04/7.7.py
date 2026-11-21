# ZADANIE:
# Napisz funkcję f(binary_number), która sprawdza, czy podany napis
# składa się wyłącznie z cyfr 0 i 1.
#
# Przykłady:
# f("101101")       -> True
# f("1311a10100")   -> False


def f(binary_number):
    # Funkcja przyjmuje jeden argument: binary_number.
    # Jest to napis (str), czyli tekst, a nie liczba typu int.
    #
    # Dlaczego używamy tekstu?
    # Ponieważ chcemy sprawdzać poszczególne znaki, np. "1", "0", "a".
    #
    # all() sprawdza, czy WSZYSTKIE elementy spełniają podany warunek.
    #
    # W zapisie:
    # char in "01"
    #
    # sprawdzamy, czy znak char znajduje się w tekście "01".
    # Czyli czy jest równy "0" albo "1".
    #
    # for char in binary_number oznacza:
    # przejdź po kolei przez każdy znak napisu binary_number.
    #
    # Przykład:
    # Dla "101" sprawdzimy kolejno: "1", "0", "1".
    #
    # all() zwróci True tylko wtedy, gdy każdy znak będzie poprawny.
    #
    # Dodatkowo sprawdzamy len(binary_number) > 0.
    # len() zwraca długość tekstu, czyli liczbę jego znaków.
    # Dzięki temu pusty napis nie zostanie uznany za liczbę binarną.
    #
    # Operator and oznacza "i".
    # Oba warunki muszą być prawdziwe.

    return len(binary_number) > 0 and all(char in "01" for char in binary_number)


# Ten warunek sprawia, że poniższy fragment uruchomi się tylko wtedy,
# gdy uruchomimy ten plik bezpośrednio.
# Nie uruchomi się automatycznie, gdybyśmy zaimportowali ten plik
# do innego programu.
if __name__ == "__main__":

    # Wywołujemy funkcję i wyświetlamy jej wyniki.
    print(f("101101"))       # Oczekiwany wynik: True
    print(f("1311a10100"))   # Oczekiwany wynik: False
    print(f(""))             # Oczekiwany wynik: False