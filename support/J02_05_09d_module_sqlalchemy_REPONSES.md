![Logo](images\logo.png)

https://docs.sqlalchemy.org/en/20/tutorial/index.html

# 🧩 **Fiche d'exercices – SQLAlchemy ORM**

## 🔧 Contexte

Tu travailles avec trois entités relationnelles :

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

✅ **Correction :**

```
a1 = Avion(modele="A320", description="Airbus moyen-courrier", vitesse_max=830)
a2 = Avion(modele="B737", description="Boeing court-courrier", vitesse_max=820)

p1 = Pilote(nom="Alice Martin", licence="LIC001")
p2 = Pilote(nom="David Morel", licence="LIC002")

v1 = Vol(numero="V100", destination="Paris", statut="prévu", avion=a1, pilote=p1)
v2 = Vol(numero="V101", destination="Berlin", statut="en vol", avion=a2, pilote=p1)
v3 = Vol(numero="V102", destination="Rome", statut="retardé", avion=a1, pilote=p2)

session.add_all([a1, a2, p1, p2, v1, v2, v3])
session.commit()
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

✅ **Correction :**

```
from sqlalchemy import desc

vols = session.query(Vol).all()
retardes = session.query(Vol).filter_by(statut="retardé").all()
trie_desc = session.query(Vol).order_by(desc(Vol.heure_decollage)).all()
```

---

## 📚 EXERCICE 3 – Jointures et filtres

**Énoncé**

1. Liste les vols effectués avec un `A320`
2. Récupère tous les vols du pilote `"Alice Martin"`
3. Liste des pilotes et leur nombre de vols

✅ **Correction :**

```
# 1
vols_a320 = session.query(Vol).join(Vol.avion).filter(Avion.modele == "A320").all()

# 2
vols_alice = session.query(Vol).join(Vol.pilote).filter(Pilote.nom == "Alice Martin").all()

# 3
from sqlalchemy import func

nb_vols_par_pilote = session.query(
    Pilote.nom,
    func.count(Vol.numero)
).join(Vol).group_by(Pilote.nom).all()
```

---

## 📚 EXERCICE 4 – Mise à jour et suppression

**Énoncé**

1. Mets à jour le statut de tous les vols vers `"terminé"` si `heure_arrivee` est non nulle
2. Supprime les vols `"retardé"` de plus de 24h

✅ **Correction :**

``` 
# 1
session.query(Vol).filter(Vol.heure_arrivee != None).update(
    {Vol.statut: "terminé"}, synchronize_session="fetch"
)
session.commit()

# 2
from datetime import datetime, timedelta

limite = datetime.utcnow() - timedelta(hours=24)
session.query(Vol).filter(
    Vol.statut == "retardé",
    Vol.heure_decollage < limite
).delete(synchronize_session="fetch")
session.commit()
```

---

## 📚 EXERCICE 5 – Préchargement et optimisation

**Énoncé**

1. Récupère tous les vols avec leurs pilotes et avions en 1 requête (évite N+1)

✅ **Correction :**

```
from sqlalchemy.orm import joinedload

vols_complets = session.query(Vol).options(
    joinedload(Vol.pilote),
    joinedload(Vol.avion)
).all()
```
