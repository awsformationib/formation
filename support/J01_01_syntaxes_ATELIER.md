![Logo](images\logo.png)


## 🧩 Fiche 1.1 – Variables, Types et Opérateurs (ATELIER)

```python
# vol_basique.py

# Données du vol
numero_vol = "AF1234"
ville_depart = "Paris"
ville_arrivee = "Toulouse"
heure_depart = "10:30"
distance_km = 604.3
en_retard = True

# Variante : vitesse de croisière estimée en km/h
vitesse_kmh = 850  # moyenne pour un vol commercial
temps_estime_h = distance_km / vitesse_kmh

# Affichage principal
statut = "En retard" if en_retard else "À l'heure"

message = (
    f"Le vol {numero_vol} part de {ville_depart} à {heure_depart} "
    f"en direction de {ville_arrivee} ({distance_km} km). "
    f"Statut : {statut}. "
    f"Durée estimée du vol : {temps_estime_h:.2f} heures."
)

print(message)
```

### Résultat attendu à l’exécution :

```
Le vol AF1234 part de Paris à 10:30 en direction de Toulouse (604.3 km). Statut : En retard. Durée estimée du vol : 0.71 heures.
```
