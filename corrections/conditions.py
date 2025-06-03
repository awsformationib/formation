"""if condition:
elif autrecondituon
else
"""
f_entiers = [0,1,1,2,3,5,8,13,21,34,55]
taille = len(f_entiers) # purement de la doc : taille d'une sequence/liste

for f in f_entiers:
    print(f)
else: #optionnel
    print("FIN")

saisie_ok = False
while not saisie_ok:
    saisie = input("Saisir un nombre entre 1 et 10 :?")
    val = int(saisie)
    saisie_ok = val>0 and val<11
else: #optionnel
    print("FIN")
