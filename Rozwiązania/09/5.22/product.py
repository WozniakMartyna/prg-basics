# ZADANIE 5.22: Pobranie od użytkownika informacji o produkcie
# i zapisanie ich w pliku JSON.

import json  # Importujemy moduł do obsługi plików JSON.

# input() wyświetla pytanie i pozwala użytkownikowi wpisać odpowiedź.
# Wpisana wartość zostaje początkowo zapisana jako tekst (str).
name = input("Enter product name: ")

# Pytamy o cenę produktu.
# float() zamienia wpisany tekst na liczbę zmiennoprzecinkową,
# dzięki czemu można podać np. 19.99.
price = float(input("Enter product price: "))

# Pytamy, czy produkt został opłacony.
# lower() zamienia wszystkie litery tekstu na małe.
# Dzięki temu odpowiedzi YES, Yes i yes będą traktowane tak samo.
paid_answer = input("Has the product been paid for? (yes/no): ").lower()

# Sprawdzamy, czy użytkownik wpisał dokładnie "yes".
# Operator == porównuje dwie wartości.
# Wynikiem porównania jest True (prawda) albo False (fałsz).
# Zmienna paid będzie więc miała typ logiczny (bool).
paid = paid_answer == "yes"

# Tworzymy słownik z informacjami o produkcie.
# Każdy klucz opisuje przechowywaną wartość.
product = {
    "name": name,   # Nazwa produktu wpisana przez użytkownika.
    "price": price, # Cena produktu jako liczba.
    "paid": paid    # Informacja o płatności jako True lub False.
}

# Otwieramy plik product.json w trybie zapisu ("w").
# Jeśli plik nie istnieje, zostanie utworzony.
# Jeśli istnieje, jego zawartość zostanie zastąpiona nowymi danymi.
with open("product.json", "w", encoding="utf-8") as file:

    # Zapisujemy słownik product do pliku w formacie JSON.
    # indent=4 dodaje wcięcia, aby dane były łatwe do odczytania.
    # ensure_ascii=False pozwala zachować polskie znaki.
    json.dump(product, file, indent=4, ensure_ascii=False)

# Informujemy użytkownika, że dane zostały zapisane.
print("Product data has been saved to product.json")

# do terminala
# cd "Rozwiązania/09/5.22"
# python product.py 

# float() zamienia cenę na liczbę, a porównanie paid_answer == "yes" daje wartość logiczną True albo False. JSON zapisuje je jako true lub false.