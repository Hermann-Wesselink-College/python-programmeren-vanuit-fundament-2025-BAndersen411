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


