# ZADANIE 5.7:
# Wyświetlenie nazw hoteli, średnich cen i porównanie miast.

hotels_in_Krakow = [
    {"name": "Sky", "price": 320.00},
    {"name": "Metropol", "price": 480.00},
    {"name": "New Port", "price": 420.00},
    {"name": "Aparthotel", "price": 390.00}
]

hotels_in_Sopot = [
    {"name": "Focus", "price": 510.00},
    {"name": "Aqua", "price": 345.00},
    {"name": "La Boutique", "price": 390.00},
    {"name": "Marina", "price": 410.00}
]

# Funkcja zwraca nazwy hoteli oddzielone przecinkami.
def hotel_list(hotels):
    names = []

    for hotel in hotels:
        names.append(hotel["name"])

    # join() łączy elementy listy w jeden tekst.
    return ",".join(names)


# Funkcja oblicza średnią cenę pokoju w hotelach.
def avg_price(hotels):
    total = 0

    # Dodajemy ceny wszystkich hoteli.
    for hotel in hotels:
        total += hotel["price"]

    # Dzielimy sumę przez liczbę hoteli.
    average = total / len(hotels)

    # round() zaokrągla wynik do liczby całkowitej.
    return round(average)


# Obliczamy średnie ceny dla obu miast.
krakow_average = avg_price(hotels_in_Krakow)
sopot_average = avg_price(hotels_in_Sopot)

# Wyświetlamy nazwy hoteli i średnie ceny.
print("Hotels in Krakow:", hotel_list(hotels_in_Krakow))
print("Average hotel price in Krakow:", krakow_average)

print("Hotels in Sopot:", hotel_list(hotels_in_Sopot))
print("Average hotel price in Sopot:", sopot_average)

# Porównujemy średnie ceny.
if krakow_average < sopot_average:
    print("Cheaper hotels in: Krakow")
elif sopot_average < krakow_average:
    print("Cheaper hotels in: Sopot")
else:
    print("Hotel prices are equal in both cities.")

# Ważne:
# - def – definiuje funkcję.
# - return – zwraca wynik funkcji.
# - append() – dodaje element do listy.
# - join() – łączy teksty z listy w jeden tekst.
# - len() – zwraca liczbę elementów.
# - round() – zaokrągla liczbę.