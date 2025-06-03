![Logo](images\logo.png)


## 🧩 Fiche 2.4 – Méthodes spéciales (CORRIGE)

---

### ✅ `vol_comparable.py` – Corrigé complet

```python
# vol_comparable.py

class Vol:
    def __init__(self, numero, destination):
        self.numero = numero
        self.destination = destination

    # Méthode d’affichage utilisateur
    def __str__(self):
        return f"Vol {self.numero} à destination de {self.destination}"

    # Méthode de représentation développeur
    def __repr__(self):
        return f"Vol('{self.numero}', '{self.destination}')"

    # Méthode de comparaison d’égalité
    def __eq__(self, other):
        if isinstance(other, Vol):
            return self.numero == other.numero
        return False

    # Méthode de comparaison d’ordre (tri)
    def __lt__(self, other):
        return self.numero < other.numero

    # Méthode pour rendre l’objet "hashable"
    def __hash__(self):
        return hash(self.numero)  # cohérent avec __eq__

# === Partie tests ===
if __name__ == "__main__":
    vols = [
        Vol("AF123", "Lyon"),
        Vol("AF456", "Nice"),
        Vol("AF123", "Paris"),
        Vol("BA789", "Londres"),
    ]

    print("✅ Affichage brut :")
    for vol in vols:
        print(vol)

    print("\n🔢 Tri des vols :")
    for vol in sorted(vols):
        print(repr(vol))

    print("\n🧹 Suppression des doublons via set :")
    vols_uniques = set(vols)
    for vol in vols_uniques:
        print(vol)

    print("\n🔁 Comparaison de deux objets :")
    v1 = Vol("AF123", "Lyon")
    v2 = Vol("AF123", "Paris")
    print("v1 == v2 ?", v1 == v2)
```

---

### ✅ Résultat attendu

```
✅ Affichage brut :
Vol AF123 à destination de Lyon
Vol AF456 à destination de Nice
Vol AF123 à destination de Paris
Vol BA789 à destination de Londres

🔢 Tri des vols :
Vol('AF123', 'Lyon')
Vol('AF123', 'Paris')
Vol('AF456', 'Nice')
Vol('BA789', 'Londres')

🧹 Suppression des doublons via set :
Vol AF123 à destination de Lyon
Vol AF456 à destination de Nice
Vol BA789 à destination de Londres

🔁 Comparaison de deux objets :
v1 == v2 ? True
```
