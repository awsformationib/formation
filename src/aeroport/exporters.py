import logging
import json
import csv

from rich.progress import Progress

import config
from encoders import VolEncoder

#par default

def export_to_json(basename , list_vols) -> None :
    try:
        fullpath = config.PATHEXP / basename
        with open(fullpath, mode="wt", encoding="utf-8") as f:
            json.dump(list_vols, f, cls=VolEncoder, indent=4, ensure_ascii=False)
        logging.debug(f"Export file {fullpath} OK")
    except Exception as ex:
        logging.error(f"Erreur durant export de {fullpath} : {ex}")

def export_to_csv(basename , list_vols) -> None :
    # https://docs.python.org/fr/3/library/csv.html
    #v0 = list_vols[0]
    try:
        fullpath = config.PATHEXP / basename # fichier fullname
        with open(fullpath, mode='w', newline='') as csvfile: # newline neutralise ce que fait deja DictWriter
            entete = tuple(list_vols[0].__dict__.keys())
            print(entete)
            writer = csv.DictWriter(csvfile, fieldnames=entete, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
            writer.writeheader()

            # utilise rich.Progress
            with Progress() as progress:
                task = progress.add_task("[cyan]Génération du CSV...", total=len(list_vols))
                for i,v in enumerate(list_vols):
                    row:dict = v.__dict__
                    row["avion"] = row["avion"].immatriculation
                    row["statut"] = row["statut"].value
                    writer.writerow(row)
                    progress.update(task, advance=1)

            logging.debug(f"Export file {fullpath} OK")
    except Exception as ex:
        logging.error(f"Erreur durant export de {fullpath} : {ex}")




def export_to_database(db,list_vols):
    pass



