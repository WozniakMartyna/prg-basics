# ZADANIE: WPROWADZENIE
# Tworzenie i wyświetlanie tablic (list) jednowymiarowych i dwuwymiarowych.

# Biblioteka random pozwala losować liczby.
import random


# --------------------------------------------------
# 1. PODSTAWOWE TWORZENIE LIST
# --------------------------------------------------

# Zwykła lista zawierająca pięć elementów.
arr1 = [3, 7, 1, 0, 4]

# Lista dwuwymiarowa, czyli lista zawierająca inne listy.
arr2 = [[2, 3], [7, 1], [0, 4]]


# --------------------------------------------------
# 2. TWORZENIE LIST ZA POMOCĄ LIST COMPREHENSION
# --------------------------------------------------

# range(5) generuje liczby od 0 do 4.
# Dla każdej z nich tworzymy element o wartości 7.
arr3 = [7 for i in range(5)]

# range(1, 10) generuje liczby od 1 do 9.
# Wartość końcowa 10 nie jest uwzględniana.
arr4 = [i for i in range(1, 10)]

# Każdą liczbę od 1 do 9 mnożymy przez 2.
arr5 = [i * 2 for i in range(1, 10)]


# --------------------------------------------------
# 3. LISTY Z LOSOWYMI LICZBAMI
# --------------------------------------------------

# random.randint(1, 20) losuje liczbę całkowitą od 1 do 20.
# Losujemy osobną liczbę dla każdego z 10 elementów.
arr6 = [random.randint(1, 20) for i in range(10)]


# --------------------------------------------------
# 4. LISTY DWUWYMIAROWE
# --------------------------------------------------

# Tworzymy 5 osobnych pustych list.
arr7 = [[] for i in range(5)]

# Tworzymy 4 wiersze, a w każdym wierszu 2 elementy o wartości 1.
arr8 = [[1 for i in range(2)] for j in range(4)]

# Tworzymy 5 wierszy i 3 kolumny.
# Każdy element otrzymuje losową liczbę od 1 do 20.
arr9 = [[random.randint(1, 20) for i in range(3)] for j in range(5)]


# --------------------------------------------------
# 5. DODATKOWE LISTY Z POLECENIA
# --------------------------------------------------

# Lista zawierająca dokładnie trzy podane wartości.
arr10 = [4, 0, 3]

# Lista 15-elementowa wypełniona zerami.
# Operator * powiela element listy 15 razy.
arr11 = [0] * 15

# Lista liczb całkowitych z zakresu od 1 do 30.
# range(1, 31) kończy się na 30, ponieważ 31 nie jest uwzględniane.
arr12 = [i for i in range(1, 31)]

# Lista 20-elementowa wypełniona losowo zerami lub jedynkami.
# randint(0, 1) może zwrócić 0 albo 1.
arr13 = [random.randint(0, 1) for i in range(20)]

# Lista dwuwymiarowa: 5 wierszy i 2 kolumny.
# Każdy element ma wartość False.
arr14 = [[False for i in range(2)] for j in range(5)]


# --------------------------------------------------
# 6. WYŚWIETLANIE WSZYSTKICH LIST
# --------------------------------------------------

# Tworzymy listę zawierającą wszystkie nasze listy.
# Dzięki temu możemy wyświetlić je w jednej pętli.
all_arrays = [
    arr1, arr2, arr3, arr4, arr5,
    arr6, arr7, arr8, arr9, arr10,
    arr11, arr12, arr13, arr14
]

# enumerate() pozwala pobrać jednocześnie numer i wartość elementu.
# start=1 sprawia, że numerowanie zaczyna się od 1.
for number, array in enumerate(all_arrays, start=1):
    print(f"arr{number} = {array}")