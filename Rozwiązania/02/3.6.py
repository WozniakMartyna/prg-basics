# W zadaniu korzystamy ze wzoru:
# d = 3.57 * \sqrt{h}
# Gdzie:
# d – odległość do horyzontu w kilometrach.
# h – wysokość obserwatora w metrach.
# Program ma zapytać użytkownika o wysokość podaną w metrach. Następnie obliczy odległość do horyzontu.

# A program that calculates the distance to the horizon.
# Program oblicza odległość do horyzontu.

# Importujemy moduł math, aby móc obliczyć pierwiastek.
import math

# Pytamy użytkownika o wysokość w metrach.
# input() pobiera wpisaną przez użytkownika wartość jako tekst.
height = input("Enter your height in meters: ")

# Zamieniamy wpisany tekst na liczbę zmiennoprzecinkową.
# float() pozwala podać również wysokość z częścią dziesiętną.
height = float(height)

# Obliczamy odległość do horyzontu według podanego wzoru.
# math.sqrt(height) oblicza pierwiastek z wysokości.
distance = 3.57 * math.sqrt(height)

# Zaokrąglamy wynik do dwóch miejsc po przecinku.
distance = round(distance, 2)

# Wyświetlamy odległość do horyzontu w kilometrach.
print("Distance to the horizon:", distance, "km")

# Przykład 1: Wpisuję swój wzrost (1.73 m). Wynik wynosi 4.70 km.
# Przykład 2: Okno hotelowe jest na wysokości 20 metrów. Wynik wynosi 15.97 km.