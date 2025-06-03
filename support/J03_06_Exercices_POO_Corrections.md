![Logo](images\logo.png)


---

### 🛠 ## ✈️ Mini-exercice fil rouge : Des piliers POO dans AirOps

On part d’un projet AirOps simplifié, et à chaque étape, on **ajoute un pilier** pour enrichir la conception.
Chaque étape vient avec :
✅ Une explication claire,
✅ Une tâche concrète,
✅ Un objectif pédagogique.

---

### 🟡 **Étape 1 : Encapsulation**

✅ **Explication** :
On regroupe les données (attributs) et les comportements (méthodes) dans des classes, pour éviter d’avoir des variables éparpillées et non sécurisées.

---

🔧 **Tâche** :
Créer une classe `Avion` avec des attributs privés (`_immatriculation`, `_modele`) et des méthodes publiques pour accéder à ces informations (`get_immatriculation()`, `get_modele()`).

---

🎯 **Objectif pédagogique** :
Protéger les attributs internes, exposer seulement ce qui est nécessaire, éviter les modifications directes depuis l’extérieur.

---

### 🟡 **Étape 2 : Abstraction**

✅ **Explication** :
On crée une **interface commune** ou une classe abstraite pour formaliser les comportements attendus, sans définir leur implémentation.

---

🔧 **Tâche** :
Créer une classe abstraite `Personnel` (avec `abc.ABC`) qui impose une méthode `presenter()`.
Créer deux sous-classes : `Pilote` et `AgentSol`, chacune donnant une implémentation spécifique.

---

🎯 **Objectif pédagogique** :
Obliger les sous-classes à respecter un contrat, clarifier les intentions et éviter les oublis.

---

### 🟡 **Étape 3 : Héritage**

✅ **Explication** :
On factorise les comportements communs dans une classe parente pour éviter de dupliquer le code.

---

🔧 **Tâche** :
Créer une classe `Vol` générale avec des méthodes communes (`afficher_details()`).
Créer deux sous-classes : `VolPassagers` (qui a des passagers) et `VolCargo` (qui a une capacité en tonnes), héritant des méthodes de `Vol`.

---

🎯 **Objectif pédagogique** :
Réutiliser le code commun et permettre des spécialisations sans repartir de zéro.

---

### 🟡 **Étape 4 : Polymorphisme**

✅ **Explication** :
On utilise différents objets de manière interchangeable, grâce à une méthode ou interface commune.

---

🔧 **Tâche** :
Créer une fonction `afficher_presentations(personnels)` qui prend une liste mixte de `Pilote` et `AgentSol`, et appelle `presenter()` sur chacun, sans tester leur type.

---

🎯 **Objectif pédagogique** :
Écrire du code générique, extensible, qui s’adapte aux différents types d’objets sans conditions spécifiques.

---

### 🟡 **Étape 5 : Composition et agrégation**

✅ **Explication** :
On construit des objets complexes en reliant plusieurs objets ensemble (fort ou faible), selon leurs dépendances.

---

🔧 **Tâche** :
Dans `VolPassagers`, ajouter un objet `PlanDeVol` qui appartient uniquement à ce vol (composition).
Dans `VolCargo`, relier plusieurs `Pilote` (agrégation), car les pilotes peuvent exister indépendamment.

---

🎯 **Objectif pédagogique** :
Savoir choisir la bonne forme de relation selon la nature du lien, structurer le projet proprement.

---

### 📦 **Livrable final pour les participants**

✅ Un petit projet complet qui combine :

* Encapsulation des données,
* Abstraction des comportements,
* Héritage structuré,
* Polymorphisme généralisé,
* Relations composées et agrégées.
