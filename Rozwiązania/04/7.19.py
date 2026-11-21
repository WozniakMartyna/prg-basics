# ZADANIE:
# Napisz funkcję f(number), która oblicza sumę cyfr,
# które występują w liczbie więcej niż jeden raz.
#
# Ważne:
# Jeśli cyfra występuje kilka razy, dodajemy ją tyle razy,
# ile razy występuje w liczbie.
#
# Przykłady:
# f(1027)       -> 0
# f(230335)     -> 9
# f(513553007)  -> 21


def f(number):
    # Zamieniamy liczbę na tekst za pomocą str().
    #
    # Dlaczego?
    # Dzięki temu możemy przechodzić po poszczególnych cyfrach.
    #
    # Przykład:
    # str(230335) -> "230335"
    #
    # Zapisujemy wynik w zmiennej number_text.

    number_text = str(abs(number))

    # abs() usuwa znak minus, jeśli liczba jest ujemna.
    # Dzięki temu sprawdzamy same cyfry liczby.

    # Tworzymy zmienną total, która będzie przechowywać sumę.
    # Początkowo suma wynosi 0.

    total = 0

    # set() tworzy zbiór elementów.
    #
    # Zbiór przechowuje tylko unikalne wartości,
    # czyli nie powtarza tych samych elementów.
    #
    # Przykład:
    # set("230335") może dać zbiór:
    # {"2", "3", "0", "5"}
    #
    # Kolejność elementów w zbiorze nie jest gwarantowana.
    #
    # Dzięki set() każdą cyfrę sprawdzimy tylko jeden raz,
    # nawet jeśli występuje w liczbie kilka razy.

    for digit in set(number_text):

        # Metoda count() zlicza, ile razy dany znak
        # występuje w napisie.
        #
        # Przykład:
        # "230335".count("3") -> 3
        #
        # Sprawdzamy, czy dana cyfra występuje więcej niż raz.
        #
        # > 1 oznacza: większe od 1.

        if number_text.count(digit) > 1:

            # Jeśli cyfra się powtarza, dodajemy ją do sumy.
            #
            # int(digit) zamienia znak na liczbę.
            #
            # Mnożymy cyfrę przez liczbę jej wystąpień.
            #
            # Przykład:
            # Cyfra "3" występuje trzy razy.
            # int("3") * 3 = 9
            #
            # Dzięki temu dodajemy wszystkie wystąpienia
            # powtarzającej się cyfry.

            total += int(digit) * number_text.count(digit)

    # Zwracamy obliczoną sumę.

    return total


if __name__ == "__main__":

    print(f(1027))       # Oczekiwany wynik: 0
    print(f(230335))     # Oczekiwany wynik: 9
    print(f(513553007))  # Oczekiwany wynik: 21

# if __name__ == "__main__": oznacza: wykonaj poniższy kod tylko wtedy, gdy ten plik został uruchomiony bezpośrednio, a nie zaimportowany jako moduł.