
# 🧪 Fiche – Outils de test alternatifs à `pytest` et `unittest` en Python

---

## ✅ 1. **Tests fonctionnels / unitaires (alternatives à pytest)**

| Outil                                                         | Atouts spécifiques                                       | Quand l’utiliser ?                                     |
| ------------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------ |
| **[nose2](https://nose2.readthedocs.io)**                     | Successeur de `nose`, simple à utiliser                  | Si tu veux rester proche de `unittest` avec plugins    |
| **[doctest](https://docs.python.org/3/library/doctest.html)** | Teste le code dans les docstrings                        | Pour la documentation vivante et tests légers intégrés |
| **[testslide](https://testslide.readthedocs.io/)**            | Tests unitaires + stubs/mocks puissants                  | Si tu veux des mocks très précis dans un grand projet  |
| **[hypothesis](https://hypothesis.readthedocs.io/)**          | Tests *property-based*, données aléatoires intelligentes | Si tu veux couvrir plus de cas que des cas fixés       |
| **[tox](https://tox.readthedocs.io/)**                        | Teste ton code dans plusieurs environnements Python      | Pour assurer la compatibilité entre versions           |

---

## 🔗 2. **Tests d’intégration (API, DB, etc.)**

| Outil                                                   | Fonction                                            | Cas d’usage conseillé                                 |
| ------------------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------- |
| **[Robot Framework](https://robotframework.org/)**      | DSL de test générique avec grande lisibilité        | Tests end-to-end (API, UI, fichiers), profils métier  |
| **[behave](https://behave.readthedocs.io/)**            | Tests BDD (Given-When-Then)                         | Spécification fonctionnelle avec PO/QA                |
| **[locust](https://locust.io)**                         | Tests de charge HTTP                                | Pour simuler des utilisateurs / appels massifs d’API  |
| **[requests + tavern](https://tavern.readthedocs.io/)** | Tests d’API REST en YAML                            | Test automatique d’API avec des scénarios lisibles    |
| **[schemathesis](https://schemathesis.readthedocs.io)** | Tests auto d’API REST à partir d’un OpenAPI/Swagger | Pour stress tester ton API sans écrire de test manuel |

---

## 🎛️ 3. **Tests UI (Desktop, Web)**

| Outil                                              | Type de GUI           | Quand l’utiliser ?                                     |
| -------------------------------------------------- | --------------------- | ------------------------------------------------------ |
| **[pytest-qt](https://pytest-qt.readthedocs.io/)** | PyQt / PySide6        | Tester une GUI Qt/PySide avec interactions utilisateur |
| **[pywinauto](https://pywinauto.github.io/)**      | Windows Desktop       | Automatiser clics, menus dans appli Windows            |
| **[Selenium](https://www.selenium.dev/)**          | Web                   | Tester sites web dans de vrais navigateurs             |
| **[Playwright](https://playwright.dev/python/)**   | Web (modern)          | Plus rapide + robuste que Selenium, très scriptable    |
| **[PyAutoGUI](https://pyautogui.readthedocs.io/)** | Simule clavier/souris | Tests manuels ou UI non exposées par API               |

---

## ⏱️ 4. **Tests de performance et stress**

| Outil                    | Utilité principale                     | Quand l’utiliser ?                             |
| ------------------------ | -------------------------------------- | ---------------------------------------------- |
| **timeit**               | Benchmark de fonctions simples         | Microbenchmark dans une boucle Python          |
| **pytest-benchmark**     | Intégré à `pytest`                     | Comparer différentes versions ou optimisations |
| **locust**               | Simulation massive d’utilisateurs HTTP | Simuler un site sous charge ou une API REST    |
| **airload**, `wrk`, etc. | Tests de stress réseau / HTTP          | Si tu veux aller plus loin que `ab` / `curl`   |

---

## 🔒 5. **Tests de sécurité et robustesse**

| Outil               | Ce qu’il teste                             | Cas typique                                   |
| ------------------- | ------------------------------------------ | --------------------------------------------- |
| **bandit**          | Vulnérabilités dans le code Python         | Audit de sécurité, devops                     |
| **safety**          | Vulnérabilités dans les packages Python    | Sécurité des dépendances (`requirements.txt`) |
| **pytest-randomly** | Détecte les tests qui dépendent de l’ordre | Robustesse de ton test suite                  |

---

## 🧠 6. **Testing orienté data science / analyse**

| Outil                       | Utilité spécifique                                          |
| --------------------------- | ----------------------------------------------------------- |
| **deepchecks**, **giskard** | Tests de modèles ML (biais, stabilité, cohérence)           |
| **great\_expectations**     | Tests automatisés sur des datasets (validation de pipeline) |
| **mlflow**                  | Suivi et comparaison des runs + test reproductibilité       |

---

## 🎓 Recommandation par usage

| Contexte / Besoin           | Outils recommandés                                |
| --------------------------- | ------------------------------------------------- |
| Projet Python classique     | `pytest` + `hypothesis` + `tox`                   |
| Projet API REST             | `pytest` + `tavern` ou `robotframework` + `httpx` |
| GUI PySide6                 | `pytest-qt` + `QtTest` + mocks                    |
| Projet avec PO / QA non-dev | `Robot Framework` ou `behave`                     |
| Projet Data / ML            | `pandas` + `great_expectations` + `deepchecks`    |
| Automatisation légère       | `doctest`, `invoke`, `click`                      |
