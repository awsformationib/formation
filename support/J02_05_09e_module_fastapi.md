![Logo](images\logo.png)

---

## 🧩 Objectif : API REST `Avion` avec FastAPI + SQLAlchemy + MySQL

---

### ✅ Structure du projet recommandée

```
.
├── main.py                 ← Application FastAPI
├── models.py              ← Modèles ORM SQLAlchemy
├── database.py            ← Connexion à la base
├── schemas.py             ← Schémas Pydantic (validation)
└── requirements.txt
```

---

## 1. 📦 `requirements.txt`

```text
fastapi
uvicorn
sqlalchemy
pymysql
```

---

## 2. ⚙️ `database.py`

```
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://USER:PASSWORD@HOST/DB"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
```

---

## 3. 🛩️ `models.py`

```
from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Avion(Base):
    __tablename__ = "avions"

    id = Column(Integer, primary_key=True, index=True)
    immatriculation = Column(String(20), unique=True, nullable=False)
    modele = Column(String(50), nullable=False)
    en_vol = Column(Boolean, default=False)
```

---

## 4. 🧰 `schemas.py`

```
from pydantic import BaseModel

class AvionBase(BaseModel):
    immatriculation: str
    modele: str
    en_vol: bool = False

class AvionCreate(AvionBase):
    pass

class AvionRead(AvionBase):
    id: int

    class Config:
        orm_mode = True
```

---

## 5. 🚀 `main.py`

```
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, database

# Crée les tables si elles n'existent pas
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Dépendance pour récupérer une session DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/avions/", response_model=schemas.AvionRead)
def create_avion(avion: schemas.AvionCreate, db: Session = Depends(get_db)):
    db_avion = models.Avion(**avion.dict())
    db.add(db_avion)
    db.commit()
    db.refresh(db_avion)
    return db_avion

@app.get("/avions/", response_model=List[schemas.AvionRead])
def read_avions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Avion).offset(skip).limit(limit).all()

@app.get("/avions/{avion_id}", response_model=schemas.AvionRead)
def read_avion(avion_id: int, db: Session = Depends(get_db)):
    avion = db.query(models.Avion).get(avion_id)
    if not avion:
        raise HTTPException(status_code=404, detail="Avion non trouvé")
    return avion

@app.delete("/avions/{avion_id}", response_model=dict)
def delete_avion(avion_id: int, db: Session = Depends(get_db)):
    avion = db.query(models.Avion).get(avion_id)
    if not avion:
        raise HTTPException(status_code=404, detail="Avion non trouvé")
    db.delete(avion)
    db.commit()
    return {"message": "Avion supprimé"}
```

---

## ▶️ Lancer le serveur

```
uvicorn main:app --reload
```

---

## 📫 Exemples d'utilisation

* `POST /avions/` avec JSON :

```json
{
  "immatriculation": "F-GKXA",
  "modele": "Airbus A320",
  "en_vol": true
}
```

* `GET /avions/` → Liste des avions
* `GET /avions/1` → Détail avion id=1
* `DELETE /avions/1` → Supprimer avion

---

## 🧠 Bonus (facultatif)

Tu peux enrichir cette base avec :

* `PUT /avions/{id}` pour modifier un avion
* des filtres : `?en_vol=true`
* Swagger intégré sur `http://127.0.0.1:8000/docs`
