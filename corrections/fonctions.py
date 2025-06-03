import math

# definition classique de fct

# valS par defaut en dernier , NON interrompu
def calcul_complique(x:int,y:float = 0, message="") -> float:
    resultat =  math.sqrt(3*x**2 + 2*y + 5)
    print(message, resultat)
    return resultat



# utilisation simple
t = 8
u = 5.2

# Position / KW tous les params
calcul_complique(u,t, "Je calcule") # par position : positional
calcul_complique(x=t, y=u, message="Je calcule") # par motclef /keyword
calcul_complique(x=t, message="Je calcule", y=u) # par motclef /keyword
calcul_complique(message="Je calcule", y=u, x=t) # par motclef /keyword

# Position / KW PAS tous les params
calcul_complique(u,t) # par position : positional pas tous les params
calcul_complique(x=t, y=u) # par kw : positional pas tous les params

# position FIRST , kw AFTER
calcul_complique(5,8, message="J'ai encore fais un calcul") # mix position / kw
# calcul_complique(message="J'ai encore fais un calcul", 5,8) # mix position / kw

calcul_complique(3)

# fonction connue
"""
print(*values: object,
          sep: str | None = " ",
          end: str | None = "\n",
          file: SupportsWrite[str] | None = None,
          flush: Literal[False] = False) -> None
"""

print(5,6,7,8, sep=";", end=" / " )
print(9,10,11,12, sep=";" )

"""
def somme(a,b,c):
    return a+b+c
"""
# Nbre variable de params POSITIONEL  *args
def somme(*vals, val_init=0): # nbre variables de parametres
    som=val_init
    for v in vals:
        som+=v
    return som

print(somme(val_init=0))
print(somme(1,5,9,8,10,val_init=20))

# Nbre variable de params KEYWORDS  **kwargs

def info_a_afficher(**infos):
    for cle,val in infos.items():
        print(cle,val,type(val), sep="=", end=" ")
    print()


info_a_afficher(prenom="cedric", nom="parmentier", formation="python")
info_a_afficher(batiment="atlantic", etage=18, annee=1997)

# position, kw, val par default, *args (tuple), **kwargs(dict)

def supergenerique(*args, **kwargs):
    print(args)
    print(kwargs)

supergenerique(1,5,7, message="hello", postfix=".")
print(supergenerique())

