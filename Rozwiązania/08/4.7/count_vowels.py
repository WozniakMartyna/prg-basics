# ZADANIE 4.7:
# Liczenie samogłosek w tekście wpisanym przez użytkownika
# za pomocą wyrażeń regularnych (Regex).

import re
# Importujemy moduł re, który pozwala wyszukiwać wzorce w tekście.

text = input("Enter text: ")
# input() pobiera tekst wpisany przez użytkownika.
# Cały wpisany tekst zapisujemy w zmiennej text.

pattern = r"[aeiou]"
# Tworzymy wzorzec Regex.
# Nawiasy kwadratowe [] oznaczają dowolny jeden znak
# spośród znaków znajdujących się wewnątrz.
# [aeiou] oznacza jedną z samogłosek: a, e, i, o lub u.
# Małe litery wystarczą, ponieważ niżej użyjemy re.IGNORECASE.

vowels = re.findall(pattern, text, re.IGNORECASE)
# re.findall() wyszukuje WSZYSTKIE dopasowania do wzorca
# i zwraca je jako listę.
# re.IGNORECASE sprawia, że wielkość liter nie ma znaczenia.
# Znajdzie więc zarówno "a", jak i "A".

print("Number of vowels:", len(vowels))
# len() liczy elementy listy, czyli znalezione samogłoski.