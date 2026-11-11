# Szyfr Cezara jest prostą metodą szyfrowania tekstu. Każdą literę zastępujemy kolejną literą alfabetu, czyli przesuwamy ją o jedną pozycję w prawo.
# Przykłady:
# A -> B
# B -> C
# C -> D
# W tym zadaniu wykorzystamy funkcje:
# ord() – zamienia znak na jego kod liczbowy.
# chr() – zamienia kod liczbowy na znak.

# Zmienna plain_text przechowuje tekst przed zaszyfrowaniem.
plain_text = 'The early bird catches the worm'

# Tworzymy pusty tekst na zaszyfrowaną wiadomość.
encrypted_text = ''

# Pętla for przechodzi kolejno przez każdy znak tekstu.
for char in plain_text:
    
    # char przechowuje aktualny znak.
    # ord() zamienia aktualny znak na jego kod liczbowy.
    char_code = ord(char)

    # Dodajemy 1 do kodu znaku, aby przesunąć go o jedną pozycję.
    new_char_code = char_code + 1

    # chr() zamienia nowy kod liczbowy na odpowiadający mu znak.
    encrypted_char = chr(new_char_code)

    # Operator + dodaje zaszyfrowany znak na końcu tekstu.
    encrypted_text = encrypted_text + encrypted_char

# Wyświetlamy tekst przed zaszyfrowaniem.
print(plain_text)

# Wyświetlamy zaszyfrowany tekst.
print(encrypted_text)

# program przesuwa o jeden kod wszystkie znaki, nie tylko litery. Dlatego spacja zmienia się w wykrzyknik.