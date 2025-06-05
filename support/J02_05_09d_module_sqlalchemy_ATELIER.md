# 🧩 **Fiche d'exercices – SQLAlchemy ORM**


Base = declarative_base()

class Avion(Base):
    __tablename__ = 'avionsorm'
    id = Column(Integer, primary_key=True)
    modele = Column(String(50), nullable=False)
    description = Column(String(100))
    vitesse_max = Column(Integer)

    vols = relationship("Vol", back_populates="avion")

class Pilote(Base):
    __tablename__ = 'pilotesorm'
    id = Column(Integer, primary_key=True)
    nom = Column(String(50), nullable=False)
    licence = Column(String(50), unique=True)

    vols = relationship("Vol", back_populates="pilote")

class Vol(Base):
    __tablename__ = 'volsorm'
    numero = Column(String(10), primary_key=True)
    destination = Column(String(50))
    statut = Column(String(20))
    heure_creation = Column(DateTime, default=datetime.utcnow)
    heure_decollage = Column(DateTime)
    heure_arrivee = Column(DateTime)



## 🔧 Contexte

On travaille avec trois entités relationnelles :

* `Avion(id, modele, description, vitesse_max)`
* `Pilote(id, nom, licence)`
* `Vol(numero, destination, statut, heure_decollage, heure_arrivee, avion_id, pilote_id)`

---

## 🎯 Objectifs

* Créer des objets et les insérer en base
* Manipuler les relations entre objets
* Faire des requêtes simples et complexes
* Comprendre `join`, `filter`, `group_by`

---

## 📚 EXERCICE 1 – Insertion de données

**Énoncé**
Crée et insère :

1. Deux avions (ex. A320, Boeing 737)
2. Deux pilotes (avec numéro de licence unique)
3. Trois vols différents (avec avion et pilote liés)

```
# À faire
# avion1 = ...
# pilote1 = ...
# vol1 = ...
# session.add(...)
# session.commit()
```
---

## 📚 EXERCICE 2 – Requêtes simples

**Énoncé**

1. Récupère tous les vols
2. Trouve les vols avec statut `"retardé"`
3. Trie les vols par heure de décollage décroissante

```
# vols = ...
```

## 📚 EXERCICE 3 – Jointures et filtres

**Énoncé**

1. Liste les vols effectués avec un `A320`
2. Récupère tous les vols du pilote `"Alice Martin"`
3. Liste des pilotes et leur nombre de vols

---

## 📚 EXERCICE 4 – Mise à jour et suppression

**Énoncé**

1. Mets à jour le statut de tous les vols vers `"terminé"` si `heure_arrivee` est non nulle
2. Supprime les vols `"retardé"` de plus de 24h

---

## 📚 EXERCICE 5 – Préchargement et optimisation

**Énoncé**

1. Récupère tous les vols avec leurs pilotes et avions en 1 requête (évite N+1)

