# ZADANIE 3.23:
# Moduł zawierający funkcje do pracy z tekstem.

# Funkcja liczy liczbę słów w tekście.
def count_words(text):

    # split() dzieli tekst na listę słów.
    words = text.split()

    # len() zwraca liczbę elementów listy.
    return len(words)


# Funkcja zwraca słowa od najdłuższego do najkrótszego.
def words_by_length(text):

    # Dzielimy tekst na pojedyncze słowa.
    words = text.split()

    # Sortujemy słowa metodą bąbelkową według długości.
    for i in range(len(words)):
        for j in range(len(words) - i - 1):

            # Jeżeli lewe słowo jest krótsze od prawego,
            # zamieniamy je miejscami.
            if len(words[j]) < len(words[j + 1]):
                words[j], words[j + 1] = words[j + 1], words[j]

    return words


# Funkcja zwraca słowa w kolejności alfabetycznej.
def words_alphabetically(text):

    # Dzielimy tekst na listę słów.
    words = text.split()

    # Sortujemy słowa alfabetycznie metodą bąbelkową.
    for i in range(len(words)):
        for j in range(len(words) - i - 1):

            # lower() zamienia litery na małe,
            # aby porównywanie nie zależało od wielkości liter.
            if words[j].lower() > words[j + 1].lower():
                words[j], words[j + 1] = words[j + 1], words[j]

    return words