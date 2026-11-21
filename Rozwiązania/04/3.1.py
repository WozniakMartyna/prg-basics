# ZADANIE 3.1
# Należy użyć modułu math, aby:
# 1. Obliczyć pierwiastek kwadratowy z liczby 7.
# 2. Obliczyć logarytm naturalny z liczby 5.
# 3. Obliczyć sinus kąta 90 stopni.

# import math oznacza zaimportowanie modułu matematycznego.
# Moduł zawiera gotowe funkcje do wykonywania obliczeń.
import math

# math.sqrt(7) oblicza pierwiastek kwadratowy z liczby 7.
square_root = math.sqrt(7)
print('Square root of 7:', square_root)

# math.log(5) oblicza logarytm naturalny z liczby 5.
natural_logarithm = math.log(5)
print('Natural logarithm of 5:', natural_logarithm)

# math.sin() oblicza sinus kąta.
# Python wymaga podania kąta w radianach, a nie w stopniach.
# math.radians(90) zamienia 90 stopni na radiany.
sine = math.sin(math.radians(90))
print('Sine of 90 degrees:', sine)

# Można też zamiast math.radians(90) użyć math.pi / 2.
# math.pi oznacza wartość liczby pi.