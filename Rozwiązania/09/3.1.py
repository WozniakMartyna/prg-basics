# # PRZYKŁAD:
# Utworzenie stosu i dodawanie oraz pobieranie elementów.

# import queue  # Importujemy moduł do obsługi kolejek i stosów.

# LifoQueue tworzy stos działający według zasady LIFO.
# cards = queue.LifoQueue()

# put() dodaje element na szczyt stosu.
# cards.put('King of Hearts \u2665')
# cards.put('Queen of Diamonds \u2666')
# cards.put('Jack of Spades \u2660')

# qsize() zwraca liczbę elementów znajdujących się na stosie.
# print('Number of stack elements:', cards.qsize())

# empty() sprawdza, czy stos jest pusty.
# get() pobiera i usuwa element ze szczytu stosu.
# while not cards.empty():
#    card = cards.get()
#    print(card)

# ^ PRZED MODYFIKACJĄ (plik stack_example.py)


# ZADANIE 3.1:
# Dodawanie liczb na stos, sumowanie dwóch ostatnich liczb
# oraz obliczanie sumy pozostałych elementów.

import queue

# Tworzymy stos działający według zasady LIFO.
stack = queue.LifoQueue()

# 1–7. Dodajemy kolejno podane liczby na stos.
stack.put(2)
stack.put(3)
stack.put(7)
stack.put(4)
stack.put(1)
stack.put(9)
stack.put(8)

# Wyświetlamy liczbę elementów na stosie.
print("Number of stack elements:", stack.qsize())

# 8. Pobieramy dwie ostatnie liczby ze stosu.
# get() usuwa pobrany element ze stosu.
number1 = stack.get()
number2 = stack.get()

# Obliczamy sumę dwóch pobranych liczb.
last_two_sum = number1 + number2

print("Last two numbers:", number1, "and", number2)
print("Sum of last two numbers:", last_two_sum)

# 9. Obliczamy sumę pozostałych elementów.
remaining_sum = 0

# empty() zwraca True, gdy stos jest pusty.
# Pętla działa, dopóki na stosie znajdują się elementy.
while not stack.empty():

    # Pobieramy kolejny element i dodajemy go do sumy.
    remaining_sum += stack.get()

print("Sum of remaining numbers:", remaining_sum)