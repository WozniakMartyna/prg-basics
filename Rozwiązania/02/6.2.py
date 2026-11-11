# Program ma wyświetlić pierwszą literę imienia i pierwszą literę nazwiska.

# Program wyświetla inicjały imienia i nazwiska.

# Zapisujemy imię w zmiennej name.
name = 'Martyna'

# Zapisujemy nazwisko w zmiennej surname.
surname = 'Wozniak'

# Indeksowanie pozwala odczytać pojedynczy znak z tekstu.
# Indeksowanie zaczyna się od 0.
# name[0] oznacza pierwszy znak imienia.
# [] pobiera znak z tekstu na podstawie jego indeksu.
first_initial = name[0]

# surname[0] oznacza pierwszy znak nazwiska.
last_initial = surname[0]

# Wyświetlamy inicjały.
# F-string pozwala wstawić wartości zmiennych do tekstu za pomocą {}.
print(f'My initials are: {first_initial}{last_initial}')