
# 📊 Atelier Pandas – Manipulation des données de vols

## 🎯 Objectif

Apprendre les bases de la bibliothèque **Pandas** en Python, avec un cas concret : les données de vols extraites depuis une base MySQL ou une API Flask.

---

## 📚 1. Introduction à Pandas

### 🧠 Principes de base

| Élément clé | Description                                                                             |
| ----------- | --------------------------------------------------------------------------------------- |
| `DataFrame` | Tableau 2D (colonnes nommées, indexées) équivalent à une feuille Excel ou une table SQL |
| `Series`    | Colonne ou vecteur indexé                                                               |
| Chargement  | Depuis CSV, Excel, base SQL, dictionnaire, JSON, etc.                                   |
| Traitement  | Indexation, filtrage, groupement, transformations, fusions, nettoyage, etc.             |

---

## 🔌 2. Connexion à la base & chargement des vols avec Pandas

```python
import pandas as pd
import mysql.connector

def charger_vols_en_dataframe():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="motdepasse",
        database="formation"
    )
    query = "SELECT * FROM vols"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

df_vols = charger_vols_en_dataframe()
print(df_vols.head())
```

---

## 🧪 3. Opérations fréquentes avec DataFrames

### 📌 Infos générales

```python
df_vols.info()        # Types, nulls
df_vols.describe()    # Statistiques sur colonnes numériques
df_vols.columns       # Liste des colonnes
df_vols.shape         # (lignes, colonnes)
```

---

### 🔍 Sélection et filtrage

```python
# Colonnes
df_vols['destination']
df_vols[['numero', 'statut']]

# Lignes selon condition
df_vols[df_vols['statut'] == 'prévu']
df_vols[df_vols['destination'].str.contains("Paris")]

# Ligne par position
df_vols.iloc[0]
```

---

### ✂️ Ajout et suppression de colonnes

```python
df_vols['retard_minutes'] = (df_vols['heure_arrivee'] - df_vols['heure_decollage']).dt.total_seconds() / 60

# Suppression
df_vols.drop(columns=['avion'], inplace=True)
```

---

### 📆 Manipulations temporelles

```python
df_vols['heure_creation'] = pd.to_datetime(df_vols['heure_creation'])
df_vols['jour_semaine'] = df_vols['heure_creation'].dt.day_name()
```

---

### 🔢 Groupements et agrégations

```python
df_vols.groupby('destination')['numero'].count()
df_vols.groupby('statut').agg({'numero': 'count', 'retard_minutes': 'mean'})
```

---

### 🔁 Tri et réindexation

```python
df_vols.sort_values(by='heure_creation', ascending=False)
df_vols.reset_index(drop=True, inplace=True)
```

---

### 🔍 Valeurs manquantes

```python
df_vols.isna().sum()
df_vols = df_vols.dropna(subset=['heure_decollage'])
```

---

## 🖇️ 4. Export des résultats

```python
df_vols.to_csv("vols_analyse.csv", index=False)
df_vols.to_excel("vols_rapport.xlsx", index=False)
```

---

## 🔄 5. Bonus : Visualisation simple

```python
import matplotlib.pyplot as plt

df_vols['destination'].value_counts().plot(kind='bar', title="Nombre de vols par destination")
plt.show()
```

---

## 📌 Résumé : À retenir sur Pandas

| Action                  | Méthode clé                 |
| ----------------------- | --------------------------- |
| Charger CSV/SQL         | `read_csv()` / `read_sql()` |
| Filtrer                 | `df[...]` ou `df.query()`   |
| Transformer une colonne | `df['col'] = ...`           |
| Grouper & agréger       | `groupby()` + `agg()`       |
| Nettoyer les nulls      | `dropna()`, `fillna()`      |
| Fusionner               | `merge()`, `concat()`       |
| Exporter                | `to_csv()`, `to_excel()`    |

---
