
# 🧩 Fiche – Les Layouts dans PySide6

## 🎯 Objectif des layouts

Un **layout (disposition)** gère automatiquement la **position**, la **taille**, et **l’agencement dynamique** des widgets dans une fenêtre. Il remplace les `.move()` et `.resize()` qui deviennent inutiles voire dangereux à maintenir.

---

## 🧠 Principes clés

| Principe             | Explication                                                              |
| -------------------- | ------------------------------------------------------------------------ |
| Layout imbriqué      | Un layout peut contenir d'autres layouts                                 |
| Évolutif             | S'adapte automatiquement au redimensionnement de la fenêtre              |
| Spacing & Margins    | Gère les espaces entre widgets et les bords                              |
| Layouts hiérarchisés | On organise les composants en structure arborescente                     |
| Parenté automatique  | Si un layout est appliqué à un `QWidget`, les widgets sont gérés par lui |

---

## 📦 Layouts disponibles dans PySide6

| Classe Qt Layout | Description                                                          |
| ---------------- | -------------------------------------------------------------------- |
| `QVBoxLayout`    | Organisation verticale (haut → bas)                                  |
| `QHBoxLayout`    | Organisation horizontale (gauche → droite)                           |
| `QGridLayout`    | Grille avec lignes/colonnes (tableau)                                |
| `QFormLayout`    | Colonnes label + champ, idéal pour les formulaires                   |
| `QStackedLayout` | Superpose plusieurs widgets, un seul affiché à la fois (multi-pages) |

---

## ✅ Exemples de base

### 🔹 1. `QVBoxLayout`

```python
layout = QVBoxLayout()
layout.addWidget(QLabel("Nom"))
layout.addWidget(QLineEdit())
layout.addWidget(QPushButton("Valider"))

fenetre.setLayout(layout)
```

### 🔹 2. `QHBoxLayout`

```python
layout = QHBoxLayout()
layout.addWidget(QPushButton("Annuler"))
layout.addWidget(QPushButton("OK"))
fenetre.setLayout(layout)
```

### 🔹 3. `QGridLayout`

```python
layout = QGridLayout()
layout.addWidget(QLabel("Nom"), 0, 0)
layout.addWidget(QLineEdit(), 0, 1)
layout.addWidget(QLabel("Âge"), 1, 0)
layout.addWidget(QSpinBox(), 1, 1)
fenetre.setLayout(layout)
```

### 🔹 4. `QFormLayout`

```python
layout = QFormLayout()
layout.addRow("Nom :", QLineEdit())
layout.addRow("Email :", QLineEdit())
fenetre.setLayout(layout)
```

### 🔹 5. `QStackedLayout`

```python
stack = QStackedLayout()
stack.addWidget(page1)
stack.addWidget(page2)
stack.setCurrentIndex(0)  # ou 1 pour afficher l'autre page
fenetre.setLayout(stack)
```

---

## 🔁 Combinaisons & imbrication

```python
main_layout = QVBoxLayout()
form = QFormLayout()
form.addRow("Nom :", QLineEdit())
form.addRow("Email :", QLineEdit())

btn_layout = QHBoxLayout()
btn_layout.addWidget(QPushButton("OK"))
btn_layout.addWidget(QPushButton("Annuler"))

main_layout.addLayout(form)
main_layout.addLayout(btn_layout)
fenetre.setLayout(main_layout)
```

---

## 🧰 Options avancées

| Option                    | Code                                             |
| ------------------------- | ------------------------------------------------ |
| Espacement entre widgets  | `layout.setSpacing(10)`                          |
| Marges du layout          | `layout.setContentsMargins(10, 10, 10, 10)`      |
| Alignement dans un layout | `layout.addWidget(btn, alignment=Qt.AlignRight)` |
| Stretch                   | `layout.addStretch()` pour forcer un espacement  |
| Stretch entre widgets     | `layout.setStretch(index, factor)`               |

---

## 🎯 Bonnes pratiques

✅ Toujours utiliser un `layout`, jamais `.move()`
✅ Grouper les composants similaires dans des layouts dédiés
✅ Tester le redimensionnement de la fenêtre pour s’assurer du comportement fluide
✅ `QGroupBox` ou `QFrame` permettent de **visuellement structurer** les sections

---

## 🧪 Pour aller plus loin

* Utiliser `QSplitter` pour des interfaces redimensionnables par l'utilisateur
* Tester les effets de `addStretch()` et `setStretchFactor()`
* Créer des interfaces responsives avec `QScrollArea` et layouts flexibles

