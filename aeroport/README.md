# Projet AirOps – Version Intégratrice (J1 + J2)

## Objectif
- POO : classes, instances, méthodes, encapsulation, dataclasses, Enum, méthodes spéciales
- Modules standards : datetime, random, uuid, collections, pathlib, csv, json, typing

## Structure
- `avion.py` : gestion des avions
- `vol.py` : gestion des vols
- `piste.py` : gestion des pistes
- `affectation.py` : liens vol-piste
- `simulateur.py` : génération aléatoire
- `exporter.py` : export CSV/JSON
- `main.py` : script principal

## Instructions
1. Exécutez `principal.py` :
    ```bash
    python principal.py
    ```
2. Vérifiez les fichiers générés dans le dossier `exports/` :
    - `tous_les_vols.csv` : tableau des vols
    - `tous_les_vols.json` : fichier JSON structuré
    - `formation.vols` : Base de données MySql ou SqlLite mise a jours avec des vols
3. 
4. Pour explorer :
    - Ajoutez d’autres formats d’export
    - Étendez les statistiques avec `collections.Counter`
    - Ajoutez une interface simple (console ou GUI)
