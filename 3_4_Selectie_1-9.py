#
bedrag = 100
if bedrag > 150:
  print(bedrag * 1.19)
else:
  print(bedrag * 1.16) 


bedrag = 10
if bedrag > 150:
  print(bedrag * 1.19)
elif bedrag < 55:
  print(bedrag * 1.11)
else:
  print(bedrag * 1.16)


  bedrag = float(input('Voer een bedrag in'))
if bedrag > 150:
  print(bedrag * 1.19)
elif bedrag < 55:
  print(bedrag * 1.11)
else:
  print(bedrag * 1.16)


bedrag = 100
if bedrag > 150:
  print(bedrag * 1.19)
else:
  print(bedrag * 1.16) 

  bedrag = 10
if bedrag > 150:
  print(bedrag * 1.19)
elif bedrag < 55:
  print(bedrag * 1.11)
else:
  print(bedrag * 1.16)

  bedrag = float(input('Voer een bedrag in'))
if bedrag > 150:
  print(bedrag * 1.19)
elif bedrag < 55:
  print(bedrag * 1.11)
else:
  print(bedrag * 1.16)

  bedrag = float(input("Voer een bedrag in"))
if bedrag > 150:
  nieuwBedrag = bedrag * 1.19
  print("Na verhoging met 19% is de prijs: ?" + str(nieuwBedrag))
elif bedrag < 55:
  nieuwBedrag = bedrag * 1.11
  print("Na verhoging met 11% is de prijs: ?" + str(nieuwBedrag))
else:
  nieuwBedrag = bedrag * 1.16
  print("Na verhoging met 16% is de prijs: ?" + str(nieuwBedrag))

spaargeld = float(input('Voer in hoeveel spaargeld je hebt.'))

if spaargeld <= 1000:
    print('Je moet een betere baan vinden.')
elif 1000 < spaargeld < 1500:
    print('Je bent er bijna, maar toch even nog sparen.')
elif spaargeld >= 1500:
    print('Je mag je scooter kopen!')

leeftijd = float(input("Wat is je leeftijd?"))
stempasOntvangen = input("Heb je een stempas ontvangen? (ja/nee)")
 
if leeftijd >= 16:
  print("Je mag praktijkexamen voor je scooterrijbewijs doen.")
else:
  print("Je mag geen praktijkexamen voor je scooterrijbewijs doen.")
if leeftijd >= 18:
  if stempasOntvangen == "nee":
    print("Je mag niet stemmen, want je hebt (nog) geen stempas ontvangen!")
  else:
    print("Je mag stemmen.")
else:
  print("Je mag niet stemmen.")


from datetime import datetime
uur = datetime.now().hour
 
if uur < 6:
  print("Het is nacht")
elif uur < 12:
  print("Het is ochtend")
elif uur < 18:
  print("Het is middag")
else:
  print("Het is avond")

from datetime import datetime
uur = datetime.now().hour
temperatuur = 21
luchtvochtigheid = 80
 
if uur < 8 or uur >= 17:
  print("Airco uit")
else:
  if temperatuur < 20 and luchtvochtigheid < 85:
    print("Airco uit")
  else:
    print("Airco aan")



    	#Vraag de lengte van de zijden
zijde1 = int(input("Hoe lang is zijde 1?"))
zijde2 = int(input("Hoe lang is zijde 2?"))
zijde3 = int(input("Hoe lang is zijde 3?"))
 
#Bepaal wat de langste zijde is
#en wat de twee kortste
if zijde1 < zijde3 and zijde2 < zijde3:
  langste = zijde3
  nietLangste1 = zijde1
  nietLangste2 = zijde2
elif zijde1 < zijde2 and zijde3 < zijde2:
  langste = zijde2
  nietLangste1 = zijde1
  nietLangste2 = zijde3
else:
  langste = zijde1
  nietLangste1 = zijde2
  nietLangste2 = zijde3
 
#Controleer of de kortste 2 samen langer zijn dan de langste
if nietLangste1 + nietLangste2 > langste:
  print("Dat is een driehoek!")
else:
  print("Dit kan geen driehoek zijn.")
 