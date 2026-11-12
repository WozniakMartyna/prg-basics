# W tym zadaniu tworzymy program, który wyświetla komunikat zależny od temperatury.
# Program rozróżnia pięć zakresów temperatury.

temperature = float(input('Enter temperature in Celsius: '))

# Warunki sprawdzamy po kolei, zaczynając od najwyższej temperatury.
# elif oznacza kolejny warunek sprawdzany tylko wtedy, gdy wcześniejszy nie został spełniony.

if temperature > 35:
    print('It is extremely hot')
elif temperature > 30:
    print('It is hot')
elif temperature >= 15:
    print('It is warm')
elif temperature >= 0:
    print('It is cold')
else:
    # else obejmuje temperatury, które nie spełniły żadnego wcześniejszego warunku.
    print('Warning, frost')

# :.2f w f-stringu oznacza wyświetlenie temperatury z dwoma miejscami po przecinku.
print(f'Temperature: {temperature:.2f} degrees Celsius')

# Dlaczego sprawdzamy warunki od najwyższej temperatury?
# Ponieważ elif sprawdza warunki tylko do momentu znalezienia pierwszego prawdziwego.
# Dzięki temu każda temperatura otrzymuje tylko jeden właściwy komunikat.

# Wyniki dla przykładowych temperatur:
# 33 -> It is hot
# 30 -> It is warm
# 8 -> It is cold
# 0 -> It is cold
# -2 -> Warning, frost