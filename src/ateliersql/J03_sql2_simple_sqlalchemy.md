
# ✅ Fiche Solution – Atelier CRUD `Vol` avec **SQLAlchemy ORM**

## 📦 1. Modèle `Vol` avec SQLAlchemy

```
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Vol(Base):
    __tablename__ = 'vols'

    numero = Column(String(10), primary_key=True)
    destination = Column(String(50))
    avion = Column(String(50))
    statut = Column(String(20))
    heure_creation = Column(DateTime)
    heure_decollage = Column(DateTime)
    heure_arrivee = Column(DateTime)
```

---

## ⚙️ 2. Connexion & Session

```
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Adapter avec vos identifiants
DATABASE_URL = "mysql+mysqlconnector://root:votre_mot_de_passe@localhost/formation"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)
```

---

## 🧱 3. Ajouter un vol

```
def ajouter_vol(vol: Vol):
    session = SessionLocal()
    try:
        session.add(vol)
        session.commit()
    finally:
        session.close()
```

---

## 📖 4. Lister tous les vols

```
def lister_vols():
    session = SessionLocal()
    try:
        return session.query(Vol).all()
    finally:
        session.close()
```

---

## 🔍 5. Chercher un vol par numéro

```
def chercher_vol_par_numero(numero: str):
    session = SessionLocal()
    try:
        return session.query(Vol).filter_by(numero=numero).first()
    finally:
        session.close()
```

---

## 🛠️ 6. Mettre à jour le statut d’un vol

```
def mettre_a_jour_statut(numero: str, nouveau_statut: str):
    session = SessionLocal()
    try:
        vol = session.query(Vol).filter_by(numero=numero).first()
        if vol:
            vol.statut = nouveau_statut
            session.commit()
    finally:
        session.close()
```

---

## 🗑️ 7. Supprimer un vol

```
def supprimer_vol(numero: str):
    session = SessionLocal()
    try:
        vol = session.query(Vol).filter_by(numero=numero).first()
        if vol:
            session.delete(vol)
            session.commit()
    finally:
        session.close()
```

---

## 🔎 Bonus : Recherche par destination (LIKE)

```
def chercher_par_destination(partiel: str):
    session = SessionLocal()
    try:
        return session.query(Vol).filter(Vol.destination.like(f"%{partiel}%")).all()
    finally:
        session.close()
```

---

## 🧪 8. Création des tables

À lancer une fois pour créer la table en base (si elle n’existe pas encore) :

```
Base.metadata.create_all(bind=engine)
```
