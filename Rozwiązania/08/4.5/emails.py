# ZADANIE 4.5:
# Odczytywanie nadawcy, odbiorcy, tematu i treści wiadomości e-mail.
# Funkcje znajdują się w osobnym module emails.py.

import re
# Importujemy moduł re, który umożliwia wyszukiwanie tekstu
# za pomocą wyrażeń regularnych (Regex).


def read_email():
    # Otwieramy plik email.txt i odczytujemy całą jego zawartość.

    with open("email.txt", "r", encoding="utf-8") as file:
        email = file.read()
        # read() pobiera cały tekst z pliku jako jeden string.

    return email
    # Zwracamy odczytaną wiadomość, aby inne funkcje mogły z niej korzystać.


def email_sender():
    # Pobieramy adres e-mail nadawcy z linii zaczynającej się od From:.

    email = read_email()

    result = re.search(
        r"^From:.*<([^<>]+)>",
        email,
        re.MULTILINE
    )
    # ^From: - szukamy linii zaczynającej się od From:
    # .*     - pomijamy imię i nazwisko oraz inne znaki przed adresem.
    # <      - szukamy znaku otwierającego nawias adresu.
    # ([^<>]+) - zapisujemy do grupy 1 tekst, który nie zawiera < ani >.
    # >      - szukamy zamykającego nawiasu.
    # re.MULTILINE - pozwala szukać From: na początku każdej linii.

    if result:
        return result.group(1)
        # group(1) zwraca sam adres e-mail znaleziony w nawiasach.
    else:
        return "Sender not found"


def email_recipient():
    # Pobieramy adres e-mail odbiorcy z linii zaczynającej się od To:.

    email = read_email()

    result = re.search(
        r"^To:.*<([^<>]+)>",
        email,
        re.MULTILINE
    )
    # Wzorzec działa tak samo jak przy nadawcy,
    # ale tym razem szukamy linii rozpoczynającej się od To:.

    if result:
        return result.group(1)
    else:
        return "Recipient not found"


def email_subject():
    # Pobieramy temat wiadomości z linii Subject:.

    email = read_email()

    result = re.search(
        r"^Subject:\s*(.+)$",
        email,
        re.MULTILINE
    )
    # ^Subject: - szukamy linii rozpoczynającej się od Subject:
    # \s*       - pomijamy spacje po dwukropku.
    # (.+)      - przechwytujemy temat wiadomości.
    # $         - oznacza koniec linii.

    if result:
        return result.group(1).strip()
    else:
        return "Subject not found"


def email_body():
    # Pobieramy treść wiadomości, która znajduje się po pustej linii.

    email = read_email()

    result = re.search(
        r"\r?\n\r?\n(.*)",
        email,
        re.DOTALL
    )
    # \r?\n - znak końca linii; obsługuje różne systemy.
    # Dwa takie znaki obok siebie oznaczają pustą linię.
    # (.*)  - przechwytujemy całą treść po pustej linii.
    # re.DOTALL - kropka dopasowuje również znaki nowej linii.

    if result:
        return result.group(1).strip()
        # Zwracamy całą treść wiadomości bez zbędnych znaków
        # na początku i na końcu.
    else:
        return "Email body not found"