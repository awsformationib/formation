import math

min(1,2,3)

rezult = zip([1,2,3,4],("C","B","D"))
for i in rezult:
    print(i)

#help(print)
#help(math)

chaine = ""

def sansunderscore(chaine):
    return not chaine.startswith("__")

# for f in [ f for f in dir(chaine) if not f.startswith("__")]:
for f in filter(sansunderscore, dir(chaine)):
    print(f, end=" , ")
print()
voitures = ["ferrari","alpine","renault", "bmw", "Fiat", "rover", "ford"]

"""
    4) afficher la liste des voitures 1 : restitution / print(final)
    1) commencant par f,                : selection / filter
    2) en majuscules,                   : transfo / map
    3) trié                             : tri / sorted
"""

voitures = ["ferrari","alpine","renault", "bmw", "Fiat", "rover", "ford", "RR"]
annees = [1954,1980,1938, 1924, 1953, 1925, 1912, 1992]
def f_only(chaine):
    return chaine.startswith("R") or chaine.startswith('r')
def transform(chaine):
    idx = voitures.index(chaine)
    return annees[idx], chaine.upper()
def by_size(tu):   # pas encore utilisé
    return len(tu[1])


#HYPER FLEXIBLE
# COLLECT
iter1 = filter(f_only,voitures)
print(iter1)
# TRANS
iter2 = map(transform, iter1)
print(iter2)
iter3 = sorted(iter2, key=by_size, reverse=True)

#RESTITUTION
print(iter3)



