import math

class Vehicule: # generalise Avion

    def __init__(self):
        self.vitesse_max = 999

    def deplace(self):
        pass


class Avion(Vehicule): #avion herite de vehicule, le specialise
    def __init__(self, immatriculation, modele=None, **caracteristiques):
        super().__init__()
        self.immatriculation = immatriculation
        self.modele = modele
        self.en_vol = False

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
        return f"I={self.immatriculation}, M={self.modele}"

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
    print(gp1, gp1.vitesse_max)








