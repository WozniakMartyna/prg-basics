# ZADANIE 3.3:
# Sprawdzanie poprawności nawiasów za pomocą stosu.

# Wykorzystujemy stos:
# 1. Jeśli napotkamy nawias otwierający, dodajemy go na stos.
# 2. Jeśli napotkamy nawias zamykający, pobieramy ostatni nawias otwierający.
# 3. Sprawdzamy, czy tworzą pasującą parę.
# 4. Na końcu stos musi być pusty.

# Funkcja zwraca True, jeśli wszystkie nawiasy są poprawne,
# albo False, jeśli występuje błąd.
def brackets_ok(expression):

    # Lista będzie pełnić funkcję stosu.
    stack = []

    # Słownik określa, jaki nawias otwierający
    # pasuje do danego nawiasu zamykającego.
    matching_brackets = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    # Przechodzimy po wszystkich znakach wyrażenia.
    for char in expression:

        # Jeśli znak jest nawiasem otwierającym,
        # dodajemy go na szczyt stosu.
        if char in "({[":
            stack.append(char)

        # Jeśli znak jest nawiasem zamykającym...
        elif char in ")}]":

            # Jeśli stos jest pusty, nie ma nawiasu otwierającego,
            # który mógłby pasować do zamykającego.
            if len(stack) == 0:
                return False

            # Pobieramy ostatni nawias otwierający ze stosu.
            last_opening = stack.pop()

            # Sprawdzamy, czy pobrany nawias pasuje
            # do aktualnego nawiasu zamykającego.
            if last_opening != matching_brackets[char]:
                return False

    # Jeśli stos jest pusty, wszystkie nawiasy zostały zamknięte.
    # Jeśli coś pozostało, brakuje nawiasu zamykającego.
    return len(stack) == 0


# Trzy wyrażenia podane w zadaniu.
expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"
expression2 = "[(2+3]/4)"
expression3 = "(2-3*4+(5/6)"


# Sprawdzamy pierwsze wyrażenie.
if brackets_ok(expression1):
    print("Expression 1: brackets are correct.")
else:
    print("Expression 1: brackets are incorrect.")

# Sprawdzamy drugie wyrażenie.
if brackets_ok(expression2):
    print("Expression 2: brackets are correct.")
else:
    print("Expression 2: brackets are incorrect.")

# Sprawdzamy trzecie wyrażenie.
if brackets_ok(expression3):
    print("Expression 3: brackets are correct.")
else:
    print("Expression 3: brackets are incorrect.")


# - for char in expression – przechodzi po kolejnych znakach tekstu.
# - char in "({[" – sprawdza, czy znak jest jednym z nawiasów otwierających.
# - matching_brackets[char] – pobiera ze słownika nawias pasujący do aktualnego nawiasu zamykającego.
# - return False – natychmiast kończy funkcję i zwraca informację o błędzie.
# - return len(stack) == 0 – zwraca True, jeśli stos jest pusty, w przeciwnym razie False.
# Ważne: W treści zadania pojawia się import queue, ale w tym rozwiązaniu nie jest potrzebny. Moduł queue służy przede wszystkim do obsługi kolejek. Tutaj stos realizujemy za pomocą listy i metod append() oraz pop().