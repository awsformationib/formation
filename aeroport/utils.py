import datetime
import random
from random import choice
from string import ascii_uppercase, digits


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

