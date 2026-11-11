# Program wyświetla liczby od 0 do 4.
# while rozpoczyna pętlę, która działa, dopóki warunek jest prawdziwy.

count = 0  # Tworzymy zmienną count i ustawiamy jej wartość początkową na 0.

while count < 5:  # Pętla wykonuje się, dopóki count jest mniejsze od 5.
    print(count)  # Wyświetlamy aktualną wartość zmiennej count.
    count += 1  # Zwiększamy count o 1. To samo co: count = count + 1. Zwiększanie count jest ważne, ponieważ bez niego warunek mógłby być cały czas prawdziwy i pętla nie zakończyłaby się.
    # Gdy count osiągnie 5, warunek count < 5 będzie fałszywy (False) i pętla się zakończy.
    # Wcięcie oznacza, że instrukcje print() i count += 1 należą do pętli.