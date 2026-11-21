
# ZADANIE 3.17:
# Policz, ile razy podana wartość występuje w krotce.

# Tworzymy krotkę z liczbami.
numbers = (50, 20, 40, 50, 30, 50)

# Określamy wartość, której wystąpienia chcemy policzyć.
search_number = 50

# Metoda count() zlicza wystąpienia podanej wartości w krotce.
count = numbers.count(search_number)

# Wyświetlamy liczbę wystąpień.
print("Liczba", search_number, "występuje", count, "razy.")


# WYNIK:
# Liczba 50 występuje 3 razy.


# NOTATKI:
# count() - metoda dostępna zarówno dla list, jak i krotek.
# Zwraca liczbę wystąpień wskazanej wartości.
#
# Przykład:
# (1, 2, 2, 3).count(2) zwróci 2.
#
# Krotka jest niemodyfikowalna, ale można sprawdzać jej elementy,
# odczytywać je oraz liczyć ich wystąpienia.
#
# Czy count() zmienia zawartość krotki?
# Odpowiedź: Nie, tylko zlicza wystąpienia wartości.
#
# Ile razy występuje 50 w naszej krotce?
# Odpowiedź: Trzy razy.