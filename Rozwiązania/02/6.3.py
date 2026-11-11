# Program ma wyświetlić skrót nazwy Krakow University of Economics, czyli KUE.

# Program wyświetla skrót nazwy uczelni.

# Zapisujemy pełną nazwę uczelni w zmiennej university.
university = "Krakow University of Economics"

# Pobieramy pierwszą literę każdego wyrazu.
# [] pobiera znak z tekstu na podstawie jego indeksu.
# Indeks [0] oznacza pierwszą literę wyrazu Krakow.
# Indeks [7] oznacza literę U, od której zaczyna się University.
# Indeks [21] oznacza literę E, od której zaczyna się Economics.
abbreviation = university[0] + university[7] + university[21]

# Wyświetlamy utworzony skrót.
# F-string pozwala wstawić wartość zmiennej abbreviation do tekstu.
print(f'University abbreviation: {abbreviation}')