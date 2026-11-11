# Program sprawdza, czy hasło ma co najmniej 8 znaków.

# Pobieramy hasło od użytkownika.
# input() pobiera wpisany tekst.
password = input('Enter password: ')

# Funkcja len() liczy liczbę znaków w haśle.
# Operator >= sprawdza, czy liczba jest większa lub równa 8.
# Wynik porównania zapisujemy w zmiennej password_ok.
password_ok = len(password) >= 8

# Wyświetlamy informację, czy długość hasła jest prawidłowa.
# F-string pozwala wstawić wartość zmiennej password_ok do tekstu za pomocą nawiasów klamrowych {}.
print(f'Password length is valid: {password_ok}')

# Sprawdzanie haseł:
# university – hasło ma 10 znaków, więc password_ok = True
# peter123 – hasło ma 8 znaków, więc password_ok = True
# seven – hasło ma 5 znaków, więc password_ok = False
# anna333 – hasło ma 7 znaków, więc password_ok = False