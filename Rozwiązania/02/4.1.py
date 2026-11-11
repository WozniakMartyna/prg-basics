# Musimy rozszerzyć program o dwie nowe zmienne: age (wiek) i height (wzrost). Dodatkowo program ma obliczyć, ile lat będzie miała osoba za 6 lat.

# A program that prints student's personal data.
# Program wyświetla dane osobowe ucznia.

# Zapisujemy imię ucznia.
name = "Adam"

# Zapisujemy wiek ucznia.
age = 20

# Zapisujemy wzrost ucznia w centymetrach.
height = 180

# Wyświetlamy imię za pomocą f-string.
# f"..." – tworzy f-string, czyli tekst, w którym można umieszczać wartości zmiennych w nawiasach {}.
# {name} – wstawia wartość zmiennej name do tekstu.
print(f"My name is {name}.")

# Wyświetlamy wiek i wzrost ucznia.
print(f"I am {age} years old, and my height is {height} cm.")

# Obliczamy wiek za 6 lat i wyświetlamy wynik.
# {age + 6} – najpierw oblicza działanie, a następnie wstawia wynik do tekstu.
print(f"In 6 years I will be {age + 6} years old.")