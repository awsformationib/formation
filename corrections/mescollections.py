

# list : sequence de valeurs ordonnées , modifiable
print("* " * 50)

entiers = [ 1,5,8,99,-1, 8, 5,1 , -1]   #sugar coding

a_remplir = []
a_remplir = list()
valeurs = [ "manon", 8000000000, None, "paris", True , 25 ]
print('prenom ' , valeurs[0])
valeurs[0] = "amandine"

taille = len(valeurs)
print(taille)
print(valeurs)

valeurs.insert(0,'madame')

taille = len(valeurs)
print(taille)
print(valeurs)

print("*" * 50)

while valeurs:
    print(valeurs.pop(0))

print("*" * 50)

print(entiers)
entiers.sort()
print(entiers)

# tuple :   sequence de valeurs ordonnées , NON modifiable
print("* " * 50)
t_entiers = ( 1,5,8,99,-1, 8)
print(type(t_entiers))
position = t_entiers.index(99)
print(t_entiers[0])
# t_entiers[0] = 10

# set :  sequence de valeurs NON ordonnées , modifiable
print("* " * 50)
s_entiers = set()
s_entiers = { 1,5,8,99,-1, 8 }
s_entiers.add(100)
print(s_entiers)
if 99 in s_entiers:
    print("99 est bien dans cette sequence")

#set n'a pas d'ordre donc doublons impossibles

entiers_uniq = list(set(entiers))
print(entiers_uniq)

seta = {4,5,6,7,8,9,1,2,3}
setb = {8,9,10,11}

print("A" , seta)
print("B" , setb)
print("DIFF A/B" ,  seta.difference(setb))
print("DIFF A/B" ,  setb.difference(seta))
print("DIFF A inter B" ,  setb.intersection(seta))

t_impairs = (1,3,5,7,9)
print("DIFF A diff Impairs " ,seta.difference( t_impairs ) )

# dict : kv, clef-valeur : sequence KV modifiable, non ordonnee
print("* " * 50)
d_entiers = dict()
d_entiers = { 1:"one",5:"five",8:"eight",99:"ninety nine",-1:"minus one", "CINQ":"five"}
print(type(d_entiers))

print(d_entiers)
print(d_entiers.keys())
print(d_entiers.values())

print(d_entiers.items()) # liste de tuples

"""
for key in d_entiers.keys():
    print(key)
for val in d_entiers.values():
    print(val)
"""

for tx in d_entiers.items()    :
    print(tx[0], tx[1])

for cle,valeur in d_entiers.items()    :
    print(cle, valeur)


info_perso = { 'date_formation':"02062025", "formation":249, "nom":"marc", "prenom":"lucas"}
t_perso = ("marc", "lucas", "02062025", 249)

print(info_perso["prenom"])
info_perso["prenom"] = "jean" # modifiable

print(info_perso)
# for k in info_perso.keys():
for k in info_perso:
    print(k, info_perso[k])

cle = "ville"
if cle in info_perso:
    print(info_perso["ville"])
else:
    print(f"Pas de {cle} dans ces infos")



