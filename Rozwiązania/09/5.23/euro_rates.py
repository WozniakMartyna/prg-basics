# ZADANIE 5.23: Pobranie 10 ostatnich kursów euro ze strony NBP,
# wyświetlenie ich w terminalu i zapisanie do pliku Euro.json.

import json  # Moduł służący do odczytywania i zapisywania danych JSON.
import urllib.request  # Moduł pozwalający pobierać dane ze stron internetowych.

# Zapisujemy adres API NBP, z którego pobierzemy kursy euro.
# API to sposób, w jaki program może pobierać dane z innej usługi.
#
# rates/a/eur oznacza kurs średni euro z tabeli A.
# last/10 oznacza, że chcemy pobrać 10 ostatnich notowań.
# format=json określa, że odpowiedź ma być w formacie JSON.
url = "https://api.nbp.pl/api/exchangerates/rates/a/eur/last/10/?format=json"

# urllib.request.urlopen() łączy się z podanym adresem internetowym.
# Odpowiedź ze strony zapisujemy w zmiennej response.
# with automatycznie zamyka połączenie po zakończeniu bloku kodu.
with urllib.request.urlopen(url) as response:

    # read() pobiera zawartość odpowiedzi ze strony.
    # Dane otrzymujemy w postaci bajtów, dlatego używamy decode().
    # decode("utf-8") zamienia bajty na zwykły tekst.
    data_text = response.read().decode("utf-8")

# json.loads() zamienia tekst zapisany w formacie JSON
# na odpowiednią strukturę danych Pythona, w tym przypadku słownik.
# Różnica: loads() odczytuje tekst, a load() odczytuje bezpośrednio plik.
data = json.loads(data_text)

# Wyświetlamy nagłówek wyników w terminalu.
print("10 LAST EURO EXCHANGE RATES")
print("---------------------------")

# W słowniku data pod kluczem "rates" znajduje się lista kursów.
# Pętla for przechodzi kolejno przez każdy element tej listy.
for rate in data["rates"]:

    # effectiveDate oznacza datę obowiązywania danego kursu.
    print("Date:", rate["effectiveDate"])

    # mid oznacza średni kurs euro podany w złotówkach.
    print("Euro rate:", rate["mid"], "PLN")

    # Pusty print() dodaje wolny wiersz, aby oddzielić kolejne notowania.
    print()

# Po wyświetleniu danych zapisujemy je również w osobnym pliku.
# Otwieramy Euro.json w trybie zapisu ("w").
# Jeśli plik nie istnieje, Python go utworzy.
with open("Euro.json", "w", encoding="utf-8") as file:

    # json.dump() zapisuje słownik data do pliku.
    # file wskazuje plik, do którego zapisujemy dane.
    # indent=4 ustawia wcięcia, aby plik był czytelny.
    # ensure_ascii=False zachowuje znaki specjalne.
    json.dump(data, file, indent=4, ensure_ascii=False)

# Wyświetlamy komunikat o zapisaniu danych.
print("Data has been saved to Euro.json")

# do terminala
# cd "Rozwiązania/09/5.23"
# python euro_rates.py