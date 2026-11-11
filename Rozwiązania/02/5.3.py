# Prostopadłościan ma trzy wymiary: długość, szerokość i wysokość, oznaczone jako a, b i c.
# Wzory:
# Objętość: V = a * b * c
# Pole powierzchni: P = 2(ab + ac + bc)

# A program to calculate the volume and surface area of a cuboid.
# Program oblicza objętość i pole powierzchni prostopadłościanu.

# Pobieramy od użytkownika długość pierwszej krawędzi.
# input() wyświetla pytanie i pobiera odpowiedź jako tekst.
# float() zamienia wpisany tekst na liczbę, która może mieć część dziesiętną.
a = float(input('Enter the length of the first edge a: '))

# Pobieramy długość drugiej krawędzi i zamieniamy ją na liczbę.
b = float(input('Enter the length of the second edge b: '))

# Pobieramy długość trzeciej krawędzi i zamieniamy ją na liczbę.
c = float(input('Enter the length of the third edge c: '))

# Obliczamy objętość prostopadłościanu.
# Wzór: V = a * b * c.
volume = a * b * c

# Obliczamy pole powierzchni całkowitej.
# Wzór: P = 2 * (a*b + a*c + b*c).
# Nawiasy powodują, że najpierw dodajemy pola trzech różnych ścian.
# Następnie mnożymy sumę przez 2, ponieważ każda ściana występuje dwa razy.
surface_area = 2 * (a * b + a * c + b * c)

# Wyświetlamy obliczoną objętość.
# f"..." – tworzy f-string, czyli tekst, w którym można umieszczać wartości zmiennych w nawiasach {}.
# {volume} – wstawia wartość zmiennej do f-stringa.
print(f'The volume of the cuboid is {volume}')

# Wyświetlamy obliczone pole powierzchni.
print(f'The surface area of the cuboid is {surface_area}')

# Przykładowe uruchomienie programu dla: a = 3, b = 4, c = 5
# Objętość = 60,0, Pole powierzchni = 94,0

# Przykładowe uruchomienie programu dla: a = 8, b = 1, c = 2
# Objętość = 16.0, Pole powierzchni = 52.0