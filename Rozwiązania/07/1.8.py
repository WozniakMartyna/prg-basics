# ZADANIE: Wyświetl posortowaną alfabetycznie listę gier komputerowych.
# Każda gra ma być wyświetlona w osobnej linii i mieć swój numer.
# Do wyświetlania wykorzystujemy pętlę while.

# Tworzymy listę o nazwie computer_games.
# Przechowujemy w niej nazwy gier komputerowych.
computer_games = [
    "Minecraft",
    "Fortnite",
    "Cyberpunk 2077",
    "The Witcher 3",
    "League of Legends",
    "Valorant",
    "Grand Theft Auto V",
    "Elden Ring",
    "Apex Legends",
    "Call of Duty: Warzone"
]

# sorted() tworzy nową listę zawierającą elementy w kolejności alfabetycznej.
# Przypisujemy posortowaną listę ponownie do zmiennej computer_games.
computer_games = sorted(computer_games)

# Tworzymy zmienną i = 0.
# Będzie ona przechowywać indeks aktualnie wyświetlanej gry.
# Zaczynamy od 0, ponieważ indeksy listy zaczynają się od zera.
i = 0

# Tworzymy zmienną counter = 1.
# Będzie ona przechowywać numer gry wyświetlany użytkownikowi.
# Numerowanie zaczynamy od 1, a nie od 0.
counter = 1

# Pętla while wykonuje instrukcje tak długo, jak warunek jest prawdziwy.
# len(computer_games) zwraca liczbę gier, czyli 10.
# Pętla zakończy się, kiedy i osiągnie wartość 10.
while i < len(computer_games):

    # computer_games[i] pobiera grę znajdującą się pod aktualnym indeksem.
    # print() wyświetla numer gry i jej nazwę.
    print(counter, computer_games[i])

    # Zwiększamy indeks o 1, aby przejść do następnej gry.
    i += 1

    # Zwiększamy numer wyświetlanej gry o 1.
    counter += 1