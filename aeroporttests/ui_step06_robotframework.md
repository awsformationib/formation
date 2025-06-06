
# 🤖 Fiche Démarrage – **Robot Framework**

## 🧰 1. Installation de base

```bash
# Installer Robot Framework
pip install robotframework

# Pour tester des APIs REST
pip install robotframework-requests

# Pour tester des interfaces Qt/PySide6 : option avancée
pip install robotframework-pytest

# Vérification
robot --version
```

---

## 📂 2. Structure d’un projet de test

Exemple :

```
tests_robot/
├── tests/
│   └── avion_api.robot
├── resources/
│   └── keywords.robot (facultatif)
└── variables/
    └── variables.py (facultatif)
```

---

## ✍️ 3. Exemple de test API – `avion_api.robot`

```robot
*** Settings ***
Library    RequestsLibrary
Suite Setup    Create Session    avion_api    http://localhost:5000/api

*** Test Cases ***
Ajouter Un Avion
    [Tags]    POST
    ${data}=    Create Dictionary    id=200    modele=RFTest    description=Robot    vitesse_max=999
    ${resp}=    Post Request    avion_api    /avions    json=${data}
    Should Be Equal As Integers    ${resp.status_code}    201

Vérifier Que L'Avion Existe
    ${resp}=    Get Request    avion_api    /avions
    Should Contain    ${resp.text}    RFTest

Supprimer L'Avion Test
    ${resp}=    Delete Request    avion_api    /avions/200
    Should Be Equal As Integers    ${resp.status_code}    204
```

---

## 🚀 4. Lancer les tests

```bash
robot tests/
```

* Résultat HTML dans `report.html`, `log.html` (automatiquement générés)

---

## 🛠️ 5. Syntaxe utile de Robot Framework

| Action                      | Syntaxe                                              |
| --------------------------- | ---------------------------------------------------- |
| Définir une bibliothèque    | `Library    RequestsLibrary`                         |
| Créer un dictionnaire       | `Create Dictionary    key=value`                     |
| Envoyer une requête POST    | `Post Request    alias    /endpoint    json=${data}` |
| Vérifier une réponse        | `Should Be Equal As Integers` ou `Should Contain`    |
| Tags pour filtrer les tests | `[Tags]    API    rapide`                            |

---

## 🧪 6. Pour aller plus loin

* Tests Web avec `SeleniumLibrary`
* Tests de fichiers avec `OperatingSystem`
* Tests personnalisés avec des **mots-clés Python**
* Intégration avec CI : `robot --outputdir results/ tests/`

---

## 📌 Résumé : Avantages de Robot Framework

| ✅ Atout                | 🔍 Description                            |
| ---------------------- | ----------------------------------------- |
| Syntaxe lisible        | Tableaux de mots-clés (semblable à Excel) |
| Extensible             | Python, Shell, REST, Selenium, etc.       |
| Rapports HTML intégrés | Générés à chaque run                      |
| Utilisable sans coder  | Accessible aux non-développeurs           |

---
