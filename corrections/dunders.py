from aeroport.avions import Vehicule, Avion

entiers = [5,8,-1,77,99,0]

print(type(entiers[0]))

ent = sorted(entiers)

print(entiers)


v = Vehicule(100)
v.vitesse = 200
print(v)
v.vitesse = 300
print(v)

if v < 101:
    print("Vmax moins que 101")


a1 = Avion("B","",600)
a2 = Avion("A", vitesse=600)

if a1 < a2:
    print("a1<a2")
else:
    print("a1>=a2")

print(a2.modele)
a2.modele="SousMarin"