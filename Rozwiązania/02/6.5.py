# Program ma pobrać dziewięciocyfrowy numer telefonu i wyświetlić go w trzech grupach po trzy cyfry, oddzielonych myślnikami.

# Program wyświetla numer telefonu w trzech grupach po trzy cyfry.

# Pobieramy numer telefonu od użytkownika.
# input() pobiera wpisaną wartość jako tekst.
# Dzięki temu zachowujemy wszystkie cyfry, również zero na początku.
# Dlaczego nie zamieniamy numeru telefonu na int()?
# Numer telefonu nie jest liczbą, na której wykonujemy działania matematyczne. Jest ciągiem znaków. Dzięki temu nie tracimy zera, jeśli numer zaczyna się od zera.
phone = input('Enter phone number: ')

# Pobieramy pierwsze trzy znaki numeru.
# [0:3] oznacza znaki od indeksu 0 do indeksu 2.
first_group = phone[0:3]

# Pobieramy kolejne trzy znaki.
# [3:6] oznacza znaki od indeksu 3 do indeksu 5.
second_group = phone[3:6]

# Pobieramy ostatnie trzy znaki.
# [6:9] oznacza znaki od indeksu 6 do indeksu 8.
third_group = phone[6:9]

# Łączymy trzy grupy numeru za pomocą myślników.
# Operator + łączy teksty.
formatted_phone = first_group + '-' + second_group + '-' + third_group

# Wyświetlamy sformatowany numer telefonu.
# F-string pozwala wstawić wartość zmiennej do tekstu za pomocą {}.
print(f'Phone number: {formatted_phone}')