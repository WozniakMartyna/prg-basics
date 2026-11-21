
# ZADANIE 7.6 – MODUŁ CARD
#
# Moduł zawiera funkcję hide(), która ukrywa część
# numeru karty płatniczej.
#
# Numer karty składa się z 16 cyfr.
# Widoczne pozostają:
# - pierwsze 2 cyfry,
# - ostatnie 4 cyfry.
#
# Pozostałe cyfry zastępujemy znakiem gwiazdki (*).


def hide(card_number):
    # Definiujemy funkcję hide().
    # Parametr card_number oznacza numer karty przekazany do funkcji.
    #
    # Numer karty zapisujemy jako tekst (string), a nie liczbę.
    # Dzięki temu możemy łatwo pobierać jego fragmenty.

    first_digits = card_number[:2]
    # Pobieramy pierwsze dwie cyfry numeru karty.
    # Zapis [:2] oznacza: pobierz znaki od początku
    # do indeksu 2, ale bez znaku o indeksie 2.

    last_digits = card_number[-4:]
    # Pobieramy ostatnie cztery cyfry numeru karty.
    # Zapis [-4:] oznacza: pobierz cztery ostatnie znaki
    # aż do końca tekstu.

    hidden_digits = "*" * 10
    # Tworzymy 10 gwiazdek.
    # Operator * powtarza tekst określoną liczbę razy.
    # W tym przypadku "*" * 10 daje "**********".

    masked_number = first_digits + hidden_digits + last_digits
    # Łączymy trzy fragmenty:
    # pierwsze dwie cyfry,
    # dziesięć gwiazdek,
    # ostatnie cztery cyfry.
    #
    # Operator + łączy ze sobą teksty.

    return masked_number
    # Zwracamy gotowy, zamaskowany numer karty.