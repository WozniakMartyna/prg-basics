# W oryginalnym programie mamy cztery opcje:
# 1. Sprawdzenie salda.
# 2. Wpłata pieniędzy.
# 3. Wypłata pieniędzy.
# 4. Wyjście z programu.
# Dodamy dwie kolejne:
# 5. Sprawdzenie PIN-u.
# 6. Zmiana PIN-u.
# PIN musi mieć dokładnie cztery cyfry. Zachowamy też dotychczasowe działanie bankomatu.

# ATM (cash machine) simulator
# Program symuluje działanie prostego bankomatu.
# Umożliwia sprawdzenie salda, wpłatę, wypłatę, sprawdzenie PIN-u oraz zmianę PIN-u.

balance = 1000  # Początkowe saldo konta wynosi 1000 euro.
pin = '1111'  # Początkowy PIN składa się z czterech cyfr.

# Pętla działa bez końca, dopóki użytkownik nie wybierze wyjścia.
while True:

    print()  # Wyświetlamy pustą linię dla lepszej czytelności.
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("5. Check PIN")
    print("6. Change PIN")

    choice = input("Choose an option (1-6): ")
    # input() pobiera wybraną opcję jako tekst.

    print()

    # Opcja 1 – sprawdzenie aktualnego salda.
    # if – sprawdza warunek.
    if choice == '1':
        print(f"Your current balance is: €{balance}")

    # Opcja 2 – wpłata pieniędzy.
    # elif – sprawdza kolejny warunek, jeśli wcześniejszy nie został spełniony.
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        # float() zamienia wpisany tekst na liczbę, która może mieć część dziesiętną.

        if amount > 0:
            balance += amount  # Dodajemy wpłacaną kwotę do salda. To samo co: balance = balance + amount.
            print(f"€{amount} has been deposited. New balance: €{balance}") # f"..." – pozwala umieszczać wartości zmiennych bezpośrednio w tekście.
        else:
            # else – wykonuje się, gdy żaden wcześniejszy warunek nie jest spełniony.
            print("The amount must be greater than zero.")

    # Opcja 3 – wypłata pieniędzy.
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))

        if amount > 0 and amount <= balance:
            # Sprawdzamy, czy kwota jest większa od zera
            # ORAZ czy nie przekracza aktualnego salda.

            balance -= amount  # Odejmujemy wypłacaną kwotę od salda. To samo co: balance = balance - amount.
            print(f"€{amount} has been withdrawn. New balance: €{balance}")

        elif amount <= 0:
            print("The amount must be greater than zero.")

        else:
            print("Insufficient balance.") # Jeśli wcześniejsze warunki nie są spełnione, pokazuje się komunikat o braku wystarczających środków.

    # Opcja 4 – zakończenie działania bankomatu.
    elif choice == '4':
        print("Exiting... Thank you for using the ATM!")
        break  # break natychmiast kończy działanie pętli while.

    # Opcja 5 – sprawdzenie PIN-u.
    elif choice == '5':
        entered_pin = input("Enter your PIN: ")
        # Pobieramy PIN jako tekst, aby zachować ewentualne zero na początku.

        if entered_pin == pin:
            print("Correct PIN!")
        else:
            print("Incorrect PIN!")

    # Opcja 6 – zmiana PIN-u.
    elif choice == '6':
        old_pin = input("Enter your current PIN: ")

        # Najpierw sprawdzamy, czy podany stary PIN jest prawidłowy.
        if old_pin == pin:
            new_pin = input("Enter your new 4-digit PIN: ")

            # Sprawdzamy, czy nowy PIN ma dokładnie 4 znaki (len(new_pin) == 4)
            # i czy wszystkie znaki są cyframi - new_pin.isdigit() – sprawdza, czy wszystkie znaki w PIN-ie są cyframi.
            if len(new_pin) == 4 and new_pin.isdigit():
                pin = new_pin  # Zapisujemy nowy PIN.
                print("PIN has been changed successfully!")
            else:
                print("Invalid PIN. It must contain exactly 4 digits.")

        else:
            print("Incorrect current PIN. PIN was not changed.")

    # Jeżeli użytkownik wpisał opcję spoza zakresu 1–6.
    else:
        print("Invalid option. Please try again.")

# Dlaczego PIN przechowujemy jako tekst (str), a nie liczbę (int)?
# Ponieważ PIN może zaczynać się od zera. Gdybyśmy zamienili 0123 na liczbę całkowitą, Python potraktowałby ją jako 123, tracąc początkowe zero. Ponadto metoda isdigit() działa na tekstach.