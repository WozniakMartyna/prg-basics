## ZADANIE 5.4 – PIERWSZA WERSJA
## Program rysuje kwadrat o boku długości 100 za pomocą modułu turtle.

# import turtle  # Importuje moduł turtle, który umożliwia rysowanie.

## Ustawienia okna.
# window = turtle.Screen()  # Tworzy okno do rysowania.
# window.bgcolor("lightgreen")  # Ustawia jasnozielone tło.

## Tworzy żółwia, który będzie rysował.
# pen = turtle.Turtle()
# pen.speed(5)  # Ustawia szybkość rysowania.

## Długość boku kwadratu.
# side_length = 100

## Rysowanie kwadratu.
## Pętla wykonuje się 4 razy, ponieważ kwadrat ma 4 boki.
# for i in range(4):
    # pen.forward(side_length)  # Rysuje jeden bok.
    # pen.right(90)  # Obraca żółwia o 90 stopni w prawo.

## Ukrywa żółwia i kończy program po zamknięciu okna.
# pen.hideturtle()
# window.mainloop()


# ZADANIE 5.4 – DRUGA WERSJA
# Program rysuje kwadrat za pomocą funkcji z osobnego modułu figures.

import turtle  # Importuje moduł do rysowania.
import figures  # Importuje nasz moduł z funkcją draw_square.

# Ustawienia okna.
window = turtle.Screen()
window.bgcolor("lightgreen")

# Tworzy żółwia, który będzie rysował.
pen = turtle.Turtle()
pen.speed(5)

# Przekazuje żółwia do modułu figures,
# aby funkcja draw_square mogła z niego korzystać.
figures.pen = pen

# Długość boku kwadratu.
side_length = 100

# Wywołuje funkcję draw_square z modułu figures.
# Przekazuje jej długość boku jako argument.
figures.draw_square(side_length)

# Ukrywa żółwia i kończy program po zamknięciu okna.
pen.hideturtle()
window.mainloop()