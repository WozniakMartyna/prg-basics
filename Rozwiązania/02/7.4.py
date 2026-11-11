# Program sprawdza, czy drzewo można ściąć.
# Drzewo można ściąć, jeśli jego średnica wynosi co najmniej 50 cm.

# Importujemy moduł math, który zawiera między innymi stałą pi.
import math

# Pobieramy obwód drzewa w centymetrach.
# input() pobiera wartość jako tekst.
# float() zamienia tekst na liczbę, która może mieć część dziesiętną.
circumference = float(input('Enter tree circumference in cm: '))

# Obliczamy średnicę drzewa.
# Wzór: średnica = obwód / pi.
# math.pi oznacza przybliżoną wartość liczby pi.
diameter = circumference / math.pi

# Sprawdzamy, czy średnica jest większa lub równa 50 cm.
# Operator >= oznacza "większe lub równe".
# Wynik będzie wartością True albo False.
can_cut_down = diameter >= 50

# Wyświetlamy informację, czy drzewo można ściąć.
# F-string pozwala wstawić wartość zmiennej do tekstu za pomocą {}.
print(f'Tree can be cut down: {can_cut_down}')

# Sprawdzanie dla danych obwodów:
# Drzewo 1 - 160 cm - can_cut_down = True
# Drzewo 2 - 90 cm - can_cut_down = False
# Drzewo 3 - 230 cm - can_cut_down = True
# Drzewo 4 - 120 cm - can_cut_down = False