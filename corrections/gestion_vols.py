"""
def peut_decoller(piste_libre, carburant):
    # TODO si piste libre est carburant > 50 retourne True
    # sinon False
    if piste_libre and carburant>50: # le plus simple a gauche
        return True

    return False

#avec annotations
def peut_decoller_simple(piste_libre:bool, carburant_ok:int) -> bool:
    return piste_libre and carburant_ok>50

"""
# ------------------------------------------------------------------------
# CODE "PASSIF"
# ------------------------------------------------------------------------

# ------------ ATELIER ------------------
# Liste de vols à simuler
#  list de 3 vols (dict)
def peut_decoller(avion_pret: bool, num_piste_dispo:int) -> bool:
    return avion_pret and num_piste_dispo and num_piste_dispo>0

def afficher_status(vol:dict) -> None:
    message = f"Avion {vol["numero"]}/{vol["destination"]} "
    if peut_decoller(vol["pret"],vol["piste"]):
        message += "pret à decoller"
    else:
        message += "reste à l'arret"
    print(message)

"""
def filtre_destination_old(vols:list, arrivee:str) -> list:
    #Je veux les vols qui arrivent dans la ville precisee
    vols_filtres = []
    for v in vols:
        if "destination" in v and v["destination"] == arrivee:
            vols_filtres.append(v)
    return vols_filtres
"""

# liste en comprehension + function interne
def filtre_destination(vols:list, arrivee:str) -> list:
    """ Je veux les vols qui arrivent dans la ville precisee """
    def dest(vo,arrivee):
        return "destination" in vo and vo["destination"] == arrivee

    return [v for v in vols if dest(v,arrivee)]

"""
def pistes_utilises_old(vols_a_lire:list) -> list[int]:
    # Je veux les numeros uniques de pistes utilisees
    pistes = set()
    for v in vols_a_lire:
        if "piste" in v and v["piste"]:
            pistes.add(v['piste'])
    return pistes
"""

def pistes_utilises(vols_a_lire:list) -> list[int]:
    """Je veux les numeros uniques de pistes utilisees"""
    return {  v['piste'] for v in vols_a_lire  if "piste" in v and v["piste"]  }


# ------------------------------------------------------------------------
# PROGRAMME ACTIF
# ------------------------------------------------------------------------

vols = [
    {"numero": "AF123", "pret": True, "piste": 14, "destination":"Paris"},
    {"numero": "BA456", "pret": True, "piste": 8, "destination":"Nice"},
    {"numero": "LH789", "pret": True, "piste": None, "destination":"Toulouse"},
    {"numero": "AF163", "pret": True, "piste": 14, "destination": "Marseille"},
    {"numero": "BA476", "pret": None, "piste": 9, "destination": "Nice"},
    {"numero": "LH799", "pret": True, "piste": None, "destination": "Toulouse"}
]



print("*" * 50)
# appel pour connaitre les pistes utilisees

vols_pour_nice = filtre_destination(vols,'Nice')
# tester pour chacun de ces vols si il peut decoller
for vol in vols_pour_nice :  # iterer 'vols' -> chaque element dans une variable vol
    afficher_status(vol)
print("*" * 50)

print( "Pistes occupees" , pistes_utilises(vols_pour_nice) )



entiers = [1,2,3,4,5,8,9]
"""
carres = []
for v in entiers:
    if not v%2:
        carres.append( v**2)
"""

carres = [ v**2 for v in entiers if not v%2 ] #liste en comprehension
print(carres)

rcarres = { v:v**0.5 for v in entiers if not v%2 } # #dict en comprehension
print(rcarres)

entier = 10
if entier>10:
    resultat = entier /2
else:
    resultat = entier

resultat = entier/2 if entier>10 else entier # inline test ou ternaire


print(type(vols))
print(type(resultat))
print(type(filtre_destination))
