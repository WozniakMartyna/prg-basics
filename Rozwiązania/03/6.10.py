# W tym zadaniu przeliczamy wiek psa podany w latach ludzkich na psie lata.
# Pierwsze dwa lata odpowiadają po 10,5 roku, a każdy kolejny rok odpowiada 4 latom.

# input() pobiera wiek psa wpisany przez użytkownika.
# float() zamienia wpisany tekst na liczbę zmiennoprzecinkową, dzięki czemu można podać np. 1.5 roku.
dog_age = float(input("Enter the dog's age in human years: "))

# Jeżeli pies ma najwyżej 2 lata, mnożymy jego wiek przez 10,5.
if dog_age <= 2:
    dog_years = dog_age * 10.5
else:
    # Pierwsze dwa lata odpowiadają łącznie 21 latom.
    first_two_years = 2 * 10.5

    # Obliczamy liczbę lat, które pozostają po odjęciu pierwszych dwóch.
    remaining_years = dog_age - 2

    # Pozostałe lata mnożymy przez 4 i dodajemy do pierwszych 21 lat.
    dog_years = first_two_years + remaining_years * 4

# F-string pozwala wstawić wynik do tekstu za pomocą nawiasów klamrowych {}.
# :.0f oznacza wyświetlenie liczby bez miejsc po przecinku.
print(f"The dog's age in dog's years is {dog_years:.0f} years.")