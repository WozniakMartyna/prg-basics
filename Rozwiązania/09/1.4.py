# ZADANIE 1.4:
# Wykonywanie różnych operacji na słowniku opisującym osobę.

# Słownik zawiera sześć par klucz-wartość.
# Wartości mają różne typy:
# str - tekst, int - liczba całkowita,
# list - lista, bool - wartość logiczna,
# dict - kolejny słownik.
person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming", "excursions"],
    "married": True,
    "phone": {
        "landline": "123444321",
        "mobile": "777888999"
    }
}

# 1. Wyświetlenie imienia.
print("Name:", person["name"])

# 2. Wyświetlenie listy zainteresowań.
print("Hobby:", person["hobby"])

# 3. Wyświetlenie całego słownika.
print("Person:", person)

# 4. Zmiana istniejącej wartości.
# Przypisanie nowej wartości do istniejącego klucza.
person["surname"] = "Nowak"

# 5. Zmiana stanu cywilnego.
# True oznacza prawdę, False oznacza fałsz.
person["married"] = False

# 6. Dodanie nowej pary klucz-wartość.
# Jeśli klucz nie istnieje, Python automatycznie go utworzy.
person["gender"] = "male"

# 7. Dodanie nowego hobby do istniejącej listy.
# .append() dodaje element na koniec listy.
person["hobby"].append("bicycle")

# 8. Dodanie numeru telefonu do zagnieżdżonego słownika.
person["phone"]["work"] = "313131444"

# 9. Ponowne wyświetlenie całego słownika.
# .items() pozwala przejść po wszystkich parach klucz-wartość.
print("\nUpdated person:")
for key, value in person.items():
    print(f"{key}: {value}")


# person["name"] – pobiera wartość przypisaną do klucza name.
# person["surname"] = "Nowak" – zmienia wartość istniejącego klucza.
# person["gender"] = "male" – dodaje nowy klucz i wartość.
# .append() – dodaje element do listy.
# person["phone"]["work"] – odwołuje się do słownika znajdującego się wewnątrz innego słownika.
# True i False – wartości logiczne typu bool.