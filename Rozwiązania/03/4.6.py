# Oryginalny program sumuje liczby od 1 do 5. Należy zmienić zakres na liczby od 5 do 10 i zastosować operator +=

# Program oblicza sumę liczb całkowitych od 5 do 10.

# Zmienna sum przechowuje wynik dodawania.
# Na początku ustawiamy ją na 0.
sum = 0

# range(5, 11) tworzy liczby od 5 do 10.
# Wartość 11 nie jest uwzględniana.
for i in range(5, 11):
    # for powtarza dodawanie dla każdej liczby z zakresu.
    # i przechowuje aktualną liczbę
    # Operator += dodaje wartość "i" do zmiennej sum.
    # Zapis sum += i oznacza to samo co sum = sum + i.
    sum += i

# f-string pozwala wstawić wartość zmiennej sum do tekstu za pomocą {}.
print(f'Sum is {sum}')