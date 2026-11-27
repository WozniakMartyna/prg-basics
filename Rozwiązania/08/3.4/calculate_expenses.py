# ZADANIE 3.4:
# Program odczytuje raport zakupów z pliku tekstowego,
# wyszukuje w nim kwoty pieniędzy i oblicza ich łączną wartość.

import re
# import oznacza dołączenie modułu do programu.
# re to wbudowany moduł Pythona obsługujący wyrażenia regularne (regex).
# Regex pozwala wyszukiwać w tekście określone wzorce, np. kwoty pieniędzy.

email_file = "report.txt"
# Nazwa pliku, z którego będziemy odczytywać raport.
# Plik musi znajdować się w tym samym folderze co program .py,
# jeśli uruchamiamy program z tego folderu.

with open(email_file, "r", encoding="utf-8") as file:
    # open() otwiera plik.
    # "r" oznacza tryb odczytu (read).
    # encoding="utf-8" pozwala poprawnie odczytać znaki specjalne,
    # np. symbol euro (€), polskie litery i inne znaki.
    # with automatycznie zamyka plik po zakończeniu pracy z nim.
    # file to zmienna reprezentująca otwarty plik.

    email = file.read()
    # read() odczytuje CAŁĄ zawartość pliku.
    # Wynik zapisujemy w zmiennej email jako jeden długi tekst (string).

# Wzorzec wyszukujący kwoty zapisane np. jako:
# 15.50 €    15,50 €    €15.50    €15
pattern = r"(?:€\s*\d+(?:[.,]\d{1,2})?|\d+(?:[.,]\d{1,2})?\s*€)"

# Wyjaśnienie wzorca:
# r przed tekstem oznacza raw string, czyli surowy tekst.
# Jest przydatny w regex, ponieważ backslash (\) ma tam specjalne znaczenie.
#
# (?: ... | ... ) oznacza dwie możliwe postacie kwoty:
# pierwsza: €15.50 lub € 15.50
# druga:   15.50 € lub 15,50 €
#
# €       - symbol euro.
# \s*     - zero lub więcej białych znaków, np. spacji.
# \d+     - jedna lub więcej cyfr.
# [.,]    - kropka LUB przecinek.
# \d{1,2} - jedna lub dwie cyfry po separatorze dziesiętnym.
# ?       - poprzedni element jest opcjonalny.
# |       - oznacza LUB, czyli alternatywę.

amounts = re.findall(pattern, email)
# re.findall() wyszukuje WSZYSTKIE fragmenty tekstu pasujące do wzorca.
# Zwraca listę znalezionych fragmentów.
# Przykład: ["15.50 €", "20 €", "€8.99"].
# Pierwszy argument to wzorzec, drugi to tekst, w którym szukamy.

total = 0.0
# Zmienna przechowująca sumę wszystkich zakupów.
# 0.0 oznacza liczbę typu float, czyli liczbę z częścią dziesiętną.

for amount in amounts:
    # Pętla for przechodzi kolejno przez każdy znaleziony fragment.
    # amount oznacza aktualnie przetwarzaną kwotę.

    amount = amount.replace("€", "")
    # replace() zamienia wskazany fragment tekstu na inny.
    # Tutaj usuwamy symbol euro, ponieważ nie da się go zamienić bezpośrednio na liczbę.

    amount = amount.strip()
    # strip() usuwa niepotrzebne spacje z początku i końca tekstu.

    amount = amount.replace(",", ".")
    # Python używa kropki jako separatora dziesiętnego.
    # Dlatego zamieniamy przecinek na kropkę, np. "15,50" na "15.50".

    total += float(amount)
    # float() zamienia tekst na liczbę dziesiętną.
    # Np. float("15.50") daje liczbę 15.5.
    # += oznacza: dodaj prawą wartość do aktualnej wartości zmiennej total.
    # Czyli każda kolejna kwota jest dodawana do poprzedniej sumy.

print(f"Total amount spent: {total:.2f} €")
# print() wyświetla wynik.
# f przed tekstem pozwala umieszczać wartości zmiennych w nawiasach {}.
# :.2f oznacza wyświetlenie liczby z dokładnością do dwóch miejsc po przecinku.

# do terminala:
# cd "Rozwiązania/08/3.4"
# python calculate_expenses.py