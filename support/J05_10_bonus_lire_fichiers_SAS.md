![Logo](images\logo.png)

---

## ✅ 1. Lecture des **jeux de données SAS (`.sas7bdat`)**

| 📂 Fichier SAS        | Lecture en Python ? | Bibliothèque(s)                                           | Remarques                |
| --------------------- | ------------------- | --------------------------------------------------------- | ------------------------ |
| `.sas7bdat` (données) | ✅ Oui               | `pandas`, `pyreadstat`, `sas7bdat`                        | Très utilisé en pratique |
| `.xpt` (transport)    | ✅ Oui               | `pandas.read_sas()` avec `format='xport'` ou `pyreadstat` | Format d’échange SAS     |

### Exemple avec Pandas :

```
import pandas as pd

df = pd.read_sas("fichier.sas7bdat", format='sas7bdat')
```

### Exemple avec Pyreadstat (plus rapide et fiable) :

```
import pyreadstat

df, meta = pyreadstat.read_sas7bdat("fichier.sas7bdat")
```

---

## ❌ 2. Lecture des fichiers **catalogues SAS (`.sas7bcat`)**

| 📂 Fichier SAS           | Lecture en Python ? | Explication                                                 |
| ------------------------ | ------------------- | ----------------------------------------------------------- |
| `.sas7bcat` (catalogues) | ❌ Non               | Fichiers binaires propriétaires (formats, macros compilées) |

> 📌 **Pas lisible** directement avec Python. Il faut exporter les formats ou macros en SAS (via `PROC FORMAT CNTLOUT=`) pour ensuite les lire en `.csv`.

---

## ✅ 3. Lecture des **fichiers `.xpt` (SAS transport)**

| 📂 Fichier SAS | Lecture en Python ? | Bibliothèque(s)        |
| -------------- | ------------------- | ---------------------- |
| `.xpt`         | ✅ Oui               | `pandas`, `pyreadstat` |

```
df = pd.read_sas("fichier.xpt", format='xport')
```

---

## ⚠️ 4. Lecture des **fichiers de log et de script SAS**

| 📂 Fichier SAS                 | Lecture      | Méthode                      |
| ------------------------------ | ------------ | ---------------------------- |
| `.sas`, `.log`, `.lst`, `.txt` | ✅ Texte brut | `open("fichier.sas").read()` |

> 💡 Tu peux analyser les erreurs dans les `.log` ou extraire du code SAS via regex, NLP, etc.

---

## ❓ 5. Lecture indirecte des formats personnalisés (`.fmt`, via export CSV)

* En SAS :

```sas
proc format cntlout=fmtlib;
run;

proc export data=fmtlib outfile="formats.csv" dbms=csv;
run;
```

* En Python :

```
import pandas as pd
formats = pd.read_csv("formats.csv")
```

---

## 🔄 6. Lecture depuis un **serveur SAS actif** (avancé)

| Outil Python   | Fonction                       | Connexion                                    |
| -------------- | ------------------------------ | -------------------------------------------- |
| `saspy`        | Interagir avec un SAS installé | 🔧 Requiert configuration (local ou distant) |
| `SAS Viya SDK` | Appel d’API REST SAS           | Pour serveurs Viya uniquement                |

---

## ✅ Résumé synthétique

| Type de fichier SAS     | Peut-on lire avec Python ?   | Bibliothèques           |
| ----------------------- | ---------------------------- | ----------------------- |
| `.sas7bdat`             | ✅ Oui                        | `pandas`, `pyreadstat`  |
| `.xpt`                  | ✅ Oui                        | `pandas`, `pyreadstat`  |
| `.sas7bcat`             | ❌ Non (propriétaire binaire) | —                       |
| `.sas`, `.log`, `.lst`  | ✅ Oui (texte)                | `open()`                |
| `.fmt`                  | ⚠️ Via export CSV            | `pandas.read_csv`       |
| Depuis SAS actif (live) | ✅ Oui (avancé)               | `saspy`, `SAS Viya SDK` |

---

Voici une **méthode simple et efficace** pour convertir un fichier **SAS `.sas7bdat`** (ou `.xpt`) vers **Parquet** avec **Python** 🐍.

---

## ✅ Étapes de conversion SAS → Parquet

### 📦 Bibliothèques nécessaires :

Il faut les bibliothèques suivantes :

```
pip install pyreadstat pyarrow pandas
```

---
## Exemple SAS->Parquet


### 🔁 Étape 1 : Lire le fichier `.sas7bdat` avec `pyreadstat`

```
import pyreadstat

# Lecture du fichier SAS
df, meta = pyreadstat.read_sas7bdat("fichier.sas7bdat")
```

> `meta` contient les métadonnées (libellés de variables, formats SAS, etc.)

---

### 💾 Étape 2 : Écrire le DataFrame en Parquet

```
# Convertir vers Parquet avec compression 'snappy'
df.to_parquet("fichier.parquet", engine="pyarrow", compression="snappy")
```

---

## 📝 Variante : si le fichier SAS est un `.xpt`

```
df, meta = pyreadstat.read_xport("fichier.xpt")
df.to_parquet("fichier.parquet", engine="pyarrow")
```

---

## 🔍 Vérification (optionnelle)

```
import pandas as pd

# Lecture du fichier Parquet
df2 = pd.read_parquet("fichier.parquet")
print(df2.head())
```

---

## 📌 Résumé complet

| Étape | Description                      | Code clé                               |
| ----- | -------------------------------- | -------------------------------------- |
| 1     | Lire fichier `.sas7bdat`         | `read_sas7bdat()`                      |
| 2     | Convertir vers `.parquet`        | `df.to_parquet(..., engine="pyarrow")` |
| 3     | (Optionnel) Vérifier le résultat | `pd.read_parquet()`                    |

---
