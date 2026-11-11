# W tym zadaniu użytkownik wpisuje imię i nazwisko. Program zapisuje je w dwóch osobnych zmiennych, a następnie łączy w pełne imię i nazwisko.

# A program that reads first and last name from the keyboard.
# Program pobiera imię i nazwisko z klawiatury.

# Pytamy użytkownika o imię.
# input() pobiera wpisany tekst i zapisuje go jako string (str).
first_name = input('Enter your first name: ')

# Pytamy użytkownika o nazwisko.
last_name = input('Enter your last name: ')

# Łączymy imię, spację i nazwisko w jeden tekst.
full_name = first_name + ' ' + last_name

# Wyświetlamy imię i nazwisko osobno.
# f"..." – tworzy f-string, czyli tekst, w którym można umieszczać wartości zmiennych w nawiasach {}.
# {first_name}, {last_name} – wstawiają wartości zmiennych do f-stringa.
print(f'Your first name is {first_name} and your last name is {last_name}')

# Wyświetlamy pełne imię i nazwisko.
print(f'And your full name is {full_name}')