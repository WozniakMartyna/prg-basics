# ZADANIE 7:
# Odczytanie liczb z pliku car_park.txt i obliczenie ich sumy.

# Otwieramy plik w trybie odczytu.
with open("car_park.txt", "r") as file:

    # read() odczytuje całą zawartość pliku jako tekst.
    content = file.read()

# splitlines() dzieli tekst na osobne linie.
# Otrzymujemy listę: ["25", "15", "7", "33", "5"].
lines = content.splitlines()

# Zmienna total przechowuje sumę liczb.
# Na początku wynosi 0, ponieważ jeszcze niczego nie dodaliśmy.
total = 0

# Przechodzimy kolejno przez wszystkie elementy listy.
for line in lines:

    # Dane odczytane z pliku są tekstem (str),
    # dlatego int() zamienia każdą wartość na liczbę całkowitą.
    number = int(line)

    # Dodajemy aktualną liczbę do dotychczasowej sumy.
    total += number

# Wyświetlamy końcowy wynik.
print("Total number of cars:", total)


# Notatka – problem ze znalezieniem pliku (FileNotFoundError)
# Python szuka pliku względem aktualnego folderu roboczego, a niekoniecznie folderu, w którym znajduje się plik .py.
# Rozwiązanie - zmiana folderu w terminalu:
# cd "Rozwiązania/08/1.7"
# python read_car_park.py
# - cd (change directory) – zmienia aktualny folder.
# - python read_car_park.py – uruchamia program.

# - total = 0 – tworzymy zmienną, która będzie przechowywać sumę.
# - int() – zamienia tekst przedstawiający liczbę na liczbę całkowitą.
# - total += number – skrócony zapis total = total + number.
# - for line in lines – wykonuje instrukcje dla każdego elementu listy.
# - splitlines() – rozdziela zawartość pliku według końców linii.

# Dlaczego potrzebujemy int()?
# Po odczytaniu pliku wartości 25, 15 i 7 są tekstem, a nie liczbami. Bez konwersji nie moglibyśmy poprawnie wykonać dodawania matematycznego.