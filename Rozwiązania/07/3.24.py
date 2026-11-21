# ZADANIE 3.24:
# Rysowanie odcinka łączącego punkty (1, 3) oraz (8, 10).

# Importujemy bibliotekę matplotlib do tworzenia wykresów.
import matplotlib.pyplot as plt

# Współrzędne X obu punktów.
x = [1, 8]

# Współrzędne Y obu punktów.
y = [3, 10]

# plot() rysuje linię na podstawie podanych współrzędnych.
# Pierwsza lista zawiera wartości X, druga wartości Y.
plt.plot(x, y)

# Dodajemy tytuł wykresu.
plt.title("Odcinek między dwoma punktami")

# Opisujemy osie wykresu.
plt.xlabel("Oś X")
plt.ylabel("Oś Y")

# Dodajemy siatkę, aby łatwiej odczytywać wartości.
plt.grid(True)

# show() wyświetla gotowy wykres w osobnym oknie.
plt.show()

# NOTATKI:
# plt.plot(x, y) - rysuje linię łączącą punkty.
# plt.title() - ustawia tytuł wykresu.
# plt.xlabel() i plt.ylabel() - opisują osie.
# plt.grid(True) - włącza siatkę.
# plt.show() - wyświetla wykres.