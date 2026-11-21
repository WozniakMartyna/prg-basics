# ZADANIE 3.25:
# Rysowanie wykresu funkcji f(x) = x^2 - 3.

import matplotlib.pyplot as plt

# Tworzymy listę wartości X od -100 do 100.
# range(-100, 101) kończy się na 101, ale nie obejmuje tej liczby.
x = list(range(-100, 101))

# Dla każdej wartości X obliczamy wartość funkcji.
# Wzór funkcji: f(x) = x^2 - 3.
y = [number ** 2 - 3 for number in x]

# Rysujemy wykres na podstawie list X i Y.
plt.plot(x, y)

# Ustawiamy tytuł i opisy osi.
plt.title("Wykres funkcji f(x) = x^2 - 3")
plt.xlabel("x")
plt.ylabel("f(x)")

# Włączamy siatkę.
plt.grid(True)

# Wyświetlamy wykres.
plt.show()

# NOTATKI:
# list(range(-100, 101)) - tworzy listę liczb od -100 do 100.
# ** 2 - oznacza podniesienie liczby do kwadratu.
# [wyrażenie for element in lista] - tworzy nową listę,
# obliczając wyrażenie dla każdego elementu.
# plt.plot(x, y) - rysuje wykres funkcji.