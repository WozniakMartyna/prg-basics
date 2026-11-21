# ZADANIE 5.2:
# Program testujący funkcje z modułu converters.
# Sprawdzamy wszystkie cztery funkcje.

# import converters oznacza, że dołączamy moduł converters.
# Python szuka pliku converters.py w tym samym folderze
# co ten program (oraz w dostępnych ścieżkach importowania).
import converters


# Wyświetlamy nagłówek programu testującego.
print('### Test converters')


# TEST 1: metry na centymetry.

# converters.m_to_cm oznacza, że korzystamy z funkcji
# m_to_cm znajdującej się w module converters.
# Liczba 3 jest argumentem przekazywanym do funkcji.
# Oczekiwany wynik: 300 cm.
print(f'Three meters is {converters.m_to_cm(3)} cm')


# TEST 2: centymetry na metry.

# Przekazujemy do funkcji liczbę 250.
# Oczekiwany wynik: 2.5 m.
print(f'250 centimeters is {converters.cm_to_m(250)} meters')


# TEST 3: centymetry na cale.

# Przekazujemy do funkcji liczbę 10.
# Oczekiwany wynik to około 3.94 cala.
# :.2f oznacza wyświetlenie wyniku z dwoma miejscami po przecinku.
print(f'10 centimeters is {converters.cm_to_inches(10):.2f} inches')


# TEST 4: stopy i cale na centymetry.

# Przekazujemy dwa argumenty:
# 5 - liczba stóp,
# 6 - liczba dodatkowych cali.
# Oczekiwany wynik: 167.64 cm.
print(f'5 feet and 6 inches is {converters.feet_and_inches_to_cm(5, 6):.2f} cm')


# WAŻNE NOTATKI:

# import - dołącza inny moduł do programu.
# converters - nazwa importowanego modułu.
# Kropka w converters.m_to_cm oznacza dostęp do funkcji
# znajdującej się wewnątrz modułu converters.
#
# Funkcja - fragment kodu wykonujący określone zadanie.
# Parametr - zmienna wpisana w nawiasach podczas definiowania funkcji.
# Argument - konkretna wartość przekazana do funkcji podczas jej wywołania.
# return - zwraca wynik funkcji.
# print() - wyświetla tekst lub wynik w konsoli.
#
# f przed cudzysłowem oznacza f-string.
# Pozwala wstawiać wartości i wyniki do tekstu za pomocą {}.
#
# :.2f - wyświetla liczbę z dokładnością do dwóch miejsc po przecinku.
# * oznacza mnożenie, / dzielenie, a + dodawanie.