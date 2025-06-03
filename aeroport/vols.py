from aeroport.avions import Avion
from aeroport.utils import genere_immat, villes_random

class Vol:
    def __init__(self, num, dest, av:Avion):
        self.numero = num
        self.destination = dest
        self.avion = av

    """
    def afficher_infos(self):
        print(f"I={self.numero}, M={self.destination}")
        self.avion.afficher_infos()
    """

    def __str__(self):
        return f"I={self.numero}, M={self.destination}"

"""    
def creer_vol(numero, destination, avion):
    # Crée un dictionnaire représentant un vol avec un avion assigné.
    return Vol(numero,destination,avion)
"""


def creer_vols_fictifs(combien=0):
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
