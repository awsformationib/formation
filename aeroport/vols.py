from datetime import datetime
from typing import List, Optional

from aeroport.avions import Avion
from aeroport.utils import genere_immat, villes_random

from enum import Enum

class StatutVol(Enum):
    PREVU = "prevu"
    EN_COURS = "en cours"
    TERMINE = "terminé"

class Vol:
    def __init__(self, num, dest, av:Avion):
        self.numero = num
        self.destination = dest
        self.avion = av
        self.statut = StatutVol.PREVU
        self.heure_creation = datetime.now()
        self.heure_decollage = None
        self.heure_arrivee = None

    def duree_de_vol(self):
        if self.heure_decollage and self.heure_arrivee:
            return self.heure_arrivee - self.heure_decollage #timedelta
        return None

    def decoller(self):
        self.heure_decollage = datetime.now()
        self.statut = StatutVol.EN_COURS

    def atterrir(self):
        self.heure_arrivee = datetime.now()
        self.statut = StatutVol.TERMINE

    def __str__(self):

        dts =(self.heure_creation,self.heure_decollage,self.heure_arrivee)
        dstr = ""
        for d in dts:
            dstr +=str(d)+"/"
        return f"numero={self.numero}, modele={self.destination} "+dstr

    # sort, comparaison (par default)
    def __lt__(self, autre_vol):
        if self.destination == autre_vol.destination:
            return self.numero < autre_vol.numero
        return self.destination < autre_vol.destination

    def __eq__(self, autre_vol):
        return self.destination == autre_vol.destination and self.numero == autre_vol.numero


def creer_vol():
    avion = Avion(genere_immat())

    # creation vol (qui fait ref a l'avion)
    nvol = genere_immat(with_digit=True, taille=6)
    nville = villes_random()
    return Vol(nvol, nville, avion)

def creer_vols_fictifs(combien=0) -> list:
    tous_les_vols = []
    for _ in range(combien):
        #creation avion
        avion = Avion( genere_immat() )

        #creation vol (qui fait ref a l'avion)
        nvol = genere_immat(with_digit=True,taille=6)
        nville = villes_random()
        vol = Vol( nvol , nville, avion )

        # mise dans un SET
        tous_les_vols.append(vol)


    return tous_les_vols

if __name__=="__main__":
    v = creer_vol()
