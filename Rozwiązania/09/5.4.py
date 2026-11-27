# ZADANIE 5.4:
# Obliczenie łącznej liczby godzin zajęć w semestrze zimowym.

# Słownik zawiera nazwy przedmiotów i liczbę godzin.
winter_semester = {
    "math": 60,
    "programming": 30,
    "history": 15
}

# Zmienna przechowująca sumę godzin.
total_hours = 0

# items() pozwala pobierać jednocześnie nazwę przedmiotu i liczbę godzin.
for course, hours in winter_semester.items():
    total_hours += hours  # Dodajemy godziny kolejnych przedmiotów.

print("The total number of hours in the winter semester is", total_hours)

# items() – zwraca pary klucz-wartość.
# total_hours += hours – dodaje kolejną wartość do sumy.
# for – przechodzi po wszystkich przedmiotach.