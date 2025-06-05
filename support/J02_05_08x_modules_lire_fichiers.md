![Logo](images\logo.png)

## Lire de très gros fichiers

---

### 🔹 **1. Lecture ligne par ligne avec `open()` (standard)**

**Avantages :** pas besoin de packages externes, faible consommation mémoire
**Inconvénients :** un peu plus lent que certaines autres solutions

```
with open("fichier.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        # traitement de la ligne
        print(ligne.strip())
```

---

### 🔹 **2. Lecture par blocs (buffer) avec `read(size)`**

**Avantages :** permet un contrôle fin sur la mémoire
**Inconvénients :** nécessite de gérer la séparation des lignes

```
def lire_par_blocs(fichier, taille_bloc=1024*1024):  # 1 Mo
    with open(fichier, "r", encoding="utf-8") as f:
        while True:
            bloc = f.read(taille_bloc)
            if not bloc:
                break
            # traitement du bloc
            print(bloc)

lire_par_blocs("fichier.txt")
```

---

### 🔹 **3. `fileinput` (standard, pour plusieurs fichiers ou en pipe)**

**Avantages :** utile pour lire plusieurs fichiers comme un seul
**Inconvénients :** moins connu, pas plus rapide que `open()`

```
import fileinput

for ligne in fileinput.input(files=["fichier1.txt", "fichier2.txt"]):
    print(ligne.strip())
```

---

### 🔹 **4. Utilisation de `pandas` pour fichiers structurés (CSV, etc.)**

**Avantages :** très pratique pour les données tabulaires
**Inconvénients :** charge tout en mémoire, donc peu adapté pour des très gros fichiers

```
import pandas as pd

# Moins efficace pour très gros fichiers, mais possible :
df = pd.read_csv("gros_fichier.csv", chunksize=100000)
for chunk in df:
    print(chunk.head())
```

---

### 🔹 **5. `csv` avec lecture en streaming (standard)**

**Avantages :** adapté pour les gros fichiers CSV sans tout charger

```
import csv

with open("gros_fichier.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

---

### 🔹 **6. Utilisation de `smart_open` (si fichier sur S3, GCS, etc.)**

**Package externe :** `smart_open`
**Avantages :** lecture à distance, supporte S3, GCS, HTTP…

```
pip install smart_open
```

```
from smart_open import open

with open('s3://bucket/mon_fichier.txt', 'r') as f:
    for ligne in f:
        print(ligne)
```

---

### 🔹 **7. `dask` pour les gros fichiers tabulaires**

**Package externe :** `dask`
**Avantages :** lecture paresseuse (lazy), traitement parallèle

```
pip install dask
```

```
import dask.dataframe as dd

df = dd.read_csv("gros_fichier.csv")
print(df.head())  # Ne charge que ce qui est nécessaire
```

---

### 🔹 **8. `mmap` (memory-mapped files)**

**Avantages :** très rapide, accès aléatoire sans tout charger
**Inconvénients :** plus complexe à manipuler, surtout si fichier non structuré

```
import mmap

with open("gros_fichier.txt", "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0)
    while line := mm.readline():
        print(line.decode().strip())
    mm.close()
```

---

### ✅ **Conclusion**

| Méthode                  | Mémoire efficace | Lecture rapide | Complexité | Remarques                                 |
| ------------------------ | ---------------- | -------------- | ---------- | ----------------------------------------- |
| `open()` ligne par ligne | ✅                | ✅              | 🟢         | Le plus simple                            |
| `read()` en blocs        | ✅                | ✅              | 🟡         | À utiliser si besoin de contrôler le flux |
| `pandas.read_csv()`      | ❌                | ✅              | 🟢         | Pas adapté aux très gros fichiers         |
| `csv.reader()`           | ✅                | ✅              | 🟢         | Simple et efficace                        |
| `dask`                   | ✅                | ✅✅             | 🟡         | Idéal pour très gros CSV                  |
| `mmap`                   | ✅✅               | ✅✅             | 🔴         | Très rapide, mais complexe                |
| `smart_open`             | ✅                | ✅              | 🟢         | Pour fichiers distants                    |
