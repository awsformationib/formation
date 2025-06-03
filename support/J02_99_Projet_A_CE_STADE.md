![Logo](images\logo.png)


## 🛫 **Projet complet AirOps – Version intégratrice (J1 + J2)**

### 📦 Contenu final

* Tous les concepts objets :

  * classes, instances, encapsulation, propriétés, méthodes spéciales
* Relations entre objets :

  * `Vol`, `Avion`, `Piste`, `Affectation`
* Bonnes pratiques :

  * `@dataclass`, `Enum`, `typing`
* Modules standards intégrés :

  * `datetime`, `random`, `uuid`, `collections`, `pathlib`, `csv`, `json`

---

### 📁 Arborescence du projet

```
air_ops/
├── avion.py
├── vol.py
├── piste.py
├── affectation.py
├── simulateur.py        ← génération et organisation des données
├── exporter.py          ← exports CSV / JSON / rapport texte
├── main.py              ← point d’entrée pour tout exécuter
```

---

### 🛠 Points clés inclus

✅ Générer aléatoirement des avions et des vols avec `random`, `uuid`
✅ Encadrer les statuts avec `Enum`
✅ Structurer les classes avec `@dataclass` là où pertinent
✅ Grouper les vols par destination avec `defaultdict`
✅ Organiser une file d’attente de vols avec `deque`
✅ Exporter les résultats en :

* CSV (`csv` + `pathlib`)
* JSON (`json` + `pathlib`)
  ✅ Annoter tous les fichiers avec `typing`

---
