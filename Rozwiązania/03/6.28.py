# Wyświetlanie pierwszych 20 wyrazów ciągu Fibonacciego

a = 0  # Pierwszy wyraz ciągu
b = 1  # Drugi wyraz ciągu
count = 0  # Licznik wyświetlonych wyrazów

while count < 20:  # Pętla działa, dopóki nie wyświetlimy 20 wyrazów
    print(a, end=' ')  # Wyświetlamy aktualny wyraz; end=' ' zostawia spację zamiast nowej linii

    next_number = a + b  # Następny wyraz jest sumą dwóch poprzednich
    a = b  # Przesuwamy drugi wyraz na pierwsze miejsce
    b = next_number  # Zapisujemy nowy wyraz na drugim miejscu

    count += 1  # Zwiększamy licznik o 1