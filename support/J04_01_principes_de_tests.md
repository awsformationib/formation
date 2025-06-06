![Logo](images\logo.png)

## 🧩 Fiche – Qualité logicielle et rôle des tests

---

### 🎯 **Objectif**

Comprendre pourquoi les tests sont un pilier essentiel de la qualité logicielle, quels sont leurs types, et pourquoi aucune équipe sérieuse (ou développeur sérieux) ne peut s’en passer, même dans un projet Python.

---

### 🏗 **Pourquoi parle-t-on de qualité ?**

En développement, la qualité ne se limite pas à :
✅ écrire du code qui marche “aujourd’hui”.
Elle englobe aussi :
✅ la maintenabilité,
✅ la robustesse face aux changements,
✅ la compréhension par d’autres développeurs,
✅ la prévention des régressions.

Sans outils et bonnes pratiques de qualité, un projet :
❌ devient vite fragile,
❌ accumule des bugs cachés,
❌ ralentit dès qu’on veut l’étendre ou le corriger.

---

### 🔍 **Pourquoi écrire des tests ?**

Les tests sont un **filet de sécurité** :

* Ils vérifient qu’une partie du code (fonction, classe, module) se comporte comme attendu.
* Ils permettent de détecter rapidement des erreurs quand on modifie le code.
* Ils réduisent la dépendance à des vérifications manuelles longues et fatigantes.

Sans tests, chaque changement peut potentiellement :
❌ casser une fonctionnalité existante,
❌ produire des effets de bord invisibles,
❌ faire perdre confiance à l’équipe.

---

### 🧪 **Types de tests à connaître**

| Type de test        | But principal                                                     |
| ------------------- | ----------------------------------------------------------------- |
| Test unitaire       | Vérifie une fonction ou classe isolée.                            |
| Test d’intégration  | Vérifie que plusieurs modules interagissent bien.                 |
| Test fonctionnel    | Vérifie un scénario métier complet (du point de vue utilisateur). |
| Test de performance | Vérifie que le système tient la charge.                           |

---

### 📦 **Pourquoi même sur un projet Python ?**

En Python, le côté dynamique rend :
✅ l’écriture rapide,
✅ l’évolution flexible,
❌ mais l’apparition d’erreurs sournoises plus probable (pas de compilation stricte).

C’est pourquoi :

* On utilise des tests unitaires (avec `unittest`, `pytest`).
* On valide l’ensemble (intégration, end-to-end).
* On automatise les vérifications (CI/CD, GitHub Actions, GitLab CI).

---

### ✈️ **Lien avec AirOps**

Dans notre projet AirOps, sans tests, comment savoir que :

* Le calcul des vols disponibles est toujours correct ?
* L’affectation des pilotes ne génère pas de conflit ?
* Les exports de rapports ne régressent pas quand on modifie un détail ?

**Réponse :** on ne peut pas le savoir sans tests, ou alors on doit tout retester manuellement à chaque fois → pas réaliste.

---

### 🚀 **À quoi ça nous prépare ?**

Dans la fiche suivante, nous allons :
✅ Découvrir les outils natifs de Python (`unittest`).
✅ Apprendre à écrire nos premiers tests unitaires.
✅ Voir comment structurer et automatiser ces tests pour garantir la qualité du projet AirOps.

---

### 🧪 **Questions préliminaires**

1. As-tu déjà été bloqué par une modification qui casse une autre partie du projet ?
2. Qu’est-ce qui est plus rapide : corriger un bug découvert en test automatique, ou un bug rapporté par un client ?
3. Quand doit-on commencer à écrire des tests : avant, pendant, ou après le code ?

---
