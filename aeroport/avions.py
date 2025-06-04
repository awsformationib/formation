import math
import uuid


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

    def deplace(self):
        pass

    def __reset(self):
        pass

    def _softreset(self): #protected
        pass

    def __str__(self):
        return f"{self.__class__.__name__} = {self.__vitesse_max}"

    def __lt__(self, other):
        if isinstance(other, Vehicule):
            return self.__vitesse_max < other.__vitesse_max
        elif isinstance(other, (int, float)):
            return self.__vitesse_max < other
        return False


class Avion(Vehicule): #avion herite de vehicule, le specialise
    def __init__(self, immatriculation, modele=None, vitesse = 800):
        super().__init__(vitesse)
        self.__id = str(uuid.uuid4())
        self.immatriculation = immatriculation
        self.__modele = modele
        self.en_vol = False

    @property
    def id(self):
        return self.__id

    @property
    def modele(self):
        return self.__modele if self.__modele else "N/A"

    # decollage
    def decoller(self):
        self.en_vol = True

    def atterrir(self):
        self.en_vol = False

    """
    def afficher_infos(self):
        print(f"I={self.immatriculation}, M={self.modele}")
    """

    # commence par __xxx__ : speciales / dunders (double_underscores)
    def __str__(self):
        return f"I={self.immatriculation}, M={self.__modele}"

    def __lt__(self, other):
        if isinstance(other, Avion):
            if self.immatriculation == other.immatriculation:
                return super().__lt__(other.__vitesse_max)
            return self.immatriculation < other.immatriculation
        elif isinstance(other,str):
            return self.immatriculation < other
        return False

"""
def creer_avion(code) -> Avion:    
    return Avion(code, None)
"""


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
        return f"I={self.immatriculation}, M={self.__modele}, T={self.tonnage}"

if __name__ == "__main__":
    # code de tests
    a1 = Avion("FDXX0","Airbus A320")
    a2 = Avion("BOZ1X", "Boeing 737 Max")

    gp1 = GrosPorteur("FZZ0","Airbus A380", 12000)
    gp1.decoller()

    print(a1)
    print(a2)
    print(gp1, gp1.__vitesse_max)

    print(dir(gp1))







