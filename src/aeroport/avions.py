import math
import uuid
from dataclasses import field, dataclass


class Vehicule: # generalise Avion

    def __init__(self, v = 0):
        self.vitesse = v

    @property
    def vitesse(self):
        return self.__vitesse_max;

    @vitesse.setter
    def vitesse(self,v):
        if v>0:
            self.__vitesse_max = v
        else:
            raise ValueError(f"La vitesse donnée est erronnée {v}")

@dataclass(order=True, init=True)
class Avion(Vehicule):
    immatriculation: str
    modele: str
    en_vol:bool = field(default_factory=lambda: False)
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def __str__(self) -> str:
        return f"{self.immatriculation} ({self.modele})"

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,i):
        self.__id = i

    @property
    def modele(self):
        return self.__modele if self.__modele else "N/A"

    @modele.setter
    def modele(self, mod):
        self.__modele = mod


    # decollage
    def decoller(self):
        self.en_vol = True

    def atterrir(self):
        self.en_vol = False

    # commence par __xxx__ : speciales / dunders (double_underscores)
    def __str__(self):
        return f"I={self.immatriculation}, M={self.__modele}"


class GrosPorteur(Avion):

    def __init__(self, immatriculation, modele=None, tonnage=10000):
        super().__init__(immatriculation,modele)
        self.tonnage = tonnage
        self.restant = self.tonnage

    def charger(self, poids_chargement):
        if poids_chargement<=self.restant:
            self.restant-=poids_chargement
        else:
            print("Tonnage maximum atteint")

    #dunders
    def __str__(self):
        return f"I={self.immatriculation}, M={self.modele}, T={self.tonnage}"

if __name__ == "__main__":
    # code de tests
    a1 = Avion("FDXX0","Airbus A320")
    a2 = Avion("BOZ1X", "Boeing 737 Max")

    gp1 = GrosPorteur("FZZ0","Airbus A380", 12000)
    gp1.decoller()

    print(a1)
    print(a2)
    print(gp1)

    print(dir(gp1))







