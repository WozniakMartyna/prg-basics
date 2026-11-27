
# ZADANIE 5.13:
# Kalkulator odwrotnej notacji polskiej (RPN) wykorzystujący stos.
#
# Przykład:
# 2 3 + = oznacza 2 + 3 i daje wynik 5.
# 2 4 1 + * = oznacza 2 * (4 + 1) i daje wynik 10.

# Funkcja oblicza wyrażenie zapisane w odwrotnej notacji polskiej.
def calculate_rpn(expression):

    # Lista będzie pełnić funkcję stosu.
    stack = []

    # split() dzieli tekst na osobne elementy na podstawie spacji.
    # Przykład: "2 3 +" zamienia na ["2", "3", "+"].
    elements = expression.split()

    # Przechodzimy kolejno przez wszystkie elementy wyrażenia.
    for element in elements:

        # Znak "=" oznacza koniec wyrażenia.
        if element == "=":
            break

        # Jeśli element jest liczbą, dodajemy go na stos.
        elif element.lstrip("-").isdigit():
            stack.append(float(element))

        # W przeciwnym razie zakładamy, że element jest operatorem.
        elif element in ["+", "-", "*", "/"]:

            # Najpierw pobieramy prawy argument działania,
            # czyli liczbę, która została dodana na stos jako ostatnia.
            right = stack.pop()

            # Następnie pobieramy lewy argument działania.
            left = stack.pop()

            # Wykonujemy odpowiednie działanie.
            if element == "+":
                result = left + right
            elif element == "-":
                result = left - right
            elif element == "*":
                result = left * right
            elif element == "/":
                if right == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result = left / right

            # Wynik działania ponownie umieszczamy na stosie.
            stack.append(result)

        else:
            raise ValueError(f"Unknown element: {element}")

    # Po wykonaniu wszystkich działań na stosie powinien zostać jeden wynik.
    if len(stack) != 1:
        raise ValueError("Incorrect RPN expression.")

    return stack.pop()


# Pobieramy wyrażenie od użytkownika.
expression = input("Enter RPN expression (use spaces and finish with =): ")

# try pozwala przechwycić błędy, np. niepoprawne wyrażenie.
try:
    result = calculate_rpn(expression)
    print("Result:", result)

except (ValueError, IndexError, ZeroDivisionError) as error:
    print("Error:", error)


# Najważniejsze zasady działania stosu w tym zadaniu:
# 1. Jeśli program napotka liczbę, dodaje ją na stos.
# 2. Jeśli napotka operator, pobiera dwie ostatnie liczby.
# 3. Wykonuje działanie na pobranych liczbach.
# 4. Wynik odkłada z powrotem na stos.
# 5. Znak = kończy obliczenia.
# Kolejność pobierania liczb ma znaczenie! Dla odejmowania i dzielenia najpierw pobieramy right, a później left, ponieważ działanie wykonujemy jako left - right lub left / right.