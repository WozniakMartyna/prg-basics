# ZADANIE 09.2.5:
# Połączenie dwóch zbiorów kontaktów bez powtarzających się adresów.

# Pierwsza lista kontaktów.
contacts_A = {
    "john@example.com",
    "alice@example.com",
    "bob@example.com"
}

# Druga lista kontaktów.
contacts_B = {
    "bob@example.com",
    "michael@example.com",
    "sara@example.com"
}

# Operator | łączy oba zbiory.
# Adres bob@example.com występuje w obu, ale w wyniku będzie tylko raz.
merged_contacts = contacts_A | contacts_B

# Wyświetlamy połączony zbiór kontaktów.
print("Merged contacts:", merged_contacts)


# | – łączy dwa zbiory.
# Powtarzające się elementy zostają uwzględnione tylko raz.
# Nie należy zakładać konkretnej kolejności elementów podczas wyświetlania.