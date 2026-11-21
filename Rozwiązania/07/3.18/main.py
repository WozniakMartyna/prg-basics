# ZADANIE 3.18:
# Testowanie funkcji z własnego modułu MyArrays.

# import pozwala korzystać z funkcji zapisanych w innym pliku Python.
import MyArrays

# Tworzymy listę z liczbami podanymi w poleceniu.
numbers = [7, 3, 8, 5, 2]

# Wywołujemy funkcje zapisane w module MyArrays.
print("Drugi największy element:", MyArrays.second_largest(numbers))
print("Różnica maksimum i minimum:", MyArrays.difference(numbers))
print("Mediana:", MyArrays.median(numbers))
print("Minimum i maksimum:", MyArrays.min_max(numbers))
print("Elementy jako tekst:", MyArrays.as_string(numbers))

# Funkcje wywołujemy przez nazwę modułu, kropkę i nazwę funkcji.
# Przykład: MyArrays.median(numbers)