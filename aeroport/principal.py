import json

from aeroport.avions import Avion
from aeroport.encoders import VolEncoder
from vols import creer_vols_fictifs, Vol
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

    def compare(v1:Vol):
        return -1 * len(v1.destination)

    # RESTITITUION
    tous_les_vols.sort(key=compare)

    for v in tous_les_vols:
       print(v)
       print(v.avion)

    a = Avion("XYZ","Cessna")
    v1 = Vol("I1X214","Paris", a)
    v2 = Vol("I1X214", "Paris", a)

    print(v1 == v2)

    f = open("tous_les_vols.json", mode="wt", encoding="utf-8")
    json.dump(tous_les_vols,f,cls=VolEncoder, indent=4,  ensure_ascii=False)
    f.close()

# python une liste de dict dans un fichier json
