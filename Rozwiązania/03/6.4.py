# W tym zadaniu sprawdzamy, czy hasło podane przez użytkownika ma co najmniej 12 znaków.

new_password = input('Enter new password: ')

# Funkcja len() zwraca liczbę znaków w tekście.
# Jeżeli długość hasła jest mniejsza niż 12, wyświetlamy komunikat o błędzie.
if len(new_password) < 12:
    print('Password too short (min. 12 chars)')
else:
    # else wykonuje się wtedy, gdy warunek if jest fałszywy,
    # czyli hasło ma co najmniej 12 znaków.
    print('Password length is sufficient')

# Warto pamiętać, że spacje również są liczone jako znaki przez len().