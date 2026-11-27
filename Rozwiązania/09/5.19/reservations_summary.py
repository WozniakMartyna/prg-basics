# ZADANIE 5.19: Odczytanie rezerwacji hotelowych z pliku JSON
# i wyświetlenie podsumowania za pomocą osobnych funkcji.

import json  # Moduł json pozwala odczytywać dane zapisane w formacie JSON.


# Funkcja odczytuje dane z pliku i zwraca listę rezerwacji.
def load_reservations():
    with open("reservations.json", "r", encoding="utf-8") as file:
        data = json.load(file)  # Zamienia zawartość pliku JSON na słownik Pythona.

    return data["reservations"]  # Zwraca listę znajdującą się pod kluczem "reservations".


# Funkcja oblicza liczbę zarezerwowanych pokoi.
def count_rooms(reservations):
    return len(reservations)  # len() zwraca liczbę elementów na liście.


# Funkcja oblicza liczbę opłaconych rezerwacji.
def count_paid(reservations):
    count = 0

    for reservation in reservations:  # Przechodzimy po każdej rezerwacji na liście.
        if reservation["paid"] == True:  # Sprawdzamy, czy rezerwacja została opłacona.
            count += 1  # Zwiększamy licznik o 1.

    return count


# Funkcja oblicza liczbę nieopłaconych rezerwacji.
def count_unpaid(reservations):
    count = 0

    for reservation in reservations:
        if reservation["paid"] == False:  # False oznacza, że rezerwacja nie jest opłacona.
            count += 1

    return count


# Funkcja oblicza łączną wartość rezerwacji o wskazanym statusie płatności.
def calculate_value(reservations, payment_status):
    total = 0

    for reservation in reservations:
        if reservation["paid"] == payment_status:
            # Cena całej rezerwacji = liczba nocy * cena za jedną noc.
            reservation_value = reservation["nights"] * reservation["price_per_night"]
            total += reservation_value  # Dodajemy wartość rezerwacji do sumy.

    return total


# Główna część programu – pobieramy dane i wyświetlamy podsumowanie.
reservations = load_reservations()

print("HOTEL RESERVATIONS SUMMARY")
print("--------------------------")

print("Number of rooms:", count_rooms(reservations))
print("Number of paid reservations:", count_paid(reservations))
print("Number of unpaid reservations:", count_unpaid(reservations))

# True oznacza rezerwacje opłacone, a False – nieopłacone.
print("Total value of paid reservations:", calculate_value(reservations, True))
print("Total value of unpaid reservations:", calculate_value(reservations, False))


# do terminala
# cd "Rozwiązania/09/5.19"
# python reservations_summary.py

# Ważne: Wartość rezerwacji obliczamy jako nights * price_per_night, a nie tylko jako cenę jednej nocy.
# Funkcja calculate_value() przyjmuje drugi argument payment_status, dzięki czemu może obliczać zarówno sumę opłaconych, jak i nieopłaconych rezerwacji