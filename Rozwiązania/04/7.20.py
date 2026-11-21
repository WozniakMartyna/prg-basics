# ZADANIE:
# Napisz funkcję f(n), która zwraca n-tą liczbę pierwszą.
#
# Liczba pierwsza to liczba naturalna większa od 1,
# która ma dokładnie dwa dzielniki:
# 1 oraz samą siebie.
#
# Przykłady:
# f(1) -> 2
# f(5) -> 11
#
# Kolejne liczby pierwsze:
# 2, 3, 5, 7, 11, 13, 17, 19, 23...


def f(n):
    # Zmienna prime_count będzie przechowywać,
    # ile liczb pierwszych udało nam się już znaleźć.
    #
    # Zaczynamy od 0, ponieważ nie znaleźliśmy jeszcze żadnej.

    prime_count = 0

    # Zmienna number oznacza aktualnie sprawdzaną liczbę.
    #
    # Zaczynamy od 2, ponieważ 2 jest najmniejszą liczbą pierwszą.
    # Liczba 1 nie jest liczbą pierwszą.

    number = 2

    # Pętla while wykonuje się tak długo,
    # jak długo podany warunek jest prawdziwy.
    #
    # Tutaj działamy, dopóki nie znajdziemy n liczb pierwszych.
    #
    # != oznacza "różne od".
    #
    # Przykład:
    # prime_count != n
    # oznacza, że liczba znalezionych liczb pierwszych
    # jest jeszcze inna niż liczba, której szukamy.

    while prime_count != n:

        # Na początku zakładamy, że aktualna liczba jest pierwsza.
        #
        # is_prime to zmienna logiczna.
        # Może przechowywać True albo False.

        is_prime = True

        # Sprawdzamy, czy number ma dzielnik inny niż 1 i sama liczba.
        #
        # range(2, number) oznacza liczby od 2 do number - 1.
        #
        # Przykład:
        # Jeśli number = 7, sprawdzamy:
        # 2, 3, 4, 5, 6.
        #
        # Jeśli któraś z tych liczb dzieli number bez reszty,
        # to number nie jest liczbą pierwszą.

        for divisor in range(2, number):

            # Operator % zwraca resztę z dzielenia.
            #
            # Jeśli number % divisor == 0,
            # oznacza to, że liczba dzieli się bez reszty.
            #
            # Przykład:
            # 8 % 2 == 0 -> True
            # 8 % 3 == 0 -> False
            #
            # Jeśli znajdziemy taki dzielnik,
            # liczba nie jest pierwsza.

            if number % divisor == 0:

                is_prime = False

                # break natychmiast kończy działanie pętli for.
                #
                # Nie musimy już sprawdzać kolejnych dzielników,
                # ponieważ znaleźliśmy już jeden dzielnik
                # inny niż 1 i sama liczba.

                break

        # Po sprawdzeniu dzielników sprawdzamy,
        # czy liczba nadal jest uznawana za pierwszą.

        if is_prime:

            # Jeśli is_prime == True,
            # zwiększamy licznik znalezionych liczb pierwszych.

            prime_count += 1

        # Przechodzimy do następnej liczby.
        #
        # number += 1 oznacza:
        # number = number + 1

        number += 1

    # Gdy pętla while się zakończy,
    # zmienna number jest już o 1 większa od szukanej liczby.
    #
    # Dlatego zwracamy number - 1.

    return number - 1


if __name__ == "__main__":

    print(f(1))  # Oczekiwany wynik: 2
    print(f(2))  # Oczekiwany wynik: 3
    print(f(3))  # Oczekiwany wynik: 5
    print(f(5))  # Oczekiwany wynik: 11