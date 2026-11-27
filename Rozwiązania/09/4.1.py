# PRZYKŁAD 4.1:
# Tworzenie kolejki i dodawanie oraz pobieranie elementów.

import queue  # Importujemy moduł obsługujący kolejki.

# Queue() tworzy kolejkę działającą według zasady FIFO.
people = queue.Queue()

# put() dodaje elementy na koniec kolejki.
people.put('Michael')
people.put('Charlotte')
people.put('Olivia')

# qsize() zwraca liczbę elementów znajdujących się w kolejce.
print('Number of queue elements:', people.qsize())

# empty() sprawdza, czy kolejka jest pusta.
# get() pobiera i usuwa pierwszy element z kolejki.
while not people.empty():
    person = people.get()
    print(person)