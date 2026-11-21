# ZADANIE 3.22:
# Losowanie jednego elementu z listy.

# Importujemy moduł random, który umożliwia wykonywanie losowań.
import random

# Definiujemy funkcję przyjmującą listę jako argument.
def rand_elem(array):

    # random.choice() losowo wybiera jeden element z listy.
    return random.choice(array)


# Tworzymy przykładową listę.
numbers = [10, 20, 30, 40, 50]

# Kilka razy wywołujemy funkcję, aby zobaczyć różne losowania.
print("Pierwsze losowanie:", rand_elem(numbers))
print("Drugie losowanie:", rand_elem(numbers))
print("Trzecie losowanie:", rand_elem(numbers))
print("Czwarte losowanie:", rand_elem(numbers))
print("Piąte losowanie:", rand_elem(numbers))

# PRZYKŁADOWY WYNIK:
# Pierwsze losowanie: 30
# Drugie losowanie: 10
# Trzecie losowanie: 50
# Czwarte losowanie: 30
# Piąte losowanie: 40
#
# Wyniki mogą być inne przy każdym uruchomieniu programu.
#
# NOTATKI:
# import random - importuje bibliotekę do losowania.
# random.choice(array) - wybiera losowy element z listy.
# return - zwraca wylosowany element.
#
# Ważne: lista przekazana do random.choice() nie może być pusta.