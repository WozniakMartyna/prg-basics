# Program symuluje pięć rzutów kostką.

# Importujemy moduł random, który pozwala losować liczby.
import random

# Wyświetlamy tytuł programu.
print("Dice rolling simulator")


# Pętla for powtarza określone instrukcje.
# range(5) – funkcja tworząca zakres pięciu powtórzeń.
# i - zmienna, która przyjmuje kolejne wartości w czasie działania pętli.
for i in range(5):


    # Losujemy liczbę całkowitą od 1 do 6.
    # randint(1, 6) losuje liczbę z tego zakresu, włącznie z 1 i 6.
    dice_roll = random.randint(1,6)


    # Wyświetlamy wylosowaną liczbę.
    # end=" " sprawia, że kolejne wyniki są wyświetlane w tym samym wierszu, oddzielone spacją.
    print(dice_roll, end=" ")