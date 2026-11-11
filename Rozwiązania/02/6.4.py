# Z podanego opisu pracownika program ma wyodrębnić imię, nazwisko, datę urodzenia i inicjały.

# Program wyświetla szczegółowe informacje o pracowniku.

# Zapisujemy cały opis pracownika w jednej zmiennej.
employee = "Mr. John May, born on 1998-02-16"

# Wycinamy imię z tekstu.
# employee[4:8] pobiera znaki od indeksu 4 do indeksu 7.
# Indeks końcowy 8 nie jest wliczany.
name = employee[4:8]

# Wycinamy nazwisko z tekstu.
# employee[9:12] pobiera znaki od indeksu 9 do indeksu 11.
surname = employee[9:12]

# Wycinamy datę urodzenia.
# employee[22:] pobiera tekst od indeksu 22 aż do końca.
birth_date = employee[22:]

# Pobieramy pierwszą literę imienia i nazwiska.
# name[0] oznacza pierwszą literę imienia.
# surname[0] oznacza pierwszą literę nazwiska.
initials = name[0] + surname[0]

# Wyświetlamy imię.
# F-string pozwala wstawiać wartości zmiennych do tekstu za pomocą {}.
print(f'Name: {name}')

# Wyświetlamy nazwisko.
print(f'Surname: {surname}')

# Wyświetlamy datę urodzenia.
print(f'Born: {birth_date}')

# Wyświetlamy inicjały.
print(f'Initials: {initials}')