# Program sprawdza, czy użytkownik wpisał prawidłowy login i hasło.
# Prawidłowe dane:
# Login: joe
# Hasło: abcd

login = 'joe'  # Zmienna przechowuje prawidłowy login.
password = 'abcd'  # Zmienna przechowuje prawidłowe hasło.

# input() pobiera login wpisany przez użytkownika.
entered_login = input('Login: ')

# input() pobiera hasło wpisane przez użytkownika.
entered_password = input('Password: ')

# Operator == sprawdza, czy wpisany login jest zgodny z prawidłowym loginem.
# Operator and oznacza "i" – oba warunki muszą być prawdziwe.
# Sprawdzamy więc jednocześnie login i hasło.
if login == entered_login and password == entered_password:
    # if wykonuje kod, jeśli oba warunki są prawdziwe.
    print('You are logged in')
else:
    # else wykonuje się, jeśli przynajmniej jeden warunek jest fałszywy.
    print('Incorrect login or password!!')