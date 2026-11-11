# Dane z zadania:
# Cała populacja świata: 8 miliardów.
# Półkula północna: 7,2 miliarda.
# Półkula południowa: pozostała część populacji.

# A program that calculates the population of both hemispheres.
# Program oblicza liczbę ludności na obu półkulach Ziemi.

# Zapisujemy całkowitą liczbę ludności świata.
total = 8000000000

# Zapisujemy liczbę ludności półkuli północnej.
north = 7200000000

# Obliczamy liczbę ludności półkuli południowej.
south = total - north

# Wyświetlamy całkowitą liczbę ludności świata.
print("World population: ", total)

# Wyświetlamy liczbę ludności półkuli północnej.
print("Northern Hemisphere: ", north)

# Obliczamy i wyświetlamy procent ludności półkuli północnej.
print("Northern Hemisphere in %: ", north / total * 100)

# Wyświetlamy liczbę ludności półkuli południowej.
print("Southern Hemisphere: ", south)

# Obliczamy i wyświetlamy procent ludności półkuli południowej.
print("Southern Hemisphere in %: ", south / total * 100)