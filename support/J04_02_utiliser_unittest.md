![Logo](images\logo.png)

## 🧩 Fiche – Comment utiliser `unittest` en Python

---

### 🎯 **Objectif**

Découvrir le module `unittest` :
✅ Comprendre sa structure,
✅ Apprendre à écrire des tests,
✅ Savoir utiliser `setUp`, `tearDown`,
✅ Comprendre la configuration des suites de tests.

---

### 🔍 **Pourquoi `unittest` ?**

* C’est le module de test **standard** inclus avec Python.
* Inspiré de JUnit (Java), il est robuste, structuré et compatible avec d’autres outils (ex. CI/CD).
* Il permet d’écrire des tests clairs, réutilisables, et de les exécuter automatiquement.

---

### 🛠 **Exemple : une petite classe à tester**

On imagine une classe **Calculatrice** :

```
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

### 🏗 **Structure d’un test `unittest`**

```
import unittest

class TestCalculatrice(unittest.TestCase):

    def setUp(self):
        """Initialisation avant chaque test."""
        self.calc = Calculatrice()

    def tearDown(self):
        """Nettoyage après chaque test (optionnel ici)."""
        pass

    def test_addition(self):
        self.assertEqual(self.calc.addition(2, 3), 5)

    def test_soustraction(self):
        self.assertEqual(self.calc.soustraction(10, 4), 6)

    def test_division_normale(self):
        self.assertEqual(self.calc.division(10, 2), 5)

    def test_division_par_zero(self):
        with self.assertRaises(ValueError):
            self.calc.division(10, 0)
```

---

### 🔑 **Points clés à retenir**

| Élément                                                        | Rôle                                                                        |
| -------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `unittest.TestCase`                                            | Classe de base pour définir vos tests.                                      |
| `setUp()`                                                      | Appelée **avant chaque test** : sert à initialiser l’environnement.         |
| `tearDown()`                                                   | Appelée **après chaque test** : pour nettoyer si nécessaire.                |
| Méthodes `test_*`                                              | Chaque méthode dont le nom commence par `test_` est exécutée comme un test. |
| Assertions (`assertEqual`, `assertTrue`, `assertRaises`, etc.) | Vérifient si les résultats sont corrects.                                   |

---

### ⚙️ **Lancer les tests**

Depuis le terminal :

```
python -m unittest test_calculatrice.py
```

Depuis un IDE (VSCode, PyCharm) : clic droit → **Run tests**.

---

### 🧩 **Les assertions les plus courantes**

| Assertion              | Vérifie que…                  |
| ---------------------- | ----------------------------- |
| `assertEqual(a, b)`    | `a == b`                      |
| `assertNotEqual(a, b)` | `a != b`                      |
| `assertTrue(x)`        | `bool(x) is True`             |
| `assertFalse(x)`       | `bool(x) is False`            |
| `assertIn(a, b)`       | `a` est dans `b`              |
| `assertIsNone(x)`      | `x is None`                   |
| `assertRaises(exc)`    | Une exception `exc` est levée |

---

### 🏗 **Organisation des fichiers de tests**

* Placez vos tests dans un répertoire `tests/`.
* Nommez vos fichiers `test_*.py`.
* Structure classique :

```
/projet
    calculatrice.py
    /tests
        test_calculatrice.py
```

---

### ⚙️ **Configurer une suite de tests**

Si vous avez plusieurs fichiers :

```
python -m unittest discover -s tests
```

Cela va découvrir et exécuter **tous les fichiers** `test_*.py` dans le dossier `tests`.

---

### 🌟 **Conseils avancés**

✅ Ajoutez des cas limites (ex. nombres négatifs, gros nombres).
✅ Utilisez `setUpClass` et `tearDownClass` pour des initialisations globales.
✅ Intégrez vos tests dans un pipeline (GitHub Actions, GitLab CI).
✅ Couplé avec `coverage`, mesurez combien de votre code est testé.

---

### 🧪 **Questions pour discussion**

1. Pourquoi séparer les tests du code principal ?
2. Quand doit-on utiliser `setUp` vs. `setUpClass` ?
3. Pourquoi tester les erreurs (`assertRaises`) est-il aussi important que tester les résultats corrects ?
4. Peut-on écrire des tests pour des appels réseau, des bases de données ? Comment ?

---
