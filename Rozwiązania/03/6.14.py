# W tym zadaniu sprawdzamy, czy osoba posiada co najmniej dwa konta spośród Facebooka, Twittera i Instagrama.
# True oznacza, że osoba posiada dane konto, a False oznacza, że go nie posiada.

facebook = True
twitter = False
instagram = True

# and oznacza "i" – oba połączone warunki muszą być prawdziwe.
# or oznacza "lub" – wystarczy, że przynajmniej jeden z połączonych warunków będzie prawdziwy.
# Sprawdzamy wszystkie trzy możliwe pary posiadanych kont.
if (facebook and twitter) or (facebook and instagram) or (twitter and instagram):
    print('You are a good influencer!')
else:
    print('You are not a good influencer.')

# Dlaczego sprawdzamy trzy pary kont?
# Ponieważ osoba może posiadać dowolne dwa konta z trzech dostępnych platform.
# Wystarczy spełnienie jednej z tych trzech kombinacji.