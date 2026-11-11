# Program ma obliczyć wartości ułamków:
# Będziemy korzystać z pętli for, która kolejno podstawi liczby od 1 do 10 do mianownika.

# Program oblicza wartości ułamków od 1/1 do 1/10.

# range(1, 11) tworzy liczby od 1 do 10.
# Pętla for wykonuje się dla każdej z tych liczb.
# i przechowuje aktualną liczbę, która jest mianownikiem ułamka.
for i in range(1, 11):

    # Obliczamy 1 podzielone przez aktualną wartość i.
    # f-string pozwala wstawić wartości zmiennych do tekstu za pomocą {}.
    print(f'1/{i} = {1/i}')

# Rozwiązania:
# 1/1 = 1.0
# 1/2 = 0.5
# 1/3 = 0.3333333333333333
# 1/4 = 0.25
# 1/5 = 0.2
# 1/6 = 0.16666666666666666
# 1/7 = 0.14285714285714285
# 1/8 = 0.125
# 1/9 = 0.1111111111111111
# 1/10 = 0.1