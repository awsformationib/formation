![Logo](images\logo.png)


## 🧩 Fiche 1.4 – Fonctions & portée (aka scope)

Voici le fichier **corrigé complet `fonctions_vols.py`**, intégrant tous les cas abordés dans la fiche 1.4 (fonctions simples, arguments `*args`, `**kwargs`, valeur par défaut, portée).

---

```
# fonctions_vols.py

# 1. Filtrer par destination
def filtrer_par_destination(vols, destination):
    """Retourne la liste des vols dont la destination correspond."""
    return [vol for vol in vols if vol["destination"] == destination]

# 2. Compter les vols par destination à partir d'une liste *args
def compter_vols_par_destination(*vols):
    """Retourne un dictionnaire comptant les vols par destination."""
    compteur = {}
    for vol in vols:
        dest = vol["destination"]
        compteur[dest] = compteur.get(dest, 0) + 1
    return compteur

# 3. Afficher des informations optionnelles sur un vol
def details_vol(**infos):
    """Affiche les informations complémentaires d’un vol."""
    print("📋 Détails du vol :")
    for cle, valeur in infos.items():
        print(f" - {cle} : {valeur}")

# 4. Annoncer un vol avec un statut par défaut
def statut_vol(numero, en_retard=False):
    """Affiche le statut du vol (retard ou à l’heure)."""
    statut = "En retard" if en_retard else "À l'heure"
    print(f"Vol {numero} - Statut : {statut}")

# 5. Exemple de portée de variable
vol_global = "AF999"

def test_portee():
    vol_local = "BA456"
    print("🔧 Dans la fonction :", vol_local)

# Exemple de données
vols = [
    {"numero": "AF123", "destination": "Nice"},
    {"numero": "BA456", "destination": "Londres"},
    {"numero": "AF124", "destination": "Nice"},
    {"numero": "LH789", "destination": "Berlin"},
]

# --- Démonstration des fonctions ---

print("\n🧪 1. Filtrage vers Nice :")
vols_nice = filtrer_par_destination(vols, "Nice")
for v in vols_nice:
    print(f"- {v['numero']} vers {v['destination']}")

print("\n🧪 2. Comptage des vols par destination :")
compte = compter_vols_par_destination(*vols)
for dest, nb in compte.items():
    print(f"- {dest} : {nb} vol(s)")

print("\n🧪 3. Affichage d'infos diverses :")
details_vol(pilote="Martin", avion="A320", piste=4)

print("\n🧪 4. Statut du vol :")
statut_vol("AF123")
statut_vol("BA456", en_retard=True)

print("\n🧪 5. Portée des variables :")
test_portee()
print("🔧 En dehors de la fonction :", vol_global)
```

---

### Résultat attendu (extrait) :

```
🧪 1. Filtrage vers Nice :
- AF123 vers Nice
- AF124 vers Nice

🧪 2. Comptage des vols par destination :
- Nice : 2 vol(s)
- Londres : 1 vol(s)
- Berlin : 1 vol(s)

🧪 3. Affichage d'infos diverses :
📋 Détails du vol :
 - pilote : Martin
 - avion : A320
 - piste : 4

🧪 4. Statut du vol :
Vol AF123 - Statut : À l'heure
Vol BA456 - Statut : En retard

🧪 5. Portée des variables :
🔧 Dans la fonction : BA456
🔧 En dehors de la fonction : AF999
```
