# ZADANIE 5:
# Tworzenie listy zakupów na podstawie danych wpisywanych z klawiatury.

# Nazwa pliku, w którym będziemy przechowywać listę zakupów.
shopping_list = "shopping_list.txt"


# Funkcja dodaje jeden produkt na końcu pliku.
# file_name – nazwa pliku, do którego zapisujemy produkt.
# product_name – nazwa produktu podana przez użytkownika.
def add_product(file_name, product_name):

    # Otwieramy plik w trybie "a" (append).
    # Jeśli plik nie istnieje, zostanie utworzony.
    # Jeśli istnieje, nowy tekst zostanie dopisany na końcu.
    with open(file_name, "a") as file:

        # Zapisujemy nazwę produktu.
        # \n powoduje, że kolejny produkt będzie w nowej linii.
        file.write(product_name + "\n")


# Zmienna przechowuje nazwę produktu wpisaną przez użytkownika.
# Na początku jest pustym tekstem.
product = ""

# Pętla działa, dopóki użytkownik nie wpisze "0".
while product != "0":

    # input() wyświetla pytanie i pobiera tekst z klawiatury.
    product = input("Enter product name (0 stops): ")

    # Sprawdzamy, czy użytkownik wpisał 0.
    if product == "0":

        # break natychmiast kończy działanie pętli while.
        break

    else:

        # Jeśli użytkownik nie wpisał 0, dodajemy produkt do pliku.
        add_product(shopping_list, product)

# Komunikat wyświetlany po zakończeniu pętli.
print("Shopping list has been saved.")


# do terminala
# cd "Rozwiązania/08/2.5"
# python shopping.py

# "a" – tryb dopisywania danych na końcu pliku.
# def – definiuje funkcję.
# input() – pobiera dane wpisane przez użytkownika.
# while – powtarza instrukcje, dopóki warunek jest prawdziwy.
# if – sprawdza warunek.
# break – natychmiast przerywa działanie pętli.
# == – sprawdza, czy dwie wartości są równe.
# add_product(shopping_list, product) – wywołuje funkcję i przekazuje jej dwa argumenty.
# product_name + "\n" – zapisuje produkt w osobnej linii.