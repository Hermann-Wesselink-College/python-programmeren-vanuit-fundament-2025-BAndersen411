for i in range(1,11):
 print(str(i) + " keer 3 = " + str(i * 3))

for i in range(1,11):
 print(str(i) + " keer " + str(5) + " = " + str(i * 5))

if 5 <= 0 or 5 > 10:
 print("Error")
else:
 for i in range(1,11):
    print(str(i) + " keer " + str(5) + " = " + str(i * 5))


mile = 1.609
print('Km/Miles')
for i in range(1,11):
 miles = i * mile
 print(str(i) + '\t' + str(miles))


getal = int(input("Van welk getal wil je de faculteit?"))
uitkomst = 1
for i in range(1, getal + 1):
  uitkomst = uitkomst * i
 
print(str(uitkomst))

for i in range(0,50,2):
  print(i)

for i in range(0,51,2):
  print(i)

minPlus = False
uitkomst = 1
 
for i in range(3,100000,2):
  if minPlus:
    uitkomst = uitkomst + (1/i)
  else:
    uitkomst = uitkomst - (1/i)
  minPlus = not minPlus
 
print(4*uitkomst)

tekst = input('Geef mij een word.')
for i in tekst:
    print(i)