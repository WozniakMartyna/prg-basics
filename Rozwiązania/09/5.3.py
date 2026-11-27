# ZADANIE 5.3:
# Program tłumaczy słowa z języka angielskiego na polski.

# Tworzymy słownik, w którym klucze to słowa angielskie,
# a wartości to ich polskie tłumaczenia.
translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}

# Pobieramy słowo od użytkownika.
word = input("Enter an English word: ")

# Sprawdzamy, czy podane słowo znajduje się w słowniku.
if word in translations:
    # Jeśli tak, wyświetlamy jego tłumaczenie.
    print("Translation:", translations[word])
else:
    # Jeśli nie, informujemy o braku tłumaczenia.
    print("Translation is not available.")

# input() – pobiera tekst od użytkownika.
# word in translations – sprawdza, czy słowo jest kluczem słownika.
# translations[word] – pobiera wartość przypisaną do danego klucza.