# ZADANIE 1.7:
# Wyświetlenie produktów w sklepie komputerowym
# oraz obliczenie ich łącznej liczby.

# Klucze oznaczają nazwy produktów,
# a wartości oznaczają ich ilości.
products = {
    "Laptop": 15,
    "Desktop PC": 10,
    "Monitor": 25,
    "Keyboard": 50,
    "Mouse": 60,
    "External Hard Drive": 30,
    "Printer": 12,
    "Router": 20,
    "USB Flash Drive": 100,
    "Graphics Card": 8
}

# Zmienna przechowująca sumę wszystkich produktów.
total = 0

print("PRODUCTS IN STORE")
print("=================")

# Przechodzimy po parach: nazwa produktu i ilość.
for name, quantity in products.items():
    print(f"{name}: {quantity}")

    # Dodajemy ilość aktualnego produktu do sumy.
    total += quantity

# Wyświetlamy łączną liczbę produktów.
print("=================")
print(f"Total number of products: {total}")

# total = 0 – początkowa wartość sumy.
# for name, quantity in products.items() – pobiera nazwę i ilość produktu.
# total += quantity – dodaje ilość do aktualnej sumy. To skrócony zapis total = total + quantity.