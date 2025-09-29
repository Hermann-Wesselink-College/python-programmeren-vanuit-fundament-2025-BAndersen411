# opdrachten 1 tot en met 3 van pragraaf 2.8
prijs = 24.49
print('Prijs:', prijs)

voornaam = "Henk"
achternaam = "de Vries"
naam = voornaam, achternaam
naamLengte = len(naam)
print('Mijn naam is', naam)
print('Mijn naam bestaat uit', str(naamLengte) , ' letters')
print(voornaam.lower())
print(achternaam.upper())

voornaam = input('Wat is jouw voornaam')
achternaam = input('wat is jouw achternaam')
naam = voornaam, achternaam
naamlengte = len(naam)
print('je naam is', naam)
print('je naam bestaat uit ', str(naamLengte), ' letters (inclusief spaties)')