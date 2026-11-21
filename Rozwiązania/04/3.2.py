# ZADANIE 3.2
# Należy użyć modułu random, aby zasymulować rzut kostką do gry.
# Program ma wylosować jedną liczbę całkowitą od 1 do 6 i wyświetlić wynik.

# import random importuje moduł służący do losowania.
import random

# random.randint(1, 6) losuje liczbę całkowitą od 1 do 6.
# Zarówno 1, jak i 6 mogą zostać wylosowane.
dice_result = random.randint(1, 6)

# print() wyświetla wylosowany wynik.
print('Dice result:', dice_result)

# Zamiast randint(1, 6) można użyć randrange(1, 7).
# randrange() nie uwzględnia górnej granicy,
# dlatego podajemy 7, aby można było wylosować również 6.