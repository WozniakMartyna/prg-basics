# ZADANIE:
# Napisz funkcję f(n), która tworzy napis zawierający
# wszystkie liczby od 1 do n, zapisane jedna za drugą.
#
# Pomiędzy liczbami nie dodajemy spacji ani innych znaków.
#
# Przykłady:
# f(11) -> "1234567891011"
# f(4)  -> "1234"


def f(n):
    # Funkcja przyjmuje jeden argument n.
    # Określa on ostatnią liczbę, którą chcemy umieścić w napisie.
    #
    # Tworzymy zmienną result.
    # Będzie przechowywać budowany przez nas napis.
    #
    # Na początku jest pusty, dlatego wpisujemy "".
    #
    # Pamiętaj:
    # "" oznacza pusty napis (tekst bez żadnego znaku).
    # Nie jest tym samym co 0.

    result = ""

    # Pętla for przechodzi kolejno przez liczby wygenerowane przez range().
    #
    # range(1, n + 1) oznacza:
    # rozpocznij od 1 i zakończ na n włącznie.
    #
    # Dlaczego n + 1?
    # Ponieważ range() nie uwzględnia ostatniej podanej wartości.
    #
    # Przykład dla n = 4:
    # range(1, 5) daje: 1, 2, 3, 4.
    #
    # Zmienna number przyjmuje kolejno te wartości.

    for number in range(1, n + 1):

        # str(number) zamienia aktualną liczbę na napis.
        #
        # Jest to konieczne, ponieważ result jest tekstem.
        # Nie możemy bezpośrednio dodawać do tekstu liczby.
        #
        # Przykład:
        # str(1) -> "1"
        # str(10) -> "10"
        #
        # Operator += dopisuje nowy tekst na końcu istniejącego tekstu.
        #
        # Przykład:
        # result = "12"
        # result += "3"
        # result będzie teraz równy "123".

        result += str(number)

    # Po zakończeniu pętli zwracamy cały utworzony napis.

    return result


if __name__ == "__main__":

    print(f(11))  # Oczekiwany wynik: 1234567891011
    print(f(4))   # Oczekiwany wynik: 1234
    print(f(1))   # Oczekiwany wynik: 1

# if __name__ == "__main__": oznacza: wykonaj poniższy kod tylko wtedy, gdy ten plik został uruchomiony bezpośrednio, a nie zaimportowany jako moduł.