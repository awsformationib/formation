
## 🔧 Étape 1 : Définir les modèles ORM

### ✅ Objectifs

* Déclarer les classes SQLAlchemy
* Utiliser les bonnes relations (`ForeignKey`, `relationship`)
* Créer la base

### 📦 Modèles

```
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class Avion(Base):
    __tablename__ = 'avions'
    id = Column(Integer, primary_key=True)
    modele = Column(String(50), nullable=False)
    description = Column(String(100))
    vitesse_max = Column(Integer)
    
    vols = relationship("Vol", back_populates="avion")

class Pilote(Base):
    __tablename__ = 'pilotes'
    id = Column(Integer, primary_key=True)
    nom = Column(String(50), nullable=False)
    licence = Column(String(50), unique=True)

    vols = relationship("Vol", back_populates="pilote")

class Vol(Base):
    __tablename__ = 'vols'
    numero = Column(String(10), primary_key=True)
    destination = Column(String(50))
    statut = Column(String(20))
    heure_creation = Column(DateTime, default=datetime.utcnow)
    heure_decollage = Column(DateTime, nullable=True)
    heure_arrivee = Column(DateTime, nullable=True)

    avion_id = Column(Integer, ForeignKey("avions.id"))
    pilote_id = Column(Integer, ForeignKey("pilotes.id"))

    avion = relationship("Avion", back_populates="vols")
    pilote = relationship("Pilote", back_populates="vols")
```

---

## 🧪 Étape 2 : Création base + session

```
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://user:password@localhost/ma_base", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
```

---

## 🔍 Étape 3 : Insertions & Requêtes

### ✅ Ajouter un vol avec avion + pilote

```
a = Avion(modele="A320", description="Moyen-courrier", vitesse_max=850)
p = Pilote(nom="Jean Dupont", licence="FR-456789")
v = Vol(numero="AF101", destination="Madrid", statut="prévu", avion=a, pilote=p)

session.add(v)
session.commit()
```

---

### 🔎 Requêtes utiles

| Objectif             | Exemple SQLAlchemy                                                                           |
| -------------------- | -------------------------------------------------------------------------------------------- |
| Tous les vols        | `session.query(Vol).all()`                                                                   |
| Vols pour un pilote  | `session.query(Vol).filter_by(pilote_id=1).all()`                                            |
| Vols + avion joint   | `session.query(Vol).join(Vol.avion).filter(Avion.modele == "A320").all()`                    |
| Vols triés par heure | `session.query(Vol).order_by(Vol.heure_decollage.desc()).all()`                              |
| GroupBy avion        | `session.query(Avion.modele, func.count(Vol.numero)).join(Vol).group_by(Avion.modele).all()` |

---

## 🧱 Étape 4 : Bonnes pratiques et bonus

### ✅ Séparer modules

* `models.py` → les classes ORM
* `db.py` → moteur et session
* `main.py` → tests, requêtes

### ✅ Requêtes avancées

* `joinedload()` pour précharger
* `aliased()` pour requêtes complexes
* `selectinload()` pour éviter le N+1

---

## 💡 Pour aller plus loin

* ⚙️ Relations `many-to-many` (ex. Vols <-> Passagers)
* 🔄 `update()` et `delete()` conditionnels
* 🔐 Contrainte d’unicité, index, `nullable`, etc.
* 🧪 Tests unitaires SQLAlchemy (ex: avec `sqlite:///:memory:`)

---
