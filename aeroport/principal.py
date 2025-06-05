import json
import logging
from collections import defaultdict, Counter

import config
import databaselite
import databasemysql
from exporters import export_to_json, export_to_csv
from vols import creer_vols_fictifs, Vol

# IF : le code en dessus ne s'execute que si ce code est le
# script d'entre aka script principal
#  n'execute pas si principal.py est utiliser par un autre fichier avec
#  'import principal'

if __name__=="__main__":

    config.init()

    logging.basicConfig(filename=config.PATHLOG / "exporters.log", encoding="utf-8", level=config.LEVEL)

    logging.info("Demarrage")

    # CAPTATION
    tous_les_vols = creer_vols_fictifs(50)

    # RESTITITUION
    tous_les_vols.sort(key=lambda v1 : -1 * len(v1.destination))

    for v in tous_les_vols:
       print(v)
       print(v.avion)

    export_to_json("tous_les_vols.json",tous_les_vols )
    export_to_csv("tous_les_vols.csv",tous_les_vols ) #TODO

    vols_par_destination = defaultdict(list)
    for vol in tous_les_vols:
        vols_par_destination[vol.destination].append(vol)

    stats = Counter(vol.destination for vol in tous_les_vols)

    cnx = databasemysql.ouvrebase("127.0.0.1")
    #databasemysql.creer_base(cnx)

    last_vol = tous_les_vols[-1]
    for v in tous_les_vols:
        #
        pass
        #databasemysql.ecrire_vol(cnx,v)

    print(last_vol)
    #databaselite.lire_vol(cnx, last_vol.numero)
    records_lus = databasemysql.lire_vols(cnx)
    for r in records_lus:
        print(r)

    print(stats)

    logging.info("Arret du programme")


"""
def createinsqllite():
    cnx = databaselite.ouvrebase("formation.db")

    last_vol = tous_les_vols[-1]
    databaselite.ecrire_vol(cnx,last_vol)
    print(last_vol)
    #databaselite.lire_vol(cnx, last_vol.numero)
    databaselite.lire_vols(cnx)
"""