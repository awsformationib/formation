

# 🧮 Fiche Comparative – **Pandas vs Polars** pour la manipulation de données de vols

## 🧠 Objectif

Comparer **syntaxe, performance et fonctionnalités** entre Pandas et Polars pour les opérations fréquentes de traitement de données tabulaires, sur le cas concret de vols (aérien).

---

## ⚙️ 0. Installation

```bash
pip install pandas polars
```

---

## 📦 1. Chargement des données

| Action         | Pandas                     | Polars                                                |
| -------------- | -------------------------- | ----------------------------------------------------- |
| Chargement CSV | `pd.read_csv("vols.csv")`  | `pl.read_csv("vols.csv")`                             |
| Chargement SQL | `pd.read_sql(query, conn)` | ❌ (pas natif, mais possible via PyArrow + ConnectorX) |

---

## 📋 2. Comparaison : actions **simples**

| Opération              | Pandas                                 | Polars                                                                    |
| ---------------------- | -------------------------------------- | ------------------------------------------------------------------------- |
| Aperçu des données     | `df.head()`                            | `df.head()`                                                               |
| Filtrage par condition | `df[df["statut"] == "prévu"]`          | `df.filter(pl.col("statut") == "prévu")`                                  |
| Sélection de colonnes  | `df[["numero", "destination"]]`        | `df.select(["numero", "destination"])`                                    |
| Ajout de colonne       | `df["retard"] = ...`                   | `df.with_columns((pl.col("arrivée") - pl.col("départ")).alias("retard"))` |
| Suppression de colonne | `df.drop(columns=["avion"])`           | `df.drop("avion")`                                                        |
| Conversion datetime    | `pd.to_datetime(df["heure_creation"])` | `df.with_columns(pl.col("heure_creation").str.strptime(pl.Datetime))`     |

---

## 🧠 3. Comparaison : actions **complexes**

| Action avancée                      | Pandas                                                                             | Polars                                                                                  |
| ----------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| GroupBy + Agg. moyenne + count      | `df.groupby("dest").agg({"retard": "mean", "numero": "count"})`                    | `df.groupby("dest").agg([pl.col("retard").mean(), pl.col("numero").count()])`           |
| Pivot table                         | `df.pivot_table(index="dest", columns="statut", values="numero", aggfunc="count")` | `df.pivot(index="dest", columns="statut", values="numero", aggregate_function="count")` |
| Détection d’outliers                | `df[df["retard"] > 360]`                                                           | `df.filter(pl.col("retard") > 360)`                                                     |
| Application d’une fonction Python   | `df["cat"] = df["retard"].apply(fonction)`                                         | ⚠️ Nécessite `.map_elements()` mais déconseillé (Polars préfère expr. vectorielles)     |
| Fusion avec table externe (`merge`) | `pd.merge(df1, df2, on="dest", how="left")`                                        | `df1.join(df2, on="dest", how="left")`                                                  |
| Group-by custom boucle              | possible mais souvent lent ou verbeux                                              | préférable d’éviter les boucles : logique vectorielle recommandée                       |

---

## 📈 4. Performance et efficacité mémoire

| Critère                     | Pandas                                       | Polars                                          |
| --------------------------- | -------------------------------------------- | ----------------------------------------------- |
| Performance (volumétrie ++) | ⚠️ plus lent (single-threaded, objet Python) | ✅ très rapide (multi-threaded, Rust, zero-copy) |
| Conso mémoire               | élevée (objets, copies fréquentes)           | faible (formats compacts, lazy evaluation)      |
| Lazy evaluation             | ❌ non                                        | ✅ oui, via `df.lazy()`                          |
| Support des types Arrow     | partiel                                      | ✅ natif, très efficace avec `Parquet`           |

---

## 🧭 5. Résumé comparatif

| Critère                     | Pandas                                 | Polars                                  |
| --------------------------- | -------------------------------------- | --------------------------------------- |
| Facilité d'apprentissage    | ✅ Très accessible                      | ⚠️ Syntaxe fonctionnelle plus stricte   |
| Compatibilité écosystème    | ✅ Compatible sklearn, matplotlib, etc. | ⚠️ Moins d’intégration Python classique |
| Rapidité / performance      | ⚠️ OK pour fichiers < 1M lignes        | ✅ Optimisé pour gros volumes (10M+)     |
| API vectorielle moderne     | ✅ correcte                             | ✅✅ très riche, très rapide              |
| Utilisation en prod / batch | 🟡 OK mais sensible à l’optimisation   | ✅ recommandé (Rust core + stable)       |

---

## 🧠 Quand choisir Pandas ou Polars ?

| Situation typique                               | Recommandé |
| ----------------------------------------------- | ---------- |
| Petit volume (<100 000 lignes) + visualisation  | **Pandas** |
| Gros volume / besoin de rapidité                | **Polars** |
| Intégration avec sklearn ou matplotlib          | **Pandas** |
| Traitement distribué ou à paralléliser          | **Polars** |
| Flux de données Apache Arrow ou Parquet         | **Polars** |
| Projet éducatif, script simple                  | **Pandas** |
| Pipeline analytique optimisé (ETL, ML pipeline) | **Polars** |


