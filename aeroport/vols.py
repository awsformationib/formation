from datetime import datetime

from aeroport.avions import Avion

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
        self._heure_creation = datetime.now()
        self.heure_decollage = None
        self.heure_arrivee = None

    @property
    def heure_creation(self):
        if not self._heure_creation: return ""
        return self._heure_creation

    @heure_creation.setter
    def heure_creation(self, d):
        self._heure_creation = d

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



