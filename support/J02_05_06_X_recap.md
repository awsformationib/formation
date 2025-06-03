![Logo](images\logo.png)


## 🧩 Mini-Fiche Bilan – Modules standards 

### ✅ Modules abordés

| Module | Rôle dans le projet `AirOps` | Bénéfice apporté |
|--------|------------------------------|------------------|
| `datetime` | Enregistrer l’heure de création, décollage, atterrissage | Gestion du temps fiable |
| `random` | Générer des numéros de vol, villes aléatoires | Simulation, test rapide |
| `uuid` | Créer des identifiants uniques pour les objets | Unicité garantie |
| `enum` | Encadrer les statuts des vols (`prévu`, `en cours`, etc.) | Code plus robuste et lisible |
| `dataclasses` | Écrire des classes plus courtes et expressives | Gain de temps + lisibilité |
| `typing` | Annoter les types pour les outils et humains | Aide au développement + vérification statique |

---

### 🔁 Questions pour remise en mémoire rapide

1. Quelle est la différence entre un `Enum` et une simple chaîne de caractères ?
2. Pourquoi `uuid4()` est-il mieux qu’un simple compteur pour identifier les objets ?
3. Que permet `field(default_factory=...)` dans une `@dataclass` ?
4. Que vaut `Optional[datetime]` si l’objet n’a pas encore d’heure définie ?
5. Comment `typing` améliore-t-il la collaboration dans une équipe ?
---

### 📌 À retenir

> Ces modules sont **disponibles nativement** en Python (aucune installation) et sont **largement utilisés en production**.  
> Maîtriser leur usage courant est un **pré-requis pour développer en Python moderne**.
