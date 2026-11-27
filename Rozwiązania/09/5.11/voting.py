# ZADANIE 5.11:
# Program przeprowadza głosowanie i zapisuje wyniki w pliku voting.json.
# Plik JSON będzie przechowywał nazwiska kandydatów i liczbę otrzymanych głosów.

import json  # Moduł json umożliwia zapisywanie i odczytywanie danych w formacie JSON.

file_name = "voting.json"

# Lista kandydatów dostępnych w głosowaniu.
candidates = ["Anna", "Jan", "Marek"]

# Próbujemy odczytać dotychczasowe wyniki z pliku.
try:
    with open(file_name, "r", encoding="utf-8") as file:
        votes = json.load(file)  # Zamienia dane JSON na słownik Pythona.

except FileNotFoundError:
    # Jeśli plik nie istnieje, tworzymy słownik z początkową liczbą głosów równą 0.
    votes = {
        candidate: 0
        for candidate in candidates
    }

# Wyświetlamy dostępnych kandydatów.
print("CANDIDATES")
for candidate in candidates:
    print(candidate)

# Użytkownik wpisuje imię wybranego kandydata.
choice = input("Vote for a candidate: ")

# Sprawdzamy, czy wpisane imię znajduje się wśród kandydatów.
if choice in votes:
    votes[choice] += 1  # Zwiększamy liczbę głosów danego kandydata o 1.
    print("Your vote has been counted.")
else:
    print("There is no such candidate.")

# Zapisujemy aktualne wyniki do pliku JSON.
# "w" oznacza tryb zapisu – poprzednia zawartość pliku zostanie zastąpiona.
with open(file_name, "w", encoding="utf-8") as file:
    # json.dump() zapisuje słownik do pliku w formacie JSON.
    # indent=4 sprawia, że dane są czytelnie rozmieszczone w kilku liniach.
    json.dump(votes, file, indent=4, ensure_ascii=False)

# Wyświetlamy aktualne wyniki głosowania.
print("\nVOTING RESULTS")
for candidate, number_of_votes in votes.items():
    print(f"{candidate}: {number_of_votes} votes")
