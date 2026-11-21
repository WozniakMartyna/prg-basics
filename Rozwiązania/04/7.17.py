# ZADANIE:
# Napisz funkcję f(text), która sprawdza,
# czy podany napis jest palindromem.
#
# Palindrom to tekst, który czytany od początku i od końca
# wygląda tak samo.
#
# Przykłady:
# f("radar")    -> True
# f("12-11-21") -> True
# f("book")     -> False


def f(text):
    # Funkcja przyjmuje jeden argument: text.
    # Jest to napis, który chcemy sprawdzić.
    #
    # W Pythonie możemy odwrócić napis za pomocą zapisu [::-1].
    #
    # Jest to tzw. wycinanie fragmentu (slicing).
    #
    # Ogólna postać wycinania:
    # tekst[start:stop:krok]
    #
    # start – miejsce rozpoczęcia,
    # stop  – miejsce zakończenia (nie jest uwzględniane),
    # krok  – przesunięcie pomiędzy kolejnymi znakami.
    #
    # W zapisie [::-1]:
    # start jest pominięty,
    # stop jest pominięty,
    # krok wynosi -1.
    #
    # Krok -1 oznacza przechodzenie przez tekst od końca do początku.
    #
    # Przykład:
    # "radar"[::-1] daje "radar".
    # "book"[::-1] daje "koob".
    #
    # Porównujemy oryginalny tekst z tekstem odwróconym.
    #
    # Jeśli są identyczne, wynik będzie True.
    # Jeśli są różne, wynik będzie False.

    return text == text[::-1]


if __name__ == "__main__":

    print(f("radar"))     # Oczekiwany wynik: True
    print(f("12-11-21"))  # Oczekiwany wynik: True
    print(f("book"))      # Oczekiwany wynik: False

# if __name__ == "__main__": oznacza: wykonaj poniższy kod tylko wtedy, gdy ten plik został uruchomiony bezpośrednio, a nie zaimportowany jako moduł.