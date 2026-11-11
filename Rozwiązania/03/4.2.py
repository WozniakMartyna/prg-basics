# Pętla for pozwala powtarzać instrukcje dla kolejnych elementów, np. liter w tekście albo liczb w określonym zakresie.

# Przykład z treści zadania:
# Zmienna city przechowuje nazwę miasta.
city = 'Krakow'

# Pętla for przechodzi kolejno przez wszystkie znaki tekstu city.
# Zmienna char przechowuje aktualnie odczytaną literę.
for char in city:
    # print() wyświetla aktualną literę.
    print(char)

# Drugi przykład:
# range(5) tworzy zakres liczb od 0 do 4.
# Pętla for wykonuje się pięć razy.
for i in range(5):
    # Wyświetlamy aktualną wartość zmiennej i.
    print(i)

# for rozpoczyna pętlę, czyli powtarzanie instrukcji.
# char jest zmienną, która kolejno przechowuje znaki tekstu.
# i jest zmienną, która kolejno przechowuje liczby z zakresu.
# in oznacza "w" i wskazuje sekwencję, po której przechodzimy.
# Wcięcie wskazuje, które instrukcje należą do pętli.