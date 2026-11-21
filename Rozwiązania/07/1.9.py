# ZADANIE: Wyświetl numery rejestracyjne samochodów z Krakowa.
# Numery z Krakowa rozpoczynają się od KR lub KK.
# Każdy znaleziony numer rejestracyjny należy ponumerować.

# Tworzymy listę numerów rejestracyjnych.
# Każdy element listy jest tekstem zapisanym w cudzysłowie.
polish_license_plates = [
    "KR5233F",
    "PO6987E",
    "KR16179",
    "BI7192L",
    "KK12255",
    "WA7930T",
    "SK6922I",
    "KK61108",
    "KR90538",
    "BI8052Q",
    "KK54985",
    "LU4864U"
]

# Zmienna counter przechowuje numer znalezionego samochodu.
# Rozpoczynamy numerowanie od 1.
counter = 1

# Pętla for przechodzi kolejno przez wszystkie numery rejestracyjne.
# Zmienna car_number przechowuje aktualnie sprawdzany numer.
for car_number in polish_license_plates:

    # startswith() sprawdza, czy tekst rozpoczyna się od podanego fragmentu.
    # Operator or oznacza LUB.
    # Warunek jest prawdziwy, jeśli numer zaczyna się od KR albo KK.
    if car_number.startswith("KR") or car_number.startswith("KK"):

        # Wyświetlamy numer porządkowy i numer rejestracyjny.
        print(counter, car_number)

        # Zwiększamy licznik tylko wtedy, gdy znaleźliśmy właściwy samochód.
        counter += 1