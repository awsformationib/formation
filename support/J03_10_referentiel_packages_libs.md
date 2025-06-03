![Logo](images\logo.png)


## 📦 Liste regroupée des librairies externes Python – par catégorie technique

---

### 🗄 **Bases de données et fichiers**

| Nom                       | Description                                                                       |
| ------------------------- | --------------------------------------------------------------------------------- |
| **sqlite3** (standard)    | Intègre une base SQLite directement dans Python.                                  |
| **sqlalchemy**            | ORM puissant pour interagir avec des bases SQL (PostgreSQL, MySQL, SQLite, etc.). |
| **pymongo**               | Connecte et manipule des bases NoSQL MongoDB.                                     |
| **openpyxl**              | Lit et écrit des fichiers Excel (.xlsx).                                          |
| **csv** (standard)        | Manipule les fichiers CSV facilement.                                             |
| **pyarrow / fastparquet** | Manipule des fichiers Parquet ultra-rapides (données massives).                   |

---

### 📊 **Données et analyses**

| Nom              | Description                                                                                     |
| ---------------- | ----------------------------------------------------------------------------------------------- |
| **pandas**       | Analyse, nettoie et transforme des datasets tabulaires (CSV, Excel, SQL).                       |
| **numpy**        | Effectue des calculs mathématiques et scientifiques rapides sur des tableaux.                   |
| **scipy**        | Fournit des algorithmes avancés en statistiques, optimisation, signal, etc.                     |
| **scikit-learn** | Implémente des modèles de machine learning classiques (classification, clustering, régression). |
| **statsmodels**  | Propose des analyses statistiques poussées et des modèles économétriques.                       |

---

### 📈 **Visualisation et reporting**

| Nom            | Description                                                                           |
| -------------- | ------------------------------------------------------------------------------------- |
| **matplotlib** | Crée des graphiques simples ou avancés en 2D.                                         |
| **seaborn**    | Génère des visualisations statistiques élégantes, basées sur matplotlib.              |
| **plotly**     | Construit des graphiques interactifs pour dashboards et web.                          |
| **rich**       | Affiche des tableaux, des logs et des barres de progression colorés dans le terminal. |
| **tabulate**   | Formatte des tableaux ASCII ou Markdown pour la console ou les rapports texte.        |

---

### 🌐 **Web, APIs et services**

| Nom                       | Description                                                                            |
| ------------------------- | -------------------------------------------------------------------------------------- |
| **requests**              | Effectue des requêtes HTTP simples (GET, POST, etc.).                                  |
| **httpx**                 | Version plus moderne et asynchrone pour les appels HTTP.                               |
| **flask**                 | Crée des petites applications web et APIs REST.                                        |
| **fastapi**               | Développe des APIs modernes, performantes et documentées automatiquement.              |
| **uvicorn**               | Serveur ASGI rapide pour exécuter FastAPI.                                             |
| **beautifulsoup4**        | Scrape et analyse des pages HTML.                                                      |
| **selenium / playwright** | Automatise l’interaction avec des navigateurs pour les tests ou le scraping dynamique. |

---

### ⚙ **Infrastructure, CLI et qualité**

| Nom          | Description                                                |
| ------------ | ---------------------------------------------------------- |
| **loguru**   | Met en place un système de logs avancé et lisible.         |
| **typer**    | Crée rapidement des interfaces en ligne de commande (CLI). |
| **click**    | Alternative CLI populaire (moins moderne que Typer).       |
| **pytest**   | Framework de test automatisé simple et puissant.           |
| **black**    | Formatte le code Python selon un style uniforme.           |
| **mypy**     | Vérifie les annotations de type pour prévenir des erreurs. |
| **pydantic** | Valide et convertit des données selon des modèles stricts. |

---

### 🎭 **Génération de données et tests**

| Nom              | Description                                                                       |
| ---------------- | --------------------------------------------------------------------------------- |
| **faker**        | Crée des jeux de données fictifs réalistes (noms, adresses, numéros, etc.).       |
| **factory\_boy** | Génère des objets de test liés à vos modèles Python (souvent combiné avec Faker). |

---

### ✈️ **Exemples AirOps – Packages particulièrement pertinents**

| Besoin AirOps                                            | Librairie                       |
| -------------------------------------------------------- | ------------------------------- |
| Simuler des jeux de données vol/avion/pilote             | `faker`, `factory_boy`          |
| Analyser les statistiques des vols                       | `pandas`, `numpy`, `matplotlib` |
| Connecter une API météo ou trafic                        | `requests`, `httpx`             |
| Créer une API REST pour exposer AirOps                   | `fastapi`, `uvicorn`            |
| Générer des rapports visuels et interactifs              | `plotly`, `rich`                |
| Tester les règles métiers (par ex. contraintes horaires) | `pytest`, `pydantic`            |

---

### 📘 **Conseils pratiques**

✅ Vérifier que la librairie est bien maintenue (dernière mise à jour, activité sur GitHub).
✅ Explorer la documentation officielle avant de l’adopter.
✅ Tester toujours une intégration sur un projet minimal avant de l’embarquer à grande échelle.

---
