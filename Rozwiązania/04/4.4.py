# ZADANIE 4.4
# Należy napisać funkcję sum_digits(number),
# która oblicza sumę cyfr podanej liczby całkowitej.
# Liczba może być dodatnia, ujemna lub równa zero.
# Program ma pobrać liczbę od użytkownika i wyświetlić sumę jej cyfr.

# def tworzy funkcję o nazwie sum_digits.
# number jest parametrem, czyli liczbą przekazaną do funkcji.
def sum_digits(number):

    # abs() zwraca wartość bezwzględną liczby.
    # Dzięki temu np. -123 zmieni się na 123.
    number = abs(number)

    # str() zamienia liczbę na tekst.
    # Dzięki temu możemy przechodzić po jej kolejnych cyfrach.
    number_text = str(number)

    # Tworzymy zmienną, w której będziemy przechowywać sumę cyfr.
    total = 0

    # for przechodzi po każdym znaku tekstu po kolei.
    # digit oznacza aktualnie sprawdzany znak.
    for digit in number_text:

        # int() zamienia pojedynczy znak, np. '3', na liczbę 3.
        # Dodajemy tę cyfrę do dotychczasowej sumy.
        total = total + int(digit)

    # Zwracamy obliczoną sumę cyfr.
    return total


# input() pobiera liczbę od użytkownika.
# int() zamienia wpisany tekst na liczbę całkowitą.
number = int(input('Enter an integer: '))

# Wywołujemy funkcję i wyświetlamy wynik.
print('Sum of digits:', sum_digits(number))


# Przykłady:
# Dla 123 wynik wynosi 6, ponieważ 1 + 2 + 3 = 6.
# Dla -456 wynik wynosi 15, ponieważ 4 + 5 + 6 = 15.
# Dla 0 wynik wynosi 0.

# - Po co używamy abs()? Żeby usunąć znak minus z liczby.
# - Po co używamy str()? Żeby móc przechodzić po cyfrach jako znakach.
# - Co robi for? Powtarza instrukcje dla każdego elementu tekstu.
# - Co robi int(digit)? Zamienia znak cyfry na liczbę.
# - Czy można zamiast total = total + int(digit) napisać
#   total += int(digit)? Tak, to krótszy zapis tego samego działania.