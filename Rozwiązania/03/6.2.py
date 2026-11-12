# W oryginalnym programie pętla for przechodzi kolejno przez wszystkie znaki tekstu i sprawdza, czy dany znak jest samogłoską.
# Naszym zadaniem jest zastąpienie pętli for pętlą while, zachowując pozostałe działanie programu.

# Program zlicza samogłoski w tekście.

text = "This is a sample text."  # Tekst, w którym będziemy szukać samogłosek.
vowels = "aeiouAEIOU"  # Lista samogłosek: małych i wielkich liter.
vowel_count = 0  # Zmienna przechowująca liczbę znalezionych samogłosek. Ustawia początkową liczbę samogłosek na zero.
i = 0  # Ustawiamy indeks pierwszego znaku. W Pythonie indeksowanie zaczyna się od zera.

# Pętla działa, dopóki i jest mniejsze od długości tekstu.
# funkcja len() zwraca długość tekstu, czyli liczbę jego znaków.
while i < len(text):

    # Pobieramy znak (za pomocą char) znajdujący się na pozycji i w tekście.
    char = text[i]

    # Sprawdzamy, czy aktualny znak char znajduje się w ciągu vowels.
    if char in vowels:
        vowel_count += 1  # Jeżeli tak, zwiększamy licznik samogłosek o 1. To skrócony zapis vowel_count = vowel_count + 1.

    i += 1  # Zwiększamy indeks o jeden, żeby sprawdzić następny znak. Przechodzimy do następnego znaku tekstu.

# Wyświetlamy liczbę znalezionych samogłosek.
print(f"The number of vowels in the text is: {vowel_count}") # to f-string. Litera f przed cudzysłowem umożliwia wstawienie wartości zmiennej w nawiasach klamrowych {} bezpośrednio do tekstu.

# Dlaczego musimy używać i += 1?
# Ponieważ bez zwiększania indeksu program cały czas sprawdzałby ten sam znak. Pętla mogłaby wtedy nigdy się nie zakończyć.