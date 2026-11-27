# ZADANIE 4.2:
# Program zarządza kolejką plików oczekujących na wydruk.
# Plik dodany jako pierwszy zostanie wydrukowany jako pierwszy (FIFO).

import queue  # Importujemy moduł do obsługi kolejek.

# Queue() tworzy kolejkę działającą według zasady FIFO.
files_to_print = queue.Queue()

while True:
    # Wyświetlamy menu programu.
    print('1. Add file to print')
    print('2. Print file')
    print('0. Quit')

    menu = input('Select an option: ')

    # Opcja 1 – dodawanie pliku do kolejki.
    if menu == '1':
        file_name = input('Enter file name to print: ')

        # put() dodaje nowy plik na koniec kolejki.
        files_to_print.put(file_name)

        print(f'File {file_name} has been added to the print queue.')

    # Opcja 2 – drukowanie pliku.
    elif menu == '2':

        # empty() sprawdza, czy kolejka nie zawiera elementów.
        if not files_to_print.empty():

            # get() pobiera i usuwa pierwszy plik z kolejki.
            file_to_print = files_to_print.get()

            print(f'File {file_to_print} is currently being printed. Please wait!')

        else:
            print('The print queue is empty.')

    # Opcja 0 – zakończenie programu.
    elif menu == '0':
        break

    # Obsługa nieprawidłowej opcji.
    else:
        print('Invalid option. Please try again.')

    print()


# import queue	Importuje moduł kolejki
# queue.Queue()	Tworzy kolejkę FIFO
# .put(element)	Dodaje element na koniec kolejki
# .get()	Pobiera i usuwa pierwszy element
# .empty()	Sprawdza, czy kolejka jest pusta