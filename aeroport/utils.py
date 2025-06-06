from random import choice
from string import ascii_uppercase, digits

from avions import Avion
from vols import Vol


def afficher_dict(label, dico:dict):
    """Affiche proprement les éléments d’un dictionnaire."""
    print(f"\n📄 {label} :")
    for cle, valeur in dico.items():
        print(" - {} : {}".format(cle,valeur))


def genere_immat(taille=4,with_digit = False) -> str:
    chaine = ascii_uppercase
    chaine += digits if with_digit else ""
    lcode = [ choice(chaine) for _ in range(taille) ]
    return "".join(lcode)

"""
def genere_immat_old(taille=4, with_digit = False) -> str:
    code = ""
    chaine = ascii_uppercase+digits if with_digit else ascii_uppercase
    for _ in range(taille):
        code += choice(chaine)
    return code
"""

VILLES = ("Honolulu","Hong Kong","Marseille","Brisbane","Miami","Nantes")
def villes_random():
    return choice(VILLES)


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
