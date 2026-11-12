# Program wyświetla cyfry od 1 do 9.
# Każda cyfra jest powtarzana tyle razy, ile wynosi jej wartość.

# Pętla przechodzi przez liczby od 1 do 9.
for i in range(1, 10):

    # str(i) zamienia liczbę na tekst.
    # Operator * powtarza tekst tyle razy, ile wynosi i.
    print(str(i) * i)

# str() jest potrzebne, ponieważ chcemy powtarzać znak jako tekst, a nie wykonywać mnożenie matematyczne.