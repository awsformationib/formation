![Logo](images\logo.png)

### ⚙️ Prérequis

Installe d’abord SQLAlchemy et le connecteur MySQL :

```bash
pip install sqlalchemy pymysql
```

---

### 🧱 Étape 1 : Définir la classe `Avion` comme un modèle ORM

```python
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Avion(Base):
    __tablename__ = 'avions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    immatriculation = Column(String(20), unique=True, nullable=False)
    modele = Column(String(50), nullable=False)
    en_vol = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Avion(immatriculation='{self.immatriculation}', modele='{self.modele}', en_vol={self.en_vol})>"
```

---

### 🧩 Étape 2 : Créer une session SQLAlchemy et se connecter à MySQL

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Exemple de chaîne de connexion MySQL
# Remplace USER, PASSWORD, HOST, DB par les bons paramètres
engine = create_engine("mysql+pymysql://USER:PASSWORD@HOST/DB", echo=True)

# Crée les tables si elles n'existent pas
Base.metadata.create_all(engine)

# Création de la session
Session = sessionmaker(bind=engine)
session = Session()
```

---

### ✍️ Étape 3 : Utiliser le modèle pour insérer un avion

```python
# Création d'un objet Avion
nouvel_avion = Avion(immatriculation="F-HBXC", modele="Airbus A320", en_vol=True)

# Insertion en base
session.add(nouvel_avion)
session.commit()

print("Avion inséré :", nouvel_avion)
```

---

### 🔍 Étape 4 : Requête simple

```python
# Rechercher tous les avions en vol
avions_en_vol = session.query(Avion).filter_by(en_vol=True).all()
for avion in avions_en_vol:
    print(avion)
```

---

### ✅ Résumé

| Étape | Action                                            |
| ----- | ------------------------------------------------- |
| 1     | Définir le modèle avec `Base`                     |
| 2     | Créer un moteur (`engine`) avec `create_engine()` |
| 3     | Créer une session avec `sessionmaker()`           |
| 4     | Utiliser `.add()` et `.commit()` pour insérer     |
| 5     | Utiliser `.query()` pour lire les données         |

---

### 🧠 Bonnes pratiques

* Tu peux gérer les erreurs avec `try` / `except` pour capturer les problèmes de connexion ou d'intégrité.
* Active `echo=False` en production.
* Pour des projets plus grands, pense à structurer ton code avec des DAO (Data Access Objects) ou un repository pattern.
