
## 🧪 Comparatif visuel : `pytest` vs `robotframework` vs `behave`

| Critère / Outil             | 🐍 `pytest`                            | 🤖 `Robot Framework`                   | 🍀 `behave` (BDD)                       |
| --------------------------- | -------------------------------------- | -------------------------------------- | --------------------------------------- |
| **Langage**                 | Python pur                             | DSL en texte / tabulaire               | DSL Gherkin (Given / When / Then)       |
| **Public cible**            | Développeurs Python                    | QA non dev / testeurs métier           | PO, QA, développeurs en mode agile      |
| **Style de test**           | Fonctionnel, unitaire, très libre      | Keywords, tables, très structuré       | Scénarios lisibles (BDD)                |
| **Apprentissage**           | Simple pour développeurs Python        | Très simple pour non-dev               | Simple si on connaît le BDD             |
| **Extensibilité**           | Très grande (plugins, hooks)           | Forte via bibliothèques (Python, Java) | Moyenne (via steps personnalisés)       |
| **Tests API**               | ✅ avec `requests`, `httpx`             | ✅ avec `RequestsLibrary`               | ✅ via `requests` ou `rest_behave`       |
| **Tests UI (desktop/web)**  | ✅ via `pytest-qt`, `selenium`, etc.    | ✅ avec `SeleniumLibrary`, `PyWinAuto`  | ✅ mais souvent lié au web               |
| **BDD (Behaviour Driven)**  | ❌ sauf avec plugin `pytest-bdd`        | Possible mais non natif                | ✅ natif (Gherkin)                       |
| **Logs & rapports**         | Basique + plugins (`html`, `junitxml`) | ✅ Très riche : HTML, screenshots, etc. | ✅ via `allure`, `behave-html-formatter` |
| **Intégration CI/CD**       | ✅ très facile avec GitHub/GitLab CI    | ✅ possible mais dépend des runners     | ✅ facile (BDD très utilisé en DevOps)   |
| **Conventions de fichiers** | test\_\*.py ou \*\_test.py             | \*.robot                               | \*.feature                              |
| **Execution globale**       | `pytest`                               | `robot tests/`                         | `behave features/`                      |

---

### 🔍 Exemple d’un même test : "vérifier que `2 + 2 = 4`"

#### 🐍 Pytest

```python
def test_somme():
    assert 2 + 2 == 4
```

#### 🤖 Robot Framework

```robot
*** Test Cases ***
Vérifier la somme
    ${result}=    Evaluate    2 + 2
    Should Be Equal    ${result}    4
```

#### 🍀 Behave

```gherkin
Feature: Addition
  Scenario: Vérifier la somme
    Given je prends 2 et 2
    When je les additionne
    Then le résultat est 4
```

```python
# steps/addition_steps.py
from behave import given, when, then

@given("je prends {a:d} et {b:d}")
def step_impl(context, a, b):
    context.result = a + b

@then("le résultat est {expected:d}")
def step_impl(context, expected):
    assert context.result == expected
```

---

## 🧭 Quand utiliser lequel ?

| Cas d’usage                                   | Outil recommandé   |
| --------------------------------------------- | ------------------ |
| Tu es **développeur Python**                  | ✅ `pytest`         |
| Tu veux **tester une API REST sans coder**    | ✅ `robotframework` |
| Tu fais des **tests fonctionnels métiers**    | ✅ `behave`         |
| Tu veux faire du **test exploratoire rapide** | ✅ `pytest`         |
| Tu veux un **tableau de tests lisible**       | ✅ `robotframework` |
| Tu travailles en **équipe agile BDD**         | ✅ `behave`         |

