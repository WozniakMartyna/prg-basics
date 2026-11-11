# BMI Calculator
# Program oblicza wskaźnik BMI na podstawie wzrostu i masy ciała.


# Pytamy użytkownika o wzrost podany w centymetrach.
# input() pobiera tekst wpisany przez użytkownika.
height = input('Enter your height in cm: ')


# Pytamy użytkownika o wagę podaną w kilogramach.
weight = input('Enter your weight in kg: ')


# Zamieniamy wzrost z tekstu na liczbę całkowitą.
# int() służy do zamiany wartości na liczbę całkowitą.
height = int(height)


# Zamieniamy wagę z tekstu na liczbę całkowitą.
weight = int(weight)


# Obliczamy BMI według wzoru: masa ciała / (wzrost w metrach)^2.
# Dzielimy wzrost przez 100, aby zamienić centymetry na metry.
bmi = weight / (height/100)**2


# Zaokrąglamy wynik do dwóch miejsc po przecinku.
# round() zaokrągla liczbę, a 2 oznacza dwa miejsca po przecinku.
bmi = round(bmi,2)


# Wyświetlamy obliczony wynik BMI.
# print() pokazuje tekst i wartość zmiennej na ekranie.
print('Your BMI is', bmi)


# Wyświetlamy dodatkowy komunikat dla użytkownika.
print('Check on the Internet if your BMI is ok!!')