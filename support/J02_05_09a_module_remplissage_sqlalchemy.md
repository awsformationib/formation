![Logo](images\logo.png)


### ✅ **Étapes :**

1. Définir la classe `Avion` Python.
2. Créer le mapping SQLAlchemy vers la table `avion`.
3. Générer `N` objets `Avion` avec des données aléatoires.
4. Insérer ces objets dans la base MySQL.

---

### 📦 Prérequis

```
pip install sqlalchemy pymysql faker
```

---

### 📁 Structure de la table `avion`

Tu indiques qu’elle contient :

* `code` (immatriculation)
* `modele`
* `description`
* `vitessemax`

---

### 🧠 Code Complet

```
from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.orm import declarative_base, sessionmaker
from faker import Faker
import random

# Configuration base
DATABASE_URL = "mysql+pymysql://user:password@localhost:3306/ma_base"
Base = declarative_base()
faker = Faker()

# Classe ORM (table avion)
class AvionORM(Base):
    __tablename__ = "avion"
    code = Column(String(20), primary_key=True)          # immatriculation
    modele = Column(String(50))
    description = Column(Text)
    vitessemax = Column(Integer)

# Classe métier
class Avion:
    def __init__(self, immatriculation, modele=None, vitesse=0):
        self.immatriculation = immatriculation
        self.modele = modele or "Modele-X"
        self.vitesse = vitesse

# Fonction pour convertir un objet Avion en AvionORM
def avion_to_orm(avion: Avion):
    return AvionORM(
        code=avion.immatriculation,
        modele=avion.modele,
        description=faker.text(max_nb_chars=100),
        vitessemax=avion.vitesse
    )

# Générer N avions aléatoires
def generate_random_avions(n):
    avions = []
    for _ in range(n):
        immat = f"F-{faker.bothify(text='??###')}"
        modele = random.choice(["Airbus A320", "Boeing 737", "Cessna 172", "Concorde"])
        vitesse = random.randint(300, 2400)
        avions.append(Avion(immat, modele, vitesse))
    return avions

# Insérer dans la base
def insert_avions(n):
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    avions = generate_random_avions(n)
    orm_avions = [avion_to_orm(av) for av in avions]

    session.add_all(orm_avions)
    session.commit()
    print(f"{n} avions insérés avec succès.")
    session.close()

# Exemple d'exécution
if __name__ == "__main__":
    insert_avions(10)  # Par exemple, insérer 10 avions
```

---

### 🧪 Résultat dans MySQL

Tu auras une table `avion` avec des lignes du style :

| code    | modele      | description        | vitessemax |
| ------- | ----------- | ------------------ | ---------- |
| F-XZ123 | Airbus A320 | Texte aléatoire... | 892        |
| F-RJ678 | Cessna 172  | Phrase de test...  | 412        |

---

### ✏️ À adapter

* Change `DATABASE_URL` avec ton login/MDP/MySQL.
* Si tu veux une vraie description du modèle, tu peux créer une table `modele` avec une clé étrangère.
* Tu peux aussi utiliser `Alembic` si tu veux une migration propre.
