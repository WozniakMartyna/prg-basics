# ZADANIE:
# Napisz funkcję f(text), która oddziela każdy znak tekstu myślnikiem.
#
# Przykłady:
# f("Univesity") -> "U-n-i-v-e-s-i-t-y"
# f("UE")        -> "U-E"
# f("x")         -> "x"
# f("")          -> ""


def f(text):
    # join() łączy elementy w jeden napis.
    #
    # "-".join(text) wstawia myślnik POMIĘDZY znaki tekstu.
    #
    # Przykład:
    # "-".join("ABC") -> "A-B-C"
    #
    # Nie dodaje myślnika na początku ani na końcu.
    # Dla pustego tekstu zwraca pusty tekst.

    return "-".join(text)


if __name__ == "__main__":
    print(f("Univesity"))  # U-n-i-v-e-s-i-t-y
    print(f("UE"))         # U-E
    print(f("x"))          # x
    print(f(""))           # Pusty tekst

# if __name__ == "__main__": oznacza: wykonaj poniższy kod tylko wtedy, gdy ten plik został uruchomiony bezpośrednio, a nie zaimportowany jako moduł.