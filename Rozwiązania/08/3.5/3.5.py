
# ZADANIE 3.5:
# Program sprawdza, czy nazwa użytkownika i hasło
# spełniają wymagania określone w zadaniu.

import re
# Importujemy moduł re, który umożliwia sprawdzanie tekstu
# za pomocą wyrażeń regularnych (regex).

username = input("Enter username: ")
# input() wyświetla komunikat i czeka na wpisanie tekstu przez użytkownika.
# Wpisana wartość zostaje zapisana w zmiennej username.
# input() zawsze zwraca tekst (string).

password = input("Enter password: ")
# Pobieramy hasło i zapisujemy je w zmiennej password.
# W tym ćwiczeniu hasło nie jest ukrywane podczas wpisywania.

# Wzorzec określający poprawną nazwę użytkownika.
username_pattern = r"[a-z]{6,}"

# Wyjaśnienie wzorca username_pattern:
# r oznacza raw string (surowy tekst), przydatny w regex.
# [a-z] oznacza jedną małą literę od a do z.
# {6,} oznacza co najmniej 6 wystąpień poprzedniego elementu.
# Czyli [a-z]{6,} oznacza minimum 6 małych liter.
# Nie można użyć wielkich liter, cyfr, spacji ani znaków specjalnych.

# Wzorzec określający poprawne hasło.
password_pattern = r"[A-Za-z0-9_]{8,}"

# Wyjaśnienie wzorca password_pattern:
# [A-Za-z0-9_] oznacza jeden znak z dozwolonego zestawu:
# A-Z  - wielkie litery od A do Z,
# a-z  - małe litery od a do z,
# 0-9  - cyfry od 0 do 9,
# _    - znak podkreślenia.
# {8,} oznacza co najmniej 8 znaków.
# W haśle nie mogą pojawić się np. spacje, myślniki ani kropki.

# Sprawdzamy, czy wpisane dane pasują do wzorców.
username_match = re.fullmatch(username_pattern, username)
password_match = re.fullmatch(password_pattern, password)

# re.fullmatch() sprawdza, czy CAŁY wpisany tekst pasuje do wzorca.
# Zwraca obiekt dopasowania, jeśli tekst jest poprawny,
# albo None, jeśli nie pasuje.
#
# Dlaczego fullmatch(), a nie match()?
# match() sprawdza dopasowanie od początku tekstu,
# ale może nie sprawdzić, czy cały tekst jest poprawny.
# fullmatch() wymaga dopasowania całego wpisu.

# Sprawdzamy, czy oba warunki są spełnione.
if username_match and password_match:
    # and oznacza ORAZ.
    # Warunek jest prawdziwy tylko wtedy, gdy username_match
    # i password_match oznaczają poprawne dopasowanie.
    print("Username and password are correct.")

else:
    # else wykonuje się, gdy przynajmniej jeden warunek nie jest spełniony.
    print("Username or password is incorrect.")

    # Sprawdzamy osobno nazwę użytkownika.
    if not username_match:
        # not oznacza zaprzeczenie, czyli "jeśli nie jest poprawne".
        print("Username must contain at least 6 lowercase letters.")

    # Sprawdzamy osobno hasło.
    if not password_match:
        print("Password must contain at least 8 letters, digits or underscores.")
