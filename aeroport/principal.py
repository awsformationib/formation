import json

from vols import creer_vols_fictifs
from utils import afficher_dict

# IF : le code en dessus ne s'execute que si ce code est le
# script d'entre aka script principal
#  n'execute pas si principal.py est utiliser par un autre fichier avec
#  'import principal'

if __name__=="__main__":

    # CAPTATION
    tous_les_vols = creer_vols_fictifs(49)

    # TRANSFORM
        #TODO

    # RESTITITUION
    for v in tous_les_vols:
       print(v)
       print(v.avion)



    for v in tous_les_vols[0:3]: # slice
        v.avion.decoller()

    print(tous_les_vols[0].avion.en_vol)
    print(tous_les_vols[4].avion.en_vol)

"""
    f = open("tous_les_vols.json", mode="wt", encoding="utf-8")
    json.dump(tous_les_vols, f, indent=4)
    f.close()
"""

# python une liste de dict dans un fichier json