# ZADANIE 09.2.6:
# Sprawdzenie, czy użytkownik ma wszystkie wymagane uprawnienia.

# Zbiór uprawnień wymaganych do wykonania czynności.
required_permissions = {"read", "write", "execute"}

# Zbiór uprawnień, które posiada użytkownik.
user_permissions = {"read", "write"}

# .issubset() sprawdza, czy wszystkie elementy pierwszego zbioru
# znajdują się również w drugim zbiorze.
# Sprawdzamy więc, czy wymagane uprawnienia są częścią uprawnień użytkownika.
has_permissions = required_permissions.issubset(user_permissions)

# Wyświetlamy wynik sprawdzenia.
print(has_permissions)

# required_permissions.issubset(user_permissions) sprawdza, czy wszystkie wymagane uprawnienia znajdują się w zbiorze uprawnień użytkownika.