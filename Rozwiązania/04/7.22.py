# ZADANIE:
# Napisz funkcję f(text), która tworzy akronim z podanego tekstu.
#
# Akronim to skrót utworzony z pierwszych liter kolejnych wyrazów.
#
# Przykład:
# "Central Intelligence Agency" -> "CIA"
#
# Funkcja ma zwrócić pierwsze litery wszystkich wyrazów
# zapisane wielkimi literami.


def f(text):
    # Funkcja przyjmuje jeden argument: text.
    # Jest to tekst, z którego chcemy utworzyć akronim.
    #
    # Najpierw korzystamy z metody split().
    #
    # split() dzieli tekst na wyrazy.
    # Domyślnie rozdziela tekst w miejscach występowania białych znaków,
    # np. spacji, tabulatorów i znaków nowej linii.
    #
    # Przykład:
    # "Central Intelligence Agency".split()
    #
    # Wynik:
    # ["Central", "Intelligence", "Agency"]
    #
    # Otrzymujemy listę, w której każdy element jest osobnym wyrazem.

    words = text.split()

    # Tworzymy pusty napis acronym.
    # Będziemy do niego dopisywać pierwsze litery wyrazów.

    acronym = ""

    # Pętla for przechodzi po wszystkich wyrazach z listy words.
    #
    # W każdym przejściu zmienna word przechowuje jeden wyraz.

    for word in words:

        # Zapis word[0] oznacza pierwszy znak tekstu.
        #
        # W Pythonie indeksowanie znaków zaczyna się od 0.
        #
        # Przykład:
        # word = "Central"
        #
        # word[0] -> "C"
        # word[1] -> "e"
        # word[2] -> "n"
        #
        # upper() zamienia litery na wielkie.
        #
        # Przykład:
        # "c".upper() -> "C"
        #
        # Dopisujemy pierwszą literę wyrazu do akronimu.

        acronym += word[0].upper()

    # Zwracamy gotowy akronim.

    return acronym


if __name__ == "__main__":

    print(f("Central Intelligence Agency"))  # CIA
    print(f("World Health Organization"))   # WHO
    print(f("North Atlantic Treaty Organization"))  # NATO
    print(f("Python"))  # P
    print(f(""))        # Pusty napis