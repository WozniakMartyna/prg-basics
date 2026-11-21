# ZADANIE 10: Wypisywanie elementów pierwszej listy,
# których nie ma w drugiej liście.

# Tworzymy dwie listy.
array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]

# Tworzymy pustą listę na wyniki.
result = []

# Przechodzimy przez wszystkie elementy pierwszej listy.
for number in array1:

    # Operator not in sprawdza, czy elementu NIE ma w drugiej liście.
    if number not in array2:

        # Jeżeli liczby nie ma w drugiej liście, dodajemy ją do wyniku.
        result.append(number)

# Wyświetlamy wynik.
print("Elementy, których nie ma w drugiej liście:", result)

# DODATKOWE NOTATKI:
#
# in - sprawdza, czy element znajduje się w liście.
# not in - sprawdza, czy elementu nie ma w liście.
#
# Przykład:
# 5 in [2, 5, 8] zwróci True.
# 3 not in [2, 5, 8] zwróci True.
#
# append() - dodaje nowy element na końcu listy.
#
# Ważne:
# Program przechodzi po pierwszej liście i sprawdza,
# czy każdy jej element znajduje się w drugiej liście.
# Nie usuwa elementów z żadnej z oryginalnych list.