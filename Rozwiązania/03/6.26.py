# Program sprawdza poprawność czterocyfrowego kodu PIN.
# Użytkownik ma maksymalnie 3 próby.
# Po trzech błędnych próbach karta zostaje zablokowana.

# Poprawny PIN zapisujemy jako tekst, aby zachować zero na początku.
correct_pin = '0805'

# Licznik przechowuje liczbę wykorzystanych prób.
attempts = 0

# Pętla pozwala wpisywać PIN maksymalnie 3 razy.
while attempts < 3:

    # Pobieramy PIN od użytkownika.
    pin = input('Enter the PIN code: ')

    # Zwiększamy licznik prób o 1.
    attempts += 1

    # Sprawdzamy, czy PIN jest poprawny.
    if pin == correct_pin:
        print('Correct PIN')

        # break kończy pętlę po poprawnym wpisaniu PIN-u.
        break
    else:
        print('Incorrect...')

# Jeśli wykorzystano 3 próby i PIN nadal jest błędny, wyświetlamy informację o zablokowaniu karty.
if pin != correct_pin and attempts == 3:
    print('Sorry, your payment card has been blocked.')