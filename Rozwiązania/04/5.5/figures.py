
# ZADANIE 5.5 – MODUŁ FIGURES
#
# W tym pliku definiujemy trzy funkcje:
# 1. draw_square() – rysuje kwadrat.
# 2. draw_trangle() – rysuje trójkąt równoramienny.
# 3. draw_rectangle() – rysuje prostokąt.
#
# Funkcje zostaną później wykorzystane w programie głównym
# zapisanym w pliku draw_figures.py.


# Zmienna pen będzie przechowywać obiekt żółwia,
# który zostanie utworzony w programie głównym.
#
# Na razie przypisujemy jej wartość None, czyli brak obiektu.
# Później program główny przekaże tutaj swojego żółwia.
pen = None


# --------------------------------------------------
# FUNKCJA 1 – RYSOWANIE KWADRATU
# --------------------------------------------------

# def oznacza definiowanie, czyli tworzenie funkcji.
# draw_square to nazwa funkcji.
# length to parametr – będzie przechowywał długość boku kwadratu.
def draw_square(length):

    # Kwadrat ma 4 boki, dlatego pętla wykona się 4 razy.
    # range(4) oznacza cztery powtórzenia: 0, 1, 2, 3.
    for i in range(4):

        # forward(length) przesuwa żółwia do przodu
        # o odległość podaną w parametrze length.
        pen.forward(length)

        # right(90) obraca żółwia o 90 stopni w prawo.
        # Dzięki temu żółw może narysować kolejny bok kwadratu.
        pen.right(90)


# --------------------------------------------------
# FUNKCJA 2 – RYSOWANIE TRÓJKĄTA RÓWNORAMIENNEGO
# --------------------------------------------------

# draw_trangle to nazwa funkcji zgodna z poleceniem.
# length oznacza długość boku trójkąta.
#
# Rysujemy trójkąt równoboczny, który jest szczególnym
# przypadkiem trójkąta równoramiennego (ma wszystkie boki równe).
def draw_trangle(length):

    # Trójkąt ma 3 boki, dlatego pętla wykona się 3 razy.
    for i in range(3):

        # Rysuje jeden bok trójkąta o długości length.
        pen.forward(length)

        # Obraca żółwia o 120 stopni w prawo.
        # Trzy takie obroty pozwalają zamknąć trójkąt.
        pen.right(120)


# --------------------------------------------------
# FUNKCJA 3 – RYSOWANIE PROSTOKĄTA
# --------------------------------------------------

# draw_rectangle to nazwa funkcji.
# lenght_a – długość jednego boku prostokąta.
# lenght_b – długość drugiego boku prostokąta.
#
# Funkcja otrzymuje dwa parametry, ponieważ prostokąt
# ma dwa różne wymiary: długość i szerokość.
def draw_rectangle(lenght_a, lenght_b):

    # Prostokąt ma 4 boki, ale wystarczy wykonać
    # pętlę 2 razy, ponieważ jego boki występują parami.
    for i in range(2):

        # Rysuje pierwszy bok o długości lenght_a.
        pen.forward(lenght_a)

        # Obraca żółwia o 90 stopni.
        pen.right(90)

        # Rysuje drugi bok o długości lenght_b.
        pen.forward(lenght_b)

        # Ponownie obraca żółwia o 90 stopni.
        pen.right(90)