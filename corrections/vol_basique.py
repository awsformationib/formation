
# variables

numero_vol = "AF1234"
# nom , contenu , type (str)
ville_depart = "Paris"
# nom , contenu , type (str)
ville_arrivee = "Toulouse"
heure_depart = 10  # int
minute_depart = 30 # int
distance_km = 604.3  # float
en_retard = True  # bool


print( en_retard )
print( type(en_retard))

# Typage est dynamique en_reatd devient un entier
en_retard = 10
print( en_retard )
print( type(en_retard))

# expression : + - * / %
# operateur est contextuel

print(1 + 1)
print("Il fait " + "beau")

print(1 * 5)
print("-" * 5)

tirets = "-" * 20
print(tirets)

en_retard = True
message = ("Le vol " + str(numero_vol) + " part de " + ville_depart
           + " est en retard de " + str(en_retard))
print(message)

print( en_retard )
print( type(en_retard))

vitesse_km = 580                   #snake notation : bonne pratique
duree_vol = distance_km / vitesse_km

print(message + " duree "+ str(duree_vol))

chaine = "100.5"
valeur = float( chaine )
print(type(valeur), type(chaine))

# str, float , int, bool : fonctions qui permettent de transformer

en_retard = False
t = str(en_retard)
print(t)

entier = 5
print( bool(entier))

prenom = "Sebastien"
print( bool(prenom))

vide = ""
print( bool(vide))


# Outsider
contenu = None # equivalent de null, NUL
print(contenu , type(contenu))







