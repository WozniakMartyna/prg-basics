# Program ma wykonać kilka operacji na tytule filmu:
# Policzyć znaki, wyświetlić tekst wielkimi i małymi literami, policzyć wystąpienia litery e oraz sprawdzić położenie wybranych słów.

# Zapisujemy tytuł filmu w zmiennej movie.
movie = "The Lord of the Rings: The Return of the King"

# Liczymy liczbę wszystkich znaków w tytule.
# len() zwraca liczbę znaków, wliczając spacje i znaki interpunkcyjne.
print('Number of characters:', len(movie))

# Zamieniamy wszystkie litery na wielkie.
# Metoda upper() zwraca tekst zapisany wielkimi literami.
print('Uppercase:', movie.upper())

# Zamieniamy wszystkie litery na małe.
# Metoda lower() zwraca tekst zapisany małymi literami.
print('Lowercase:', movie.lower())

# Liczymy, ile razy w tekście występuje mała litera e.
# Metoda count() zwraca liczbę wystąpień podanego znaku lub fragmentu tekstu.
print('Number of letter e:', movie.count('e'))

# Sprawdzamy, na której pozycji zaczyna się słowo Lord.
# Metoda find() zwraca indeks pierwszego wystąpienia szukanego tekstu.
print('Position of Lord:', movie.find('Lord'))

# Sprawdzamy, na której pozycji zaczyna się słowo dragon.
# Jeśli szukanego tekstu nie ma, find() zwraca -1.
print('Position of dragon:', movie.find('dragon'))

# Indeksy zaczynają się od zera. Dlatego słowo Lord zaczyna się na pozycji 4, a nie 5.
# Jeśli find() nie znajdzie szukanego tekstu, zwróci -1.