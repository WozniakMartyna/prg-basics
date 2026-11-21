# ZADANIE 7.4 – MODUŁ TEXT_COUNTER
#
# Moduł zawiera funkcję, która oblicza,
# ile razy podana litera występuje w tekście.


def count_letter(text, letter):
    # Definiujemy funkcję count_letter().
    # Parametr text oznacza tekst, w którym szukamy litery.
    # Parametr letter oznacza literę, której wystąpienia liczymy.

    count = text.count(letter)
    # Metoda count() zlicza, ile razy podany znak
    # lub fragment tekstu występuje w tekście.
    # Wynik zapisujemy w zmiennej count.
    #
    # Uwaga: metoda count() rozróżnia wielkie i małe litery.
    # Na przykład "E" i "e" są traktowane jako różne znaki.

    return count
    # Zwracamy obliczoną liczbę wystąpień litery.