# ZADANIE 5.5:
# Program zlicza, ile razy każde słowo występuje w tekście.

paragraph = "cat dog mouse cat rat cat mouse"

# split() dzieli tekst na pojedyncze słowa.
words = paragraph.split()

# Tworzymy pusty słownik na wyniki.
word_count = {}

# Przechodzimy po wszystkich słowach.
for word in words:

    # Sprawdzamy, czy słowo znajduje się już w słowniku.
    if word in word_count:
        word_count[word] += 1  # Jeśli tak, zwiększamy licznik o 1.
    else:
        word_count[word] = 1   # Jeśli nie, dodajemy je z wartością 1.

# Wyświetlamy słowa i liczbę ich wystąpień.
for word, count in word_count.items():
    print(word, ":", count)

# split() – dzieli tekst na listę słów, domyślnie według białych znaków.
# word in word_count – sprawdza, czy klucz już istnieje.
# word_count[word] += 1 – zwiększa licznik danego słowa.