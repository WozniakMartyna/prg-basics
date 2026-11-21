# ZADANIE:
# Napisz funkcję f(text), która usuwa wszystkie spacje z podanego tekstu.
#
# Przykłady:
# f("Ala ma kota")       -> "Alamakota"
# f("Python jest super") -> "Pythonjestsuper"
# f("Hello")             -> "Hello"


def f(text):
    # Funkcja przyjmuje jeden argument: text.
    # Jest to tekst, z którego chcemy usunąć spacje.
    #
    # Wykorzystujemy metodę replace().
    #
    # replace() służy do zamieniania jednego fragmentu tekstu
    # na inny fragment.
    #
    # Ogólna postać:
    # tekst.replace("co_zamienić", "na_co_zamienić")
    #
    # W naszym przypadku:
    # text.replace(" ", "")
    #
    # Pierwszy argument " " to jedna spacja.
    # Drugi argument "" to pusty tekst.
    #
    # Oznacza to:
    # zamień każdą spację na pusty tekst.
    #
    # Dzięki temu spacje zostaną usunięte.
    #
    # Ważne:
    # replace() nie zmienia oryginalnego napisu.
    # Zwraca nowy napis z dokonanymi zmianami.
    # Dlatego od razu zwracamy wynik za pomocą return.

    return text.replace(" ", "")


if __name__ == "__main__":

    print(f("Ala ma kota"))        # Oczekiwany wynik: Alamakota
    print(f("Python jest super"))  # Oczekiwany wynik: Pythonjestsuper
    print(f("Hello"))              # Oczekiwany wynik: Hello
    print(f("A  B"))               # Oczekiwany wynik: AB

# if __name__ == "__main__": oznacza: wykonaj poniższy kod tylko wtedy, gdy ten plik został uruchomiony bezpośrednio, a nie zaimportowany jako moduł.