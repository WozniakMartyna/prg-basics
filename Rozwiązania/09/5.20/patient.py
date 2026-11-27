
# ZADANIE: Zapisanie danych pacjenta do pliku JSON.

import json  # Importujemy moduł do obsługi plików JSON.

# Tworzymy słownik z danymi pacjenta.
# Słownik może zawierać inne słowniki i listy.
data = {
    "patient_record": {
        "patient_id": "P001234",
        "first_name": "John",
        "last_name": "Doe",
        "date_of_birth": "1985-05-15",
        "gender": "Male",
        "contact_info": {
            "phone_number": "+1-555-123-4567",
            "email": "johndoe@example.com",
            "address": {
                "street": "123 Main St",
                "city": "New York",
                "state": "NY",
                "postal_code": "10001",
                "country": "USA"
            }
        },
        "medical_history": {
            "allergies": ["Penicillin", "Peanuts"],
            "current_medications": [
                "Lisinopril 10mg",
                "Metformin 500mg"
            ],
            "past_illnesses": [
                "Hypertension",
                "Type 2 Diabetes"
            ],
            "surgeries": [
                {
                    "surgery_type": "Appendectomy",
                    "date": "2015-08-20"
                }
            ]
        }
    }
}

# Ustalamy nazwę pliku, do którego zapiszemy dane.
file_name = "patient.json"

# Otwieramy plik w trybie zapisu ("w").
# Jeśli plik nie istnieje, Python go utworzy.
with open(file_name, "w", encoding="utf-8") as file:
    # json.dump() zapisuje słownik data do otwartego pliku.
    # indent=4 dodaje wcięcia, żeby JSON był czytelny.
    json.dump(data, file, indent=4)

# Wyświetlamy informację o zakończeniu zapisu.
print("Data has been written to", file_name)


# do terminala
# cd "Rozwiązania/09/5.20"
# python patient.py