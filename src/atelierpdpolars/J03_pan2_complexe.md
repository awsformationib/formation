

# 📊 Atelier Pandas – Manipulation des données de vols (version avancée)

## 🎯 Objectif

Apprendre à manipuler efficacement des données de vols en Python avec **Pandas**, à travers des transformations simples et complexes : calculs dérivés, regroupements, pivotements, enrichissements, détection d’anomalies.

---

## 📚 1. Introduction à Pandas (rappel)

| Élément clé   | Description                                       |
| ------------- | ------------------------------------------------- |
| `DataFrame`   | Tableau 2D : colonnes + index                     |
| `Series`      | Colonne individuelle (vecteur)                    |
| Chargement    | `read_csv`, `read_sql`, `read_json`, etc.         |
| Manipulations | Filtrage, transformation, regroupement, nettoyage |
| Export        | `to_csv`, `to_excel`, `to_sql`, etc.              |

---

## 🔌 2. Chargement des vols avec Pandas

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
    df = pd.read_sql("SELECT * FROM vols", conn)
    conn.close()
    return df

df_vols = charger_vols_en_dataframe()
```

---

## 🔍 3. Manipulations simples (rappel)

* `df_vols['statut'] == "prévu"` → filtrage conditionnel
* `df_vols.groupby('destination')` → regroupement
* `df_vols['retard_minutes'] = ...` → nouvelle colonne
* `df_vols.dropna()` / `fillna()` → nettoyage

---

## 🧠 4. **Manipulations complexes** (niveau intermédiaire à avancé)

### 🧮 4.1. Calcul de **retard effectif** (en minutes)

```python
df_vols['heure_decollage'] = pd.to_datetime(df_vols['heure_decollage'])
df_vols['heure_creation'] = pd.to_datetime(df_vols['heure_creation'])

df_vols['duree_attente'] = (df_vols['heure_decollage'] - df_vols['heure_creation']).dt.total_seconds() / 60
```

---

### 📊 4.2. Statistiques par **jour de la semaine**

```python
df_vols['jour'] = df_vols['heure_creation'].dt.day_name()

stats_par_jour = df_vols.groupby('jour').agg({
    'numero': 'count',
    'duree_attente': 'mean'
}).rename(columns={'numero': 'nb_vols', 'duree_attente': 'attente_moy'})
```

---

### 🔁 4.3. **Pivot** : Statuts des vols par destination

```python
pivot_statuts = df_vols.pivot_table(
    index='destination',
    columns='statut',
    values='numero',
    aggfunc='count',
    fill_value=0
)
```

---

### ⚠️ 4.4. Détection de **valeurs anormales**

```python
# Vols dont la durée entre création et décollage dépasse 6h
df_outliers = df_vols[df_vols['duree_attente'] > 360]
```

---

### 🔗 4.5. Fusion avec une table externe (ex: `airports.csv`)

```python
df_airports = pd.read_csv("airports.csv")  # contient 'destination' + 'pays' + 'type'
df_merge = pd.merge(df_vols, df_airports, how='left', on='destination')
```

---

### 🧩 4.6. Application d’une fonction personnalisée

```python
def classer_retard(mins):
    if pd.isna(mins): return "non précisé"
    elif mins < 30: return "court"
    elif mins < 120: return "moyen"
    else: return "long"

df_vols['categorie_retard'] = df_vols['duree_attente'].apply(classer_retard)
```

---

### 🧮 4.7. Boucle sur groupes + statistiques cumulées

```python
stats_par_dest = []

for dest, groupe in df_vols.groupby('destination'):
    moyenne = groupe['duree_attente'].mean()
    nb = groupe.shape[0]
    stats_par_dest.append({'destination': dest, 'nb_vols': nb, 'attente_moy': moyenne})

df_stats = pd.DataFrame(stats_par_dest)
```

---

## 📈 5. Visualisations (bonus)

```python
import matplotlib.pyplot as plt

# Histogramme des retards
df_vols['duree_attente'].dropna().plot(kind='hist', bins=20)
plt.title("Distribution des temps d'attente avant décollage")
plt.xlabel("Minutes")
plt.show()

# Camembert par statut
df_vols['statut'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title("Répartition des statuts de vol")
plt.show()
```

---

## 🛠️ 6. Export des données enrichies

```python
df_vols.to_csv("vols_enrichis.csv", index=False)
df_stats.to_excel("stats_par_destination.xlsx", index=False)
```

---

## 🧪 7. Extensions possibles pour vos participants

| Extension                               | Description                        |
| --------------------------------------- | ---------------------------------- |
| Regrouper par `destination` + `jour`    | pour faire des heatmaps de charge  |
| Intégrer météo simulée                  | pour analyser influence sur retard |
| Créer des indicateurs d'annulation      | via `statut == "annulé"`           |
| Indexation multiple (`MultiIndex`)      | ex: `(destination, jour)`          |
| Stocker dans base avec `df.to_sql(...)` | si besoin de persister             |


