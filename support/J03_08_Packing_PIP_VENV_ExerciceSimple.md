![Logo](images\logo.png)


## 🛠 Mini-exercice pratique – Manipuler `pip`, `venv` et les dépendances

---

### 🎯 **Objectif de l’exercice**

Mettre en place un environnement Python isolé pour AirOps, installer des dépendances externes, et comprendre comment exporter/importer la liste des packages pour partager un projet proprement.

---

### 📝 **Étapes à suivre**

---

### 1️⃣ Créer l’environnement virtuel

✅ Dans un nouveau dossier nommé `airops_env_test`, créez un environnement virtuel :

```
python -m venv venv
```

✅ Activez l’environnement :

* Sous Linux/macOS :

  ```
  source venv/bin/activate
  ```
* Sous Windows :

  ```
  venv\\Scripts\\activate
  ```

✅ Vérifiez que l’environnement actif pointe vers le bon Python :

```
which python
```

---

### 2️⃣ Installer des packages utiles

✅ Installez les packages suivants avec `pip` :

```
pip install rich requests
```

✅ Vérifiez qu’ils sont bien installés :

```
pip list
```

✅ Utilisez `rich` pour faire un mini-script Python qui affiche un titre coloré :

```
from rich import print
print("[bold magenta]Bienvenue sur AirOps ![/bold magenta]")
```

✅ Testez aussi que `requests` fonctionne en envoyant une requête simple (par exemple, récupérer la page d’accueil de Python) :

```
import requests
response = requests.get("https://www.python.org")
print("Status code:", response.status_code)
```

---

### 3️⃣ Sauvegarder les dépendances

✅ Générez un fichier `requirements.txt` :

```
pip freeze > requirements.txt
```

✅ Ouvrez ce fichier pour vérifier qu’il contient bien `rich` et `requests`.

---

### 4️⃣ Restaurer les dépendances ailleurs

✅ (Optionnel) Créez un nouveau dossier test et un nouveau `venv`.
✅ Utilisez le fichier `requirements.txt` pour réinstaller exactement les mêmes packages :

```
pip install -r requirements.txt
```

---

### 📋 **À rendre (ou vérifier soi-même)**

✅ Dossier `airops_env_test` avec :

* Un fichier `requirements.txt`.
* Un petit script Python utilisant `rich` et `requests`.
* Un environnement activé et fonctionnel.

---

### 🧪 **Questions bonus**

1. Que se passe-t-il si tu désactives l’environnement (`deactivate`) et que tu exécutes le script ?
2. Pourquoi ne faut-il pas versionner le dossier `venv` dans Git ?
3. Quelle commande utiliserais-tu pour désinstaller un package proprement ?

---
