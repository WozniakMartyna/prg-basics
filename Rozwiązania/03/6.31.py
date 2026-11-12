# Wyświetlanie 20 losowych liczb całkowitych z zakresu od 5 do 10

import random  # Importujemy moduł random, który umożliwia losowanie liczb

for i in range(20):  # Pętla wykona się 20 razy; range(20) oznacza wartości od 0 do 19
    number = random.randint(5, 10)  # Losujemy liczbę całkowitą od 5 do 10, razem z obiema granicami
    print(number)  # Wyświetlamy wylosowaną liczbę