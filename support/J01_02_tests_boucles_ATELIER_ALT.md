![Logo](images\logo.png)


## 🧩 Fiche 1.2 – Conditions, Boucles, Fonctions (ATELIER ALT)

### 🧪 Variante : boucle `while` + file d’attente

```python
# gestion_vols_while.py

def peut_decoller(avion_pret: bool, piste_dispo: bool) -> bool:
    return avion_pret and piste_dispo

def afficher_statut(vol: dict) -> str:
    if peut_decoller(vol["pret"], vol["piste"]):
        return f"Le vol {vol['numero']} peut décoller."
    else:
        return f"Le vol {vol['numero']} ne peut pas décoller."

# Liste de vols comme file d’attente (FIFO)
vols = [
    {"numero": "AF123", "pret": True, "piste": True},
    {"numero": "BA456", "pret": False, "piste": True},
    {"numero": "LH789", "pret": True, "piste": False},
    {"numero": "IB321", "pret": True, "piste": True},
]

# Traitement séquentiel avec while
index = 0
print("🕑 Démarrage du traitement des vols en file d'attente...\n")
while index < len(vols):
    vol = vols[index]
    message = afficher_statut(vol)
    print(f"[{index+1}] {message}")
    index += 1

print("\n✅ Tous les vols ont été traités.")
```

---

### Résultat attendu :

```
🕑 Démarrage du traitement des vols en file d'attente...

[1] Le vol AF123 peut décoller.
[2] Le vol BA456 ne peut pas décoller.
[3] Le vol LH789 ne peut pas décoller.
[4] Le vol IB321 peut décoller.

✅ Tous les vols ont été traités.
```

---

Ce script introduit naturellement :

* la gestion d’une file d’attente
* le traitement par index (`while` classique)
* une manière de chronométrer ou simuler un planning
