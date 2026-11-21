# ZADANIE 4.3
# Należy napisać funkcję triangle_area(a, b, c),
# która oblicza pole trójkąta na podstawie długości jego boków.
# Wykorzystujemy wzór Herona.
# Następnie program ma pobrać trzy boki od użytkownika
# i obliczyć pole, a także sprawdzić trzy przykładowe trójkąty.

# Importujemy moduł math, aby móc użyć funkcji sqrt(),
# która oblicza pierwiastek kwadratowy.
import math

# def tworzy funkcję o nazwie triangle_area.
# a, b, c to parametry, czyli długości boków trójkąta.
def triangle_area(a, b, c):

    # Obliczamy połowę obwodu trójkąta.
    # Jeden znak / oznacza dzielenie.
    s = (a + b + c) / 2

    # Wzór Herona:
    # pole = pierwiastek z s * (s-a) * (s-b) * (s-c).
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    # return zwraca obliczone pole trójkąta.
    return area

# input() pobiera dane wpisane przez użytkownika.
# float() zamienia wpisany tekst na liczbę, która może mieć część dziesiętną.
a = float(input('Enter the first side: '))
b = float(input('Enter the second side: '))
c = float(input('Enter the third side: '))

# Wywołujemy funkcję i wyświetlamy wynik.
print('Triangle area:', triangle_area(a, b, c))

# Dodatkowe przykłady wymagane w zadaniu:
# Dla boków 3, 4, 5 pole powinno wynosić 6.
print('Area for sides 3, 4, 5:', triangle_area(3, 4, 5))

# Dla boków 5, 12, 13 pole powinno wynosić 30.
print('Area for sides 5, 12, 13:', triangle_area(5, 12, 13))

# Dla boków 7, 24, 25 pole powinno wynosić 84.
print('Area for sides 7, 24, 25:', triangle_area(7, 24, 25))

# - Dlaczego używamy math.sqrt()? Ponieważ obliczamy pierwiastek.
# - Co robi return? Zwraca wynik funkcji.
# - Czy można użyć int() zamiast float()? Można, ale int()
#   nie pozwala wprowadzać liczb z częścią dziesiętną.
# - Czy można zmienić nazwy a, b, c? Tak, jeśli zmienimy je
#   konsekwentnie w całej funkcji.