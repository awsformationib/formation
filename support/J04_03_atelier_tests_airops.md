![Logo](images\logo.png)


## 🧩 Fiche – Comment utiliser `pytest` en Python

---

### 🎯 **Objectif**

Découvrir `pytest`, un framework de test Python moderne, plus souple et plus agréable à utiliser que `unittest` :
✅ Écrire des tests plus simples et lisibles,
✅ Gérer les fixtures (`setup`, `teardown`) de façon flexible,
✅ Exploiter ses puissantes options (paramétrisation, rapports, plugins).

---

### 🏗 **Rappel : la classe à tester**

```python
class Calculatrice:
    def addition(self, a, b):
        return a + b

    def soustraction(self, a, b):
        return a - b

    def division(self, a, b):
        if b == 0:
            raise ValueError("Division par zéro")
        return a / b
```

---

### 🛠 **Structure d’un test avec `pytest`**

```python
import pytest
from calculatrice import Calculatrice

@pytest.fixture
def calc():
    return Calculatrice()

def test_addition(calc):
    assert calc.addition(2, 3) == 5

def test_soustraction(calc):
    assert calc.soustraction(10, 4) == 6

def test_division_normale(calc):
    assert calc.division(10, 2) == 5

def test_division_par_zero(calc):
    with pytest.raises(ValueError):
        calc.division(10, 0)
```

---

### 🔑 **Points clés à retenir**

| Élément                | Rôle                                                                                |
| ---------------------- | ----------------------------------------------------------------------------------- |
| `@pytest.fixture`      | Fournit un objet prêt pour les tests (`setup` flexible).                            |
| Tests simples          | Pas besoin d’hériter d’une classe spéciale (contrairement à `unittest`).            |
| `assert` natif         | On utilise l’instruction Python standard (et pytest fournit des messages enrichis). |
| Gestion des exceptions | Avec `pytest.raises()`.                                                             |

---

### ⚙️ **Lancer les tests**

Depuis le terminal, dans le dossier projet :

```bash
pytest
```

Pour voir plus de détails (verbose) :

```bash
pytest -v
```

Pour générer un rapport HTML (avec plugin) :

```bash
pytest --html=rapport.html
```

---

### 🧩 **Organisation recommandée**

* Placez vos tests dans un dossier `tests/`.
* Nommez les fichiers `test_*.py`.
* Structure :

```
/projet
    calculatrice.py
    /tests
        test_calculatrice.py
```

---

### 🌟 **Avantages de `pytest`**

✅ Moins de code et plus de lisibilité.
✅ Fixtures réutilisables et puissantes.
✅ Paramétrisation facile des tests.
✅ Large écosystème de plugins.
✅ Compatible avec les tests `unittest` existants.

---

### 🔧 **Exemple : paramétriser les tests**

```python
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_addition_parametre(calc, a, b, expected):
    assert calc.addition(a, b) == expected
```

---

### 🏆 **Comparaison avec d’autres bibliothèques**

| Librairie      | Caractéristiques                                                                                                                  |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **unittest**   | Module standard, robuste, structuré, mais verbeux.                                                                                |
| **pytest**     | Moderne, minimaliste, riche en plugins, très utilisé en 2024.                                                                     |
| **nose2**      | Héritier de `nose` (abandonné), simple mais moins actif.                                                                          |
| **doctest**    | Permet d’insérer les tests directement dans les docstrings (très simple, mais limité).                                            |
| **hypothesis** | Génère automatiquement des cas de test aléatoires pour pousser le code dans ses retranchements (testing basé sur les propriétés). |

---

### 🧪 **Questions de discussion**

1. Pourquoi `pytest` est-il préféré dans beaucoup de projets modernes ?
2. Qu’apporte la paramétrisation par rapport à écrire plusieurs tests manuels ?
3. Dans quels cas `doctest` est-il utile malgré ses limites ?
4. Qu’est-ce que le property-based testing (via `hypothesis`) apporte de plus ?
5. Est-ce une bonne idée d’avoir plusieurs frameworks de test mélangés dans un même projet ?

---
