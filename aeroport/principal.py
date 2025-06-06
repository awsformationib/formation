import logging
from collections import defaultdict, Counter

import pandas as pd

import config
from database import VolMySql, WithPandas

from exporters import export_to_json, export_to_csv
from utils import creer_vols_fictifs


# IF : le code en dessus ne s'execute que si ce code est le
# script d'entre aka script principal
#  n'execute pas si principal.py est utiliser par un autre fichier avec
#  'import principal'


def main():
    config.init()

    logging.basicConfig(filename=config.PATHLOG / "exporters.log", encoding="utf-8", level=config.LEVEL)

    logging.info("Demarrage")

    # CAPTATION
    logging.debug("Creation Vols fictifs")
    tous_les_vols = creer_vols_fictifs(50)

    # RESTITITUION ECRAN
    tous_les_vols.sort(key=lambda v1 : -1 * len(v1.destination))
    for v in tous_les_vols:
       print(v)

    # RESTITITUION FICHIERS
    export_to_json("tous_les_vols.json",tous_les_vols )
    export_to_csv("tous_les_vols.csv",tous_les_vols ) #TODO

    vols_par_destination = defaultdict(list)
    for vol in tous_les_vols:
        vols_par_destination[vol.destination].append(vol)

    # VERS DATABASE (sqllite si pas possible)
    db = VolMySql(host="127.0.0.1", login="root", password="", database="formation")
    #db.creer_base(cnx)

    logging.debug("Ecriture base")
    for v in tous_les_vols:
        db.ecrire_vol(v)

    logging.debug("Lecture base")
    # ON LIT A NOUVEAU DANS LA BASE
    records_lus = db.lire_vols()
    for r in records_lus:
        print(r)


    logging.info("Arret du programme")

if __name__=="__main__":
    main()