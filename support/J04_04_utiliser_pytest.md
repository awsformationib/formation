![Logo](images\logo.png)


## 🧩 Atelier guidé – Ajouter des tests `pytest` au projet AirOps

---

### 🎯 **Objectif**

Apprendre à écrire des tests `pytest` pour le projet AirOps :
✅ Tester les classes principales (`Avion`, `Vol`, `Pilote`),
✅ Cibler les comportements clés,
✅ Couvrir à la fois les succès et les erreurs attendues,
✅ Structurer le projet avec des fichiers de tests dédiés.

---

### 🏗 **Préparation**

1️⃣ Assurez-vous que le projet AirOps est installé et fonctionnel.
2️⃣ Créez un dossier :

```
/tests
```

3️⃣ Installez `pytest` :

```
pip install pytest
```

4️⃣ Vérifiez que vous pouvez lancer un test simple :

```
pytest
```

---

### 🛠 **Bribes de départ : tests sur Avion**

Dans `tests/test_avion.py` :

```
import pytest
from avion import Avion

@pytest.fixture
def avion():
    return Avion("F-ABCD", "A320")
```

---

### ✈️ **Scénarios à couvrir**

| Scénario                                                                  | Indice de code                                             |
| ------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Créer un avion et vérifier son immatriculation.                           | `assert avion.immatriculation == "F-ABCD"`                 |
| Ajouter des vols à l’avion et vérifier qu’ils sont bien enregistrés.      | `avion.vols.append(...)` + `assert len(avion.vols) == ...` |
| Vérifier que deux avions avec même immatriculation sont égaux (`__eq__`). | `assert avion1 == avion2`                                  |

**Question rebond :**
👉 Avez-vous déjà implémenté `__eq__` dans la classe Avion ? Sinon, proposez une version simple avant de tester !

---

### 🛠 **Bribes : tests sur Vol**

Dans `tests/test_vol.py` :

```
import pytest
from vol import Vol, Avion, Piste

@pytest.fixture
def vol():
    avion = Avion("F-ABCD", "A320")
    piste = Piste("27L")
    return Vol("AF123", avion, piste)
```

---

### ✈️ **Scénarios à couvrir**

| Scénario                                                                                 | Indice de code               |
| ---------------------------------------------------------------------------------------- | ---------------------------- |
| Vérifier que le vol connaît son avion et sa piste.                                       | `assert vol.avion == avion`  |
| Vérifier qu’ajouter un pilote l’ajoute bien aux deux côtés (vol.pilotes et pilote.vols). | `vol.ajouter_pilote(...)`    |
| Vérifier la méthode `__str__` affiche les infos attendues.                               | `assert "AF123" in str(vol)` |

**Question rebond :**
👉 Comment s’assurer qu’ajouter le même pilote deux fois ne crée pas un doublon ?
👉 Proposez un test qui échoue si le comportement actuel est incorrect.

---

### 🛠 **Bribes : tests sur Pilote**

Dans `tests/test_pilote.py` :

```
import pytest
from pilote import Pilote

@pytest.fixture
def pilote():
    return Pilote("Alice")
```

---

### ✈️ **Scénarios à couvrir**

| Scénario                                                       | Indice de code                 |
| -------------------------------------------------------------- | ------------------------------ |
| Vérifier que le pilote connaît bien son nom.                   | `assert pilote.nom == "Alice"` |
| Vérifier que la liste des vols est vide au départ.             | `assert pilote.vols == []`     |
| Vérifier qu’après ajout à un vol, le lien est bien réciproque. | `vol.ajouter_pilote(pilote)`   |

**Question rebond :**
👉 Peut-on écrire un test pour vérifier que deux pilotes différents ont bien des listes de vols indépendantes ?

---

### 📦 **Organisation recommandée**

* Un fichier `test_avion.py`
* Un fichier `test_vol.py`
* Un fichier `test_pilote.py`

Tous regroupés dans le dossier `tests`.

---

### 🚀 **Bonus : couverture et robustesse**

Proposez un test :
✅ Pour une division par zéro, une affectation invalide, ou un état inattendu.
✅ Pour vérifier que les objets sont triables (avec `sorted()`) si vous avez implémenté `__lt__`.

**Question rebond :**
👉 Comment pourriez-vous simuler un scénario d’erreur métier complexe et vérifier qu’une exception est bien levée ?

---

### 🧪 **Discussion finale**

1. Quels cas de test avez-vous trouvés les plus “cachés” ?
2. Quels sont les comportements les plus critiques à couvrir par les tests ?
3. Comment organiser les tests pour qu’ils restent lisibles quand le projet grossit ?
4. Que gagnez-vous à ajouter des tests avant d’ajouter de nouvelles fonctionnalités ?

---
