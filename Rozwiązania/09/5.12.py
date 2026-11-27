
# ZADANIE 5.12:
# Odwrócenie tekstu z wykorzystaniem stosu (LIFO).

# Pustą listę wykorzystujemy jako stos.
stack = []

# Użytkownik wpisuje tekst, który chcemy odwrócić.
text = input("Enter text: ")

# Dodajemy każdy znak tekstu na stos.
for character in text:
    stack.append(character)  # append() dodaje element na koniec listy.

# Tworzymy pusty tekst, do którego będziemy dodawać pobrane znaki.
reversed_text = ""

# Dopóki stos nie jest pusty, pobieramy z niego kolejne znaki.
while len(stack) > 0:

    # pop() usuwa i zwraca ostatni element listy.
    # Ponieważ stos działa według zasady LIFO, znaki pobieramy od końca.
    reversed_text += stack.pop()

# Wyświetlamy odwrócony tekst.
print("Reversed text:", reversed_text)


# append(element) – dodaje element na koniec listy.
# pop() – usuwa i zwraca ostatni element listy.
# len(stack) – zwraca liczbę elementów stosu.
# while len(stack) > 0 – wykonuje pętlę, dopóki stos zawiera elementy.