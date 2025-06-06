=
## 🎭 Fiche Playwright – Tests automatisés Web (et API)

---

### ✅ Pourquoi utiliser Playwright ?

| Avantages clés                | Détails                                                                      |
| ----------------------------- | ---------------------------------------------------------------------------- |
| 🎯 Multi-navigateurs          | Support natif de **Chromium**, **Firefox**, **WebKit** (Safari)              |
| ⚡ Très rapide                 | Contrôle **bas niveau** du navigateur, sans dépendre de Selenium Grid        |
| 🧪 API de test riche          | Test des **UI**, des **réponses réseau**, des **fichiers téléchargés**, etc. |
| 🤖 Headless ou non            | Possibilité d’avoir un mode **visible pour déboguer**                        |
| 🔄 Tests API REST intégrés    | `request.new_context()` permet de tester les API sans interface web          |
| 🧱 Intégration facile         | Compatible avec `pytest`, `unittest`, ou même CLI Playwright                 |
| 📸 Capture screenshots/vidéos | Debugging facilité avec images ou enregistrements                            |
| 🌐 Support i18n & mobile      | Tests multi-langues, responsive, devices simulés                             |

---

### 📦 Installation

```bash
pip install playwright
playwright install
```

Ce dernier installe les navigateurs Chromium, Firefox, WebKit nécessaires aux tests.

---

### 📄 Exemple – Test simple de page web

```python
from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://example.com")
        assert page.title() == "Example Domain"
        browser.close()
```

---

### 🔁 Exemple – Appel API REST avec Playwright

```python
from playwright.sync_api import sync_playwright

def test_api_vol():
    with sync_playwright() as p:
        req = p.request.new_context()
        resp = req.get("http://localhost:5000/vols/123")
        assert resp.status == 200
        assert resp.json()["numero"] == 123
```

---

### ▶️ Exécution CLI (sans pytest)

```bash
python test_playwright_api.py
```

Ou avec `pytest` :

```bash
pytest test_playwright_api.py
```

---

### 🧩 Intégration dans un projet plus large

* Pour **tester l’UI d’une app Flask**, Playwright peut simuler la navigation (clics, formulaires).
* Pour **vérifier la présence d’un vol sur une page HTML**, on peut combiner Playwright + requêtes API.
* Pour **vérifier les appels réseau**, on peut utiliser les **routes interceptées** (`page.route`) pour mocker ou monitorer les appels.

---

### 🔐 Bonus – Authentification

Playwright permet de :

* simuler un login (formulaire, cookie, header),
* **sauvegarder une session de navigation** (`storage_state.json`) à réutiliser dans plusieurs tests.

---

## 🆚 Playwright vs Selenium

| Critère         | Playwright          | Selenium               |
| --------------- | ------------------- | ---------------------- |
| Performance     | ⚡ Très rapide       | 🐢 Plus lent           |
| Simplicité      | API moderne         | API plus verbeuse      |
| Mobile / device | ✅ Oui               | ✅ Oui                  |
| Test API REST   | ✅ Intégré           | ❌ Nécessite `requests` |
| Débogage        | Screenshot + video  | Screenshot uniquement  |
| Dépendances     | Moins lourdes       | Nécessite WebDriver    |
| Headless        | ✅ Excellent support | ✅                      |
