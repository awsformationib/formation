import logging

import config

from exporters import export_to_csv
from utils import creer_vols_fictifs


# IF : le code en dessus ne s'execute que si ce code est le
# script d'entre aka script principal
#  n'execute pas si principal.py est utiliser par un autre fichier avec
#  'import principal'


def main():
    config.init()

    logging.basicConfig(filename=config.PATHLOG / "exporters.log", encoding="utf-8", level=config.LEVEL
                        , format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    logging.info("Demarrage")

    # CAPTATION
    logging.debug("Creation Vols fictifs")
    tous_les_vols = creer_vols_fictifs(50000)

    # RESTITITUION FICHIERS
    export_to_csv("tous_les_vols.csv",tous_les_vols ) #TODO

    logging.debug("Lecture base")

    print(f"Total {len(tous_les_vols)}")

    logging.info("Arret du programme")

if __name__=="__main__":
    main()