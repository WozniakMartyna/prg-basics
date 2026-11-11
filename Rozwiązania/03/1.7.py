# Podstawowa pensja pracownika wynosi 5000 zł. Pracownik może otrzymać premię w wysokości określonego procentu pensji.
# Program oblicza wynagrodzenie pracownika z uwzględnieniem premii.

basic_salary = 5000  # Podstawowa pensja pracownika wynosi 5000 zł.
total_salary = 0  # Na początku całkowite wynagrodzenie wynosi 0 zł.
bonus = 0.30  # Premia wynosi 30%, czyli 0.30.

# input() pobiera odpowiedź użytkownika.
# == sprawdza, czy wpisany tekst jest równy literze 'Y'.
# Wynikiem porównania jest True albo False.
is_bonus = input('Does the employee receive a bonus? (Y/N): ') == 'Y'

# Jeśli pracownik otrzymuje premię, dodajemy ją do pensji podstawowej.
if is_bonus:
    total_salary = basic_salary + basic_salary * bonus
else:
    # Jeśli pracownik nie otrzymuje premii, jego pensja pozostaje podstawowa.
    total_salary = basic_salary

# print() wyświetla informacje na ekranie.
# f'...' to f-string. Wartości zmiennych wstawiamy do tekstu za pomocą nawiasów klamrowych {}.
print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')