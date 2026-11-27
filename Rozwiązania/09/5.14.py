# ZADANIE 5.14:
# Symulacja kolejki klientów w punkcie obsługi.
# Kolejka działa według zasady FIFO (First In, First Out):
# pierwszy klient, który dołączył do kolejki, zostanie obsłużony jako pierwszy.

import queue  # Moduł queue udostępnia gotowe struktury kolejkowe.

# Tworzymy pustą kolejkę klientów.
# Queue() tworzy kolejkę FIFO.
customers = queue.Queue()

# Numer kolejnego biletu zaczyna się od 1.
ticket_number = 1

# Pętla działa do momentu wybrania opcji zakończenia programu.
while True:

    print("\nCUSTOMER SERVICE")
    print("1 - Add a customer")
    print("2 - Serve next customer")
    print("3 - Show number of waiting customers")
    print("4 - Exit")

    choice = input("Choose an option: ")

    # Opcja 1 – dodanie nowego klienta do kolejki.
    if choice == "1":

        # Pobieramy imię klienta.
        name = input("Enter customer name: ")

        # put() dodaje element na koniec kolejki.
        # Klient otrzymuje kolejny numer biletu.
        customer = f"Ticket {ticket_number}: {name}"
        customers.put(customer)

        print(f"Added to queue: {customer}")

        # Zwiększamy numer biletu o 1.
        ticket_number += 1

    # Opcja 2 – obsłużenie pierwszego klienta.
    elif choice == "2":

        # empty() sprawdza, czy kolejka jest pusta.
        if customers.empty():
            print("There are no customers waiting.")

        else:
            # get() pobiera i usuwa pierwszy element kolejki.
            # Dzięki FIFO obsługiwany jest najdłużej oczekujący klient.
            customer = customers.get()
            print(f"Now serving: {customer}")

    # Opcja 3 – wyświetlenie liczby oczekujących klientów.
    elif choice == "3":

        # qsize() zwraca aktualną liczbę elementów w kolejce.
        print("Waiting customers:", customers.qsize())

    # Opcja 4 – zakończenie programu.
    elif choice == "4":
        print("Program finished.")
        break  # Przerywa działanie pętli while.

    # Obsługa nieprawidłowego wyboru.
    else:
        print("Invalid option. Choose 1, 2, 3 or 4.")


# Ważne elementy do zapamiętania:
# Instrukcja	Znaczenie
# import queue	Importuje moduł do obsługi kolejek
# queue.Queue()	Tworzy kolejkę FIFO
# put(element)	Dodaje element na koniec kolejki
# get()	Pobiera i usuwa pierwszy element
# empty()	Sprawdza, czy kolejka jest pusta
# qsize()	Zwraca liczbę elementów w kolejce
# break	Kończy działanie pętli