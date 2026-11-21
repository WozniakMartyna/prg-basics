# ZADANIE 3.26:
# Rysowanie wykresu funkcji sinus dla kątów od 0 do 360 stopni.

# math zawiera funkcje matematyczne, np. sin() i radians().
import math

# matplotlib służy do tworzenia wykresów.
import matplotlib.pyplot as plt

# Tworzymy listę kątów od 0 do 360 stopni.
# Trzeci argument range() oznacza krok, czyli odstęp między wartościami.
# Tutaj krok wynosi 1 stopień.
degrees = list(range(0, 361, 1))

# Zamieniamy stopnie na radiany.
# Funkcja math.sin() przyjmuje kąty wyrażone w radianach.
radians = [math.radians(angle) for angle in degrees]

# Obliczamy sinus każdego kąta.
y = [math.sin(angle) for angle in radians]

# Rysujemy wykres.
# Na osi X umieszczamy stopnie, a na osi Y wartości sinusa.
plt.plot(degrees, y)

# Dodajemy tytuł i opisy osi.
plt.title("Wykres funkcji y = sin(x)")
plt.xlabel("Kąt w stopniach")
plt.ylabel("sin(x)")

# Ustawiamy zakres osi X od 0 do 360.
plt.xlim(0, 360)

# Dodajemy siatkę.
plt.grid(True)

# Wyświetlamy wykres.
plt.show()

# NOTATKI:
# import math - importuje funkcje matematyczne.
# math.radians() - zamienia stopnie na radiany.
# math.sin() - oblicza sinus kąta podanego w radianach.
# range(0, 361, 1) - tworzy liczby od 0 do 360 co 1.
# Trzeci argument range() określa krok.
# plt.xlim(0, 360) - ustawia widoczny zakres osi X.