# ZADANIE 5.5 – PROGRAM GŁÓWNY
#
# Program rysuje trzy rodzaje figur:
# - kwadrat,
# - trójkąt,
# - prostokąt.
#
# Każda figura zostanie narysowana dwa razy,
# w różnych miejscach okna.
#
# Funkcje rysujące znajdują się w osobnym module figures.py.


# --------------------------------------------------
# 1. IMPORTOWANIE MODUŁÓW
# --------------------------------------------------

import turtle
# Importuje moduł turtle, który pozwala tworzyć rysunki.

import figures
# Importuje nasz własny moduł figures.py.
# Znajdują się w nim funkcje draw_square(), draw_trangle()
# i draw_rectangle().


# --------------------------------------------------
# 2. PRZYGOTOWANIE OKNA I ŻÓŁWIA
# --------------------------------------------------

window = turtle.Screen()
# Tworzy okno, w którym będą rysowane figury.

window.bgcolor("lightgreen")
# Ustawia jasnozielony kolor tła.

pen = turtle.Turtle()
# Tworzy żółwia, który będzie rysował figury.
# Zmienna pen przechowuje obiekt żółwia.

pen.speed(5)
# Ustawia szybkość rysowania.
# Można zmienić liczbę, aby żółw rysował szybciej lub wolniej.


# Przekazujemy utworzonego żółwia do modułu figures.
# Dzięki temu funkcje z pliku figures.py będą mogły
# korzystać z tego samego żółwia.
figures.pen = pen


# --------------------------------------------------
# 3. RYSOWANIE PIERWSZEGO ZESTAWU FIGUR
# --------------------------------------------------

# PIERWSZY KWADRAT

pen.penup()
# Podnosi pisak, żeby żółw nie rysował podczas przesuwania.

pen.goto(-250, 150)
# Przesuwa żółwia na współrzędne x = -250 i y = 150.
# Pierwsza liczba określa położenie poziome,
# a druga położenie pionowe.

pen.pendown()
# Opuszcza pisak, aby żółw mógł ponownie rysować.

figures.draw_square(80)
# Wywołuje funkcję rysującą kwadrat.
# Liczba 80 oznacza długość jego boku.


# PIERWSZY TRÓJKĄT

pen.penup()
# Podnosi pisak przed przesunięciem żółwia.

pen.goto(-100, 150)
# Ustawia żółwia w innym miejscu okna.

pen.pendown()
# Opuszcza pisak.

figures.draw_trangle(80)
# Wywołuje funkcję rysującą trójkąt o boku długości 80.


# PIERWSZY PROSTOKĄT

pen.penup()
pen.goto(50, 150)
pen.pendown()

figures.draw_rectangle(100, 60)
# Wywołuje funkcję rysującą prostokąt.
# Pierwsza liczba 100 oznacza długość jednego boku,
# a druga liczba 60 oznacza długość drugiego boku.


# --------------------------------------------------
# 4. RYSOWANIE DRUGIEGO ZESTAWU FIGUR
# --------------------------------------------------

# DRUGI KWADRAT

pen.penup()
pen.goto(-250, -100)
pen.pendown()

figures.draw_square(100)
# Drugi kwadrat ma bok długości 100.


# DRUGI TRÓJKĄT

pen.penup()
pen.goto(-100, -100)
pen.pendown()

figures.draw_trangle(100)
# Drugi trójkąt ma bok długości 100.


# DRUGI PROSTOKĄT

pen.penup()
pen.goto(50, -100)
pen.pendown()

figures.draw_rectangle(120, 70)
# Drugi prostokąt ma boki długości 120 i 70.


# --------------------------------------------------
# 5. ZAKOŃCZENIE PROGRAMU
# --------------------------------------------------

pen.hideturtle()
# Ukrywa żółwia, żeby nie zasłaniał gotowego rysunku.

window.mainloop()
# Utrzymuje okno otwarte, dopóki go nie zamkniemy.