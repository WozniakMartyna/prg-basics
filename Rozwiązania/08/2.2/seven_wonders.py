# ZADANIE 2:
# Zapisanie siedmiu cudów świata do pliku w kolejności alfabetycznej.

# Lista zawierająca nazwy siedmiu cudów świata.
seven_wonders = [
    "Great Wall of China",
    "Petra",
    "Christ the Redeemer",
    "Machu Picchu",
    "Chichen Itza",
    "Roman Colosseum",
    "Taj Mahal"
]

# Nazwa pliku, do którego zapiszemy listę.
file_name = "seven_wonders.txt"

# sorted() tworzy nową listę posortowaną alfabetycznie.
# Nie zmienia oryginalnej listy seven_wonders.
sorted_wonders = sorted(seven_wonders)

# Otwieramy plik w trybie zapisu ("w").
with open(file_name, "w") as file:

    # for przechodzi kolejno przez wszystkie elementy posortowanej listy.
    for item in sorted_wonders:

        # Zapisujemy nazwę cudu świata.
        # \n powoduje, że kolejny element znajdzie się w następnej linii.
        file.write(item + "\n")

# Informujemy użytkownika o zakończeniu zapisywania.
print(f"Seven Wonders have been saved to {file_name}.")

# cd "Rozwiązania/08/2.2"
# python seven_wonders.py
# Wpisać w terminalu, żeby plik utowrzył się w 2.2

# sorted(lista) – zwraca nową listę posortowaną alfabetycznie.
# for item in sorted_wonders – pobiera kolejno każdy element listy.
# file.write(item + "\n") – zapisuje element i znak przejścia do nowej linii.
# + – łączy dwa teksty (konkatenacja).
# "\n" – dzięki temu każdy cud świata zapisuje się w osobnym wierszu.