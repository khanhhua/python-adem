# Machen wir Geldautomaten (zB bei Commerzbank)

print("Welcome to Commerzbank")

summe_geld = int(input("Wieviel Geld?"))
gewuenschte_muenze = int(input("Gewuenschte Muenze"))

print("Summe:", summe_geld)
print("Gewuenschte Muenze:", gewuenschte_muenze)

liste = [50, 20, 10, 5, 2, 1]
index = liste.index(gewuenschte_muenze)

for gewuenschte_muenze in liste[index:]:
  muenze_anzahl = summe_geld // gewuenschte_muenze
  rest_summe = summe_geld % gewuenschte_muenze

  print("")
  print("gewuenschter muenze:", gewuenschte_muenze)
  print("muenzen anzahl:", muenze_anzahl)
  
  if gewuenschte_muenze == 1: break
  summe_geld = rest_summe
