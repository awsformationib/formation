![Logo](images\logo.png)

## 🧩 Fiche 4.1 – `pip`, `venv` et gestion des dépendances Python

---

### 🎯 **Objectif**

Comprendre :
✅ Comment isoler son environnement Python avec `venv`.
✅ Comment installer et gérer des packages externes avec `pip`.
✅ Pourquoi il est essentiel de maîtriser ces outils dans tout projet Python (y compris AirOps).

---

### 🔎 **Pourquoi isoler l’environnement ?**

Sans environnement virtuel :
❌ Tous les projets utilisent la même installation système.
❌ Les versions de packages peuvent entrer en conflit entre projets.
❌ Il devient difficile de reproduire un environnement à l’identique sur une autre machine.

Avec un environnement virtuel (`venv`) :
✅ Chaque projet a ses propres versions de Python et de packages.
✅ On peut reproduire l’environnement avec un simple fichier `requirements.txt`.
✅ On garde son système propre et stable.

---

### 🛠 **Créer un environnement virtuel avec `venv`**

```
# Créer un nouvel environnement
python -m venv venv

# Activer sous Linux/macOS
source venv/bin/activate

# Activer sous Windows
venv\\Scripts\\activate

# Vérifier que l'environnement est actif
which python
```

---

### 📦 **Installer des packages avec `pip`**

```
# Installer un package
pip install requests

# Vérifier les packages installés
pip list

# Sauvegarder les dépendances
pip freeze > requirements.txt

# Restaurer les dépendances sur une autre machine
pip install -r requirements.txt
```

---

### ✈️ **Application au projet AirOps**

Exemples de dépendances externes utiles :

* `rich` → pour améliorer l’affichage console.
* `matplotlib` → pour générer des graphiques.
* `pandas` → pour manipuler les données des vols.
* `flask` ou `fastapi` → pour exposer une API autour de la flotte.

---

### 📋 **Résumé**

| Commande clé                      | Usage                                        |
| --------------------------------- | -------------------------------------------- |
| `python -m venv venv`             | Créer un environnement isolé.                |
| `source venv/bin/activate`        | Activer l’environnement (Linux/macOS).       |
| `venv\\Scripts\\activate`         | Activer l’environnement (Windows).           |
| `pip install X`                   | Installer un package externe.                |
| `pip freeze > requirements.txt`   | Sauvegarder les versions installées.         |
| `pip install -r requirements.txt` | Recréer un environnement identique ailleurs. |

---

### 🧪 **Questions rapides**

1. Que se passe-t-il si tu installes un package sans activer ton `venv` ?
2. Pourquoi faut-il versionner le fichier `requirements.txt` dans ton projet (mais pas le dossier `venv`) ?
3. Comment géres-tu un projet qui a besoin de plusieurs versions de Python (ex. Python 3.9 et 3.11) ?

---
