# Mamy podane zarobki ojca i matki oraz liczbę członków rodziny. Najpierw obliczamy całkowity dochód, a następnie dzielimy go przez liczbę osób.

# A program that calculates family income per person.
# Program oblicza dochód rodziny przypadający na jedną osobę.

# Zapisujemy miesięczny dochód ojca.
father_income = 5450

# Zapisujemy miesięczny dochód matki.
mother_income = 4920

# Zapisujemy liczbę członków rodziny.
family_members = 5

# Dodajemy dochody ojca i matki.
total_income = father_income + mother_income

# Dzielimy całkowity dochód przez liczbę członków rodziny.
income_per_person = total_income / family_members

# Wyświetlamy całkowity dochód oraz dochód na jedną osobę.
# f"..." – tworzy f-string, czyli tekst, w którym można umieszczać wartości zmiennych w nawiasach {}.
# {total_income} i {income_per_person} – wstawiają wartości zmiennych do f-stringa.
print(f"Total family income is {total_income}, and income per person is {income_per_person}.")