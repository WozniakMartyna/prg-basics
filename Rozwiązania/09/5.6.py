# ZADANIE 5.6:
# Połączenie dwóch słowników w jeden słownik person.

basic_data = {
    "name": "Barbara",
    "age": 21
}

advanced_data = {
    "status": "student",
    "married": False,
    "interest": ["reading", "swimming"]
}

# Tworzymy nowy słownik, łącząc dane z obu słowników.
# Operator ** rozpakowuje zawartość słownika.
person = {**basic_data, **advanced_data}

# Wyświetlamy wszystkie pary klucz-wartość.
for key, value in person.items():
    print(key, ":", value)


# {**basic_data, **advanced_data} – tworzy nowy słownik z elementów obu słowników.
# False – wartość logiczna oznaczająca fałsz.
# Lista może być wartością w słowniku, np. "interest": ["reading", "swimming"].