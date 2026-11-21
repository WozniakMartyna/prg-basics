# ZADANIE 3.16:
# Dla krotki ("Seven", [10, 20, 30], (5, 15, 25))
# wyświetl tekst "Seven" oraz liczbę 30.

# Tworzymy krotkę zawierającą trzy elementy:
# 1. Tekst "Seven".
# 2. Listę z trzema liczbami.
# 3. Drugą krotkę z trzema liczbami.
data = ("Seven", [10, 20, 30], (5, 15, 25))

# Indeksy elementów krotki zaczynają się od 0.
# data[0] oznacza pierwszy element, czyli tekst "Seven".
print(data[0])

# data[1] oznacza drugi element, czyli listę [10, 20, 30].
# [2] oznacza trzeci element tej listy, czyli liczbę 30.
print(data[1][2])


# WYNIK:
# Seven
# 30


# NOTATKI:
# Indeksowanie pozwala odczytać konkretny element kolekcji.
#
# data[0] - pierwszy element krotki.
# data[1] - drugi element krotki.
# data[2] - trzeci element krotki.
#
# data[1][2] - najpierw pobieramy drugi element krotki,
# a następnie trzeci element znajdującej się tam listy.
#
# Indeksy w Pythonie zaczynają się od 0:
# 0 - pierwszy element,
# 1 - drugi element,
# 2 - trzeci element.
#
# WAŻNE:
# Krotka może zawierać inne kolekcje, np. listy i kolejne krotki.
#
# Co oznacza zapis data[1][2]?
# Odpowiedź: Pobieramy trzeci element listy znajdującej się
# na drugiej pozycji w krotce.