##  Packager un projet Python

* 📦 livrer à un **client final pour exécution directe (exécutable)**,
* 📚 publier dans un **repository Python (PyPI, entreprise, etc.)**,
* 💼 livrer pour usage interne (ZIP, container, etc.).

---

## 🧰 1. LIVRAISON EN TANT QUE PACKAGE PYTHON INSTALLABLE (setuptools / poetry)

### 🔧 Utilisation : Publication sur PyPI / registry privé

### 📂 Arborescence type

```
monprojet/
├── monprojet/
│   ├── __init__.py
│   ├── core.py
│   └── cli.py
├── tests/
├── pyproject.toml      ✅ recommandé (poetry/setuptools)
├── README.md
├── LICENSE
└── requirements.txt
```

### 📌 Avec `setuptools` (via `pyproject.toml`)

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "monprojet"
version = "0.1.0"
description = "Mon outil de vol"
authors = [{name = "Denis"}]
dependencies = ["pandas", "numpy"]

[project.scripts]
monprojet-cli = "monprojet.cli:main"
```

📦 Packaging :

```bash
python -m build
pip install dist/monprojet-0.1.0-py3-none-any.whl
```

🧪 Publication :

```bash
twine upload dist/*
```

👉 Pour un client : tu fournis le `.whl` ou `.tar.gz`.

---

## 💼 2. LIVRAISON DIRECTE AU CLIENT – SCRIPT + DÉPENDANCES

### Option A : 📁 Archive ZIP avec requirements

1. Structure :

```
monprojet/
├── monprojet/
├── requirements.txt
└── run.sh (ou run.bat)
```

2. Exemple `run.sh` :

```bash
#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python monprojet/cli.py
```

3. Tu compresses avec :

```bash
zip -r monprojet_livraison.zip monprojet/ requirements.txt run.sh
```

---

## 🧊 3. LIVRAISON AVEC EXÉCUTABLE (PyInstaller / cx\_Freeze)

### 🎯 Utilisation : Client sans Python installé

### Option A : PyInstaller

```bash
pip install pyinstaller
pyinstaller --onefile monprojet/cli.py
```

→ Tu obtiens un exécutable unique : `dist/cli.exe` ou `cli` (Linux/Mac).

📝 Pour customisation :

```bash
pyinstaller --onefile --icon=app.ico --name=vol-app monprojet/cli.py
```

📁 Tu livres :

* le `.exe` ou `.bin`,
* un README pour l’usage.

---

## 🐳 4. LIVRAISON DANS UN CONTENEUR DOCKER

### 🎯 Utilisation : CI/CD, portabilité maximale

### `Dockerfile` minimal :

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "monprojet/cli.py"]
```

👉 Build :

```bash
docker build -t monprojet .
```

👉 Run :

```bash
docker run --rm monprojet
```

→ Tu peux livrer l’image via :

* un `Docker Hub`,
* une archive `.tar` : `docker save`.

---

## 🔚 Résumé : Quelle méthode choisir ?

| Objectif                          | Solution recommandée                          |
| --------------------------------- | --------------------------------------------- |
| Publication open-source / interne | ✅ `pyproject.toml` + `setuptools` ou `poetry` |
| Client avec Python installé       | ✅ Archive ZIP + `run.sh`                      |
| Client **sans Python**            | ✅ `PyInstaller` exécutable                    |
| Livraison Cloud / CI              | ✅ Docker container                            |
| Registry privé (entreprise)       | ✅ `twine upload` / `Artifactory`              |

