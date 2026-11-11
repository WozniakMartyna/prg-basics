# Program pobiera dwa numery i symbol działania matematycznego. Następnie wykonuje odpowiednie działanie.
# Program działa jak prosty kalkulator.

# input() pobiera pierwszą liczbę.
# float() zamienia tekst na liczbę, która może mieć część dziesiętną.
number1 = float(input('Enter first number: '))

# Pobieramy drugą liczbę.
number2 = float(input('Enter second number: '))

# Pobieramy symbol działania matematycznego.
operator = input('Enter operator (+, -, *, /): ')

# Sprawdzamy, jakie działanie wybrał użytkownik.
# == sprawdza, czy dwie wartości są równe.
if operator == '+':
    result = number1 + number2  # Dodawanie.
elif operator == '-':
    result = number1 - number2  # Odejmowanie.
elif operator == '*':
    result = number1 * number2  # Mnożenie.
elif operator == '/':
    # Przed dzieleniem sprawdzamy, czy druga liczba nie jest zerem.
    # != oznacza "różne od".
    # Dodatkowy warunek chroni program przed dzieleniem przez zero.
    if number2 != 0:
        result = number1 / number2  # Dzielenie.
    else:
        result = None  # None oznacza brak wyniku.
else:
    result = None  # Nieprawidłowy symbol działania.

# Sprawdzamy, czy udało się obliczyć wynik.
# None oznacza brak wartości.
# is not None sprawdza, czy zmienna nie ma wartości None.
if result is not None:
    # f-string wstawia wartości zmiennych i wynik do tekstu za pomocą {}.
    print(f'{number1} {operator} {number2} = {result}')
else:
    print('Incorrect operator or division by zero')

# Sprawdzanie podanych liczb i operatorów:
# Liczby = 2, 3, Operator = +, Wynik: "2.0 + 3.0 = 5.0"
# Liczby = 2, 4, Operator = *, Wynik: "2.0 * 4.0 = 8.0"
# Liczby = 3, 5, Operator = -, Wynik: "5.0 - 3.0 = 2.0"
# Liczby = 5, 6, Operator = *, Wynik: "5.0 * 6.0 = 30.0"