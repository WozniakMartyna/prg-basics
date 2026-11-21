# ZADANIE:
# Napisz funkcję f(password), która sprawdza, czy hasło:
# 1. Ma co najmniej 6 znaków.
# 2. Nie zawiera powtarzających się znaków.
#
# Przykłady:
# f("ax15")      -> False
# f("book123")   -> False
# f("A2water3")  -> True
# f("qwerty")    -> True
# f("")          -> False


def f(password):
    # len() zwraca liczbę znaków w haśle.
    # >= 6 oznacza: co najmniej 6 znaków.
    #
    # set() tworzy zbiór unikalnych znaków, czyli usuwa powtórzenia.
    # Jeśli długość zbioru jest taka sama jak długość hasła,
    # oznacza to, że żaden znak się nie powtarza.
    #
    # and oznacza, że oba warunki muszą być spełnione.

    return len(password) >= 6 and len(set(password)) == len(password)


if __name__ == "__main__":
    print(f("ax15"))      # False – hasło jest za krótkie.
    print(f("book123"))   # False – litera "o" się powtarza.
    print(f("A2water3"))  # True – 8 znaków, bez powtórzeń.
    print(f("qwerty"))    # True – 6 znaków, bez powtórzeń.
    print(f(""))          # False – pusty tekst.