#Meilleurs print methodes

numero_vol = "AF1234"
# nom , contenu , type (str)
ville_depart = "Paris"
# nom , contenu , type (str)
ville_arrivee = "Toulouse"
heure_depart = 10  # int
minute_depart = 30 # int
distance_km = 604.3  # float
en_retard = 45  # bool

vitesse_km = 580                   #snake notation : bonne pratique
duree_vol = distance_km / vitesse_km

#Pure POO, version longue
gabarit = "Le vol {} part de {} est en retard de {:6d}, vol de {}"
message = gabarit.format(numero_vol, ville_arrivee, en_retard , duree_vol)
print(message)

#Formattage de Chaine
gabarit = "Le vol {:>20} part de {} est en retard de {}, vol de:{:1.4f}"
message = gabarit.format(numero_vol, ville_arrivee, en_retard , duree_vol)
print(message)


# sugar coding (raccourci)
# par mot clef (par variable
message = f"Le vol {numero_vol} depart de {ville_depart} duree {duree_vol:1.4f}"
print(message)

#old school (date de Python 2.x)
message = "Le vol %s depart de %s" % (numero_vol, ville_depart)
print(message)


# positionnement
greetings = "Bienvenue {0} {1}"
titre = "Madame"
nom = "Millet"
print(greetings.format(titre,nom))

# position relatif
greetings = "Konichiwa {1} {0}, happy {2:<5d} years"
titre = "San"
nom = "Lacour"
age = 24
print(greetings.format(titre,nom, age))

#https://docs.python.org/fr/3.5/library/string.html#formatexamples
