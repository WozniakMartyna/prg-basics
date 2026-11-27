# ZADANIE 4.11:
# Zapisanie liczb od 1 do 100, ich kwadratów i sześcianów do pliku.

file_name = "powers.txt"

# "w" oznacza zapis do pliku. Jeśli plik już istnieje,
# jego poprzednia zawartość zostanie zastąpiona.
with open(file_name, "w") as file:

    # range(1, 101) generuje liczby od 1 do 100.
    # Górna granica 101 nie jest wliczana do zakresu.
    for number in range(1, 101):

        # ** oznacza potęgowanie:
        # number ** 2 to kwadrat, a number ** 3 to sześcian.
        square = number ** 2
        cube = number ** 3

        # f-string pozwala wstawić wartości zmiennych do tekstu.
        # \n oznacza przejście do następnego wiersza w pliku.
        file.write(f"{number},{square},{cube}\n")

# Ten komunikat pojawi się w terminalu, a nie w pliku.
print(f"Results have been saved to {file_name}.")

# do terminala
# cd "Rozwiązania/08/4.11"
# python powers.py
# Uwaga: Każde ponowne uruchomienie programu nadpisze poprzednią zawartość powers.txt, ponieważ używamy trybu "w".