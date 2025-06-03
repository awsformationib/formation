![Logo](images\logo.png)


## 🧩 Fiche 1.2 – Conditions, Boucles, Fonctions (ATELIER)

```python
# gestion_vols.py

def peut_decoller(avion_pret: bool, piste_dispo: bool) -> bool:
    """Renvoie True si l'avion est prêt et une piste est disponible."""
    return avion_pret and piste_dispo

def afficher_statut(vol: dict) -> str:
    """Construit un message indiquant si le vol peut décoller ou non."""
    if peut_decoller(vol["pret"], vol["piste"]):
        return f"Le vol {vol['numero']} peut décoller."
    else:
        return f"Le vol {vol['numero']} ne peut pas décoller."

# Liste de vols à simuler
vols = [
    {"numero": "AF123", "pret": True, "piste": True},
    {"numero": "BA456", "pret": False, "piste": True},
    {"numero": "LH789", "pret": True, "piste": False},
]

# Traitement de chaque vol
for vol in vols:
    message = afficher_statut(vol)
    print(message)
```

### Résultat attendu à l’exécution :

```
Le vol AF123 peut décoller.
Le vol BA456 ne peut pas décoller.
Le vol LH789 ne peut pas décoller.
```
