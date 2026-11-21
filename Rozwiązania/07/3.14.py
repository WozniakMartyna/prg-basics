# ZADANIE 3.14:
# Utwórz krotkę zawierającą jeden element: "computation".
# Wyświetl typ utworzonej zmiennej.

# Tworzymy krotkę zawierającą jeden element.
# Przecinek po wartości jest konieczny, aby Python rozpoznał krotkę.
computation = ("computation",)

# type() sprawdza typ danych przechowywanych w zmiennej.
print("Zawartość:", computation)
print("Typ zmiennej:", type(computation))


# WYNIK:
# Zawartość: ('computation',)
# Typ zmiennej: <class 'tuple'>


# NOTATKI:
# Krotka (tuple) to uporządkowana kolekcja elementów.
# Podobnie jak lista, może zawierać wiele wartości.
#
# Krotkę zapisujemy za pomocą nawiasów okrągłych ().
#
# WAŻNE:
# Jednoelementowa krotka musi zawierać przecinek.
#
# ("computation") - to zwykły tekst w nawiasach.
# ("computation",) - to krotka z jednym elementem.
#
# type() - sprawdza typ danych zmiennej.
#
# Dlaczego po słowie "computation" znajduje się przecinek?
# Odpowiedź: Ponieważ to przecinek, a nie nawias, informuje
# Pythona, że tworzymy krotkę jednoelementową.