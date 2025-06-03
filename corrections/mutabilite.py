import string

#collections

listA = [1,2] # mutable  (set, dict)
listA[0] = 5

tupleA = tuple(listA) # NON mutable
# tuple[0] = 5

# int, str, float, bool, NoneType

prenom1 = "antoine"
print(id(prenom1))

prenom1 = prenom1 + "."
print(id(prenom1))

i = 5
print(id(i))
i+=8
print(id(i))


prenom1 = "antoine"
prenom2 = "antoine"
print("--------------")
print(id(prenom1), id(prenom2))
prenom2 = "Antoine"
print("--------------")
print(id(prenom1), id(prenom2))

prenom2.capitalize()
print(prenom2)
lady = prenom2.replace("e","ette")
print(prenom2, lady)

liste_longue_de_str = []
for i in range(100_000_000):
    liste_longue_de_str.append(string.ascii_letters[i%26])


for s in liste_longue_de_str:
    s = s + "*" #  3 * 100_000_000 + 1

del liste_longue_de_str



