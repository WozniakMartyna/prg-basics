# ZADANIE 3.23:
# Testowanie funkcji z modułu MyText.

# Importujemy własny moduł zapisany w pliku MyText.py.
import MyText

# Tworzymy tekst podany w poleceniu.
text = "An apple a day keeps the doctor away"

# Wywołujemy funkcję liczącą słowa.
print("Liczba słów:", MyText.count_words(text))

# Wyświetlamy słowa od najdłuższego do najkrótszego.
print("Od najdłuższego:", MyText.words_by_length(text))

# Wyświetlamy słowa w kolejności alfabetycznej.
print("Alfabetycznie:", MyText.words_alphabetically(text))

# Funkcje wywołujemy przez nazwę modułu i kropkę.
# Przykład: MyText.count_words(text)