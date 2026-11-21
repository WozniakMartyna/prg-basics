# ZADANIE 3.21:
# Sprawdzanie, czy pierwsza lista jest podzbiorem drugiej listy.

# Tworzymy dwie przykładowe listy.
array1 = [2, 4, 6]
array2 = [1, 2, 3, 4, 5, 6, 7]

# Zakładamy, że wszystkie elementy pierwszej listy znajdują się w drugiej.
is_subset = True

# Przechodzimy przez wszystkie elementy pierwszej listy.
for number in array1:

    # Sprawdzamy, czy aktualny element znajduje się w drugiej liście.
    if number not in array2:

        # Jeżeli choć jednego elementu brakuje, lista nie jest podzbiorem.
        is_subset = False
        break  # Nie musimy już sprawdzać kolejnych elementów.

# Wyświetlamy wynik.
if is_subset:
    print("Pierwsza lista jest podzbiorem drugiej listy.")
else:
    print("Pierwsza lista nie jest podzbiorem drugiej listy.")

# WYNIK:
# Pierwsza lista jest podzbiorem drugiej listy.
#
# NOTATKI:
# Podzbiór - zbiór elementów, z których każdy znajduje się w drugim zbiorze.
# in - sprawdza, czy element znajduje się w kolekcji.
# not in - sprawdza, czy elementu nie ma w kolekcji.
# break - natychmiast przerywa działanie pętli.
# True - prawda, False - fałsz.
#
# W tym rozwiązaniu sprawdzamy obecność wartości,
# nie liczbę ich powtórzeń.