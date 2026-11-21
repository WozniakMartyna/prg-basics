# ZADANIE 3.15:
# Odwróć kolejność elementów krotki:
# (10, 20, 30, 40, 50).

# Tworzymy krotkę z pięcioma elementami.
numbers = (10, 20, 30, 40, 50)

# Operator [::-1] odwraca kolejność elementów kolekcji.
# Pierwszy dwukropek oznacza pominięcie początku zakresu.
# Drugi dwukropek oznacza pominięcie końca zakresu.
# -1 oznacza przechodzenie po elementach od końca do początku.
reversed_numbers = numbers[::-1]

# Wyświetlamy oryginalną i odwróconą krotkę.
print("Oryginalna krotka:", numbers)
print("Odwrócona krotka:", reversed_numbers)


# WYNIK:
# Oryginalna krotka: (10, 20, 30, 40, 50)
# Odwrócona krotka: (50, 40, 30, 20, 10)


# NOTATKI:
# Krotka (tuple) jest podobna do listy, ale nie można zmieniać
# jej elementów po utworzeniu.
#
# Listę zapisujemy w nawiasach kwadratowych [].
# Krotkę zapisujemy w nawiasach okrągłych ().
#
# [::-1] to sposób odwracania kolejności elementów.
#
# Jest to przykład wycinania fragmentu kolekcji (slicing).
#
# Co oznacza -1 w zapisie [::-1]?
# Odpowiedź: Oznacza przechodzenie od końca do początku.
#
# Czy można zmienić element istniejącej krotki?
# Odpowiedź: Nie, krotki są niemodyfikowalne.