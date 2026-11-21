# ZADANIE: Znajdź wartość kostki występującą w najdłuższej serii kolejnych rzutów.

def f(dice):
    if dice == "":
        return None  # Dla pustego tekstu nie ma żadnych rzutów.

    current_value = dice[0]  # Aktualna wartość oczek.
    current_count = 1        # Długość aktualnej serii.

    best_value = current_value  # Najlepsza znaleziona dotąd wartość.
    best_count = 1              # Długość najdłuższej serii.

    # dice[1:] oznacza tekst od drugiego znaku do końca.
    for roll in dice[1:]:

        if roll == current_value:
            current_count += 1  # Ta sama wartość – wydłużamy serię.
        else:
            current_value = roll  # Inna wartość – zaczynamy nową serię.
            current_count = 1

        # Sprawdzamy, czy aktualna seria jest dłuższa od poprzedniej.
        # Używamy >, a nie >=, żeby przy remisie zachować pierwszą serię.
        if current_count > best_count:
            best_count = current_count
            best_value = current_value

    return int(best_value)  # Zamieniamy znak cyfry na liczbę.


def main():
    print(f("5233165554211"))  # 5 – występuje pięć razy pod rząd.
    print(f("2133"))           # 3 – dwa razy pod rząd.


if __name__ == "__main__":
    main()