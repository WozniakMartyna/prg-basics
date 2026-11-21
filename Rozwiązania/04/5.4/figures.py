# ZADANIE 5.4 – MODUŁ FIGURES
# Moduł zawiera funkcję rysującą kwadrat.

# Zmienna przechowująca żółwia.
# Program główny przekaże tutaj utworzonego żółwia.
pen = None

def draw_square(length):
    # Pętla wykonuje się 4 razy, ponieważ kwadrat ma 4 boki.
    for i in range(4):
        pen.forward(length)  # Rysuje bok o długości przekazanej do funkcji.
        pen.right(90)  # Obraca żółwia o 90 stopni.


# Ważne: funkcja przyjmuje jeden parametr length, czyli długość boku kwadratu.
# Nie dodajemy drugiego parametru, bo polecenie wyraźnie wymaga tylko jednego.