# ZADANIE 1:
# Zapisanie informacji o filmie do pliku tekstowego.

# Zmienne przechowujące informacje o filmie.
movie_title = "Inception"
director = "Christopher Nolan"
lead_actor = "Leonardo DiCaprio"

# Nazwa pliku, do którego zapiszemy informacje.
file_name = "movie_details.txt"

# Otwieramy plik w trybie "w" (write).
# Jeśli plik nie istnieje, Python go utworzy.
# Jeśli już istnieje, jego poprzednia zawartość zostanie nadpisana.
with open(file_name, "w") as file:

    # write() zapisuje tekst do pliku.
    # f-string pozwala wstawiać wartości zmiennych za pomocą {}.
    # \n oznacza przejście do następnej linii.
    file.write(f"Movie Title: {movie_title}\n")
    file.write(f"Director: {director}\n")
    file.write(f"Lead Actor: {lead_actor}\n")

# Ten komunikat wyświetla się w terminalu, a nie w pliku.
print(f"Movie details have been written to {file_name}.")


# Korzystam w terminalu z:
# cd "Rozwiązania/08/2.1"
# python movie.py
# Żeby plik utowrzył się w folderze 2.1

# open(file_name, "w") – otwiera plik w trybie zapisu.
# write() – zapisuje tekst do pliku.
# \n – przechodzi do następnej linii.
# with – automatycznie zamyka plik po zakończeniu zapisywania.
# print() – wyświetla komunikat w terminalu, nie zapisuje go do pliku.