# Program ma wykonać trzy losowe rzuty kostką, wyświetlić każdy wynik oraz obliczyć ich sumę.

# Importujemy moduł random, który umożliwia losowanie liczb.
import random

# Losujemy wynik pierwszego rzutu kostką.
# randint(1, 6) losuje liczbę całkowitą od 1 do 6.
# random.randint() oznacza wywołanie funkcji randint() znajdującej się w module random.
dice_roll_1 = random.randint(1, 6)

# Losujemy wynik drugiego rzutu kostką.
dice_roll_2 = random.randint(1, 6)

# Losujemy wynik trzeciego rzutu kostką.
dice_roll_3 = random.randint(1, 6)

# Obliczamy sumę trzech wyników.
# Operator + dodaje do siebie liczby.
total = dice_roll_1 + dice_roll_2 + dice_roll_3

# Wyświetlamy wynik pierwszego rzutu.
# print() wyświetla tekst i wartość zmiennej.
print('First roll:', dice_roll_1)

# Wyświetlamy wynik drugiego rzutu.
print('Second roll:', dice_roll_2)

# Wyświetlamy wynik trzeciego rzutu.
print('Third roll:', dice_roll_3)

# Wyświetlamy sumę wszystkich trzech rzutów.
print('Total:', total)