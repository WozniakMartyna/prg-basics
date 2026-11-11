# Program ma wyświetlić numeryczne reprezentacje podanych znaków. Do tego wykorzystujemy funkcję ord().

# Program wyświetla numeryczne kody wybranych znaków.

# Funkcja ord() zwraca kod liczbowy podanego znaku.
# Znak musi być zapisany jako tekst w cudzysłowie lub apostrofach.

# Wyświetlamy kod małej litery a.
# F-string pozwala wstawić znak i wynik funkcji ord() do tekstu.
print(f"a {ord('a')}")

# Wyświetlamy kod małej litery b.
print(f"b {ord('b')}")

# Wyświetlamy kod małej litery z.
print(f"z {ord('z')}")

# Wyświetlamy kod wielkiej litery A.
print(f"A {ord('A')}")

# Wyświetlamy kod wielkiej litery B.
print(f"B {ord('B')}")

# Wyświetlamy kod wielkiej litery Z.
print(f"Z {ord('Z')}")

# Wyświetlamy kod cyfry 1.
print(f"1 {ord('1')}")

# Wyświetlamy kod znaku równości.
print(f"= {ord('=')}")

# Wyświetlamy kod znaku plus.
print(f"+ {ord('+')}")

# Wyświetlamy kod symbolu euro.
print(f"€ {ord('€')}")