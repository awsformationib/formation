# extraire une partie de

listeA = [1, 2, 3, -4, 5, 6, 10, 11]
listeA[0:2]
listeA[1:4]
listeA[4:]
listeA[1:8:2]
print(listeA[::-3])
print(listeA[-6:-2:])
print(listeA[-2:-4:-1])

list, tuple,set,dict, str

for i,v in enumerate(set(listeA)):
    print(i,"--->",v)

print("sebastienleclerc"[::2])

for c in "cedricparmentier":
    print(c)
joursemaine = "mardi"
print(joursemaine[3:1:-1])






