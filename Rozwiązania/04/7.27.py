# ZADANIE: Sprawdź poprawność czterocyfrowego kodu produktu.
# Czwarta cyfra musi być równa reszcie z dzielenia sumy
# pierwszych trzech cyfr przez 7.

def f(code):
    code = str(code)  # Zamieniamy kod na tekst, aby móc pobierać pojedyncze cyfry.

    # Kod musi mieć dokładnie 4 cyfry i zawierać wyłącznie cyfry.
    if len(code) != 4 or not code.isdigit():
        return False

    # int() zamienia znak cyfry na liczbę całkowitą.
    digit_sum = int(code[0]) + int(code[1]) + int(code[2])

    # % oznacza resztę z dzielenia.
    control_digit = digit_sum % 7

    # Porównujemy obliczoną cyfrę kontrolną z czwartą cyfrą kodu.
    return control_digit == int(code[3])


def main():
    print(f("1082"))  # True: 1 + 0 + 8 = 9, a 9 % 7 = 2.
    print(f("2035"))  # True: 2 + 0 + 3 = 5, a 5 % 7 = 5.
    print(f("1114"))  # False: 1 + 1 + 1 = 3, a 3 % 7 = 3.
    print(f("7071"))  # False: 7 + 0 + 7 = 14, a 14 % 7 = 0.


if __name__ == "__main__":
    main()

# if __name__ == "__main__": oznacza: wykonaj poniższy kod tylko wtedy, gdy ten plik został uruchomiony bezpośrednio, a nie zaimportowany jako moduł.