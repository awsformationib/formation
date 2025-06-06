# Démo complète : équivalent Python de `PROC FREQ` et `PROC GLM` de SAS

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Chargement de données (ex. similaire à SASHELP.CLASS)
data = pd.DataFrame({
    'Sex': ['M', 'F', 'F', 'M', 'F', 'M', 'F', 'F', 'M', 'M'],
    'Age': [14, 13, 13, 14, 12, 15, 12, 15, 13, 14],
    'Height': [69, 56.5, 65.3, 63.5, 62.8, 67, 59.8, 62.5, 66.5, 61.5],
    'Weight': [112.5, 84, 98, 102.5, 102.5, 112, 92, 112.5, 120, 110]
})

# === 1. Équivalent PROC FREQ ===
print("\n==> Tableau de fréquence (PROC FREQ)")
print(data['Sex'].value_counts())

print("\n==> Fréquence relative")
print(data['Sex'].value_counts(normalize=True))

# Visualisation
sns.countplot(data=data, x='Sex')
plt.title("Distribution du sexe")
plt.show()

# === 2. Équivalent PROC GLM (modèle linéaire général) ===
# Exemple : prédire le poids par la taille et le sexe (Weight ~ Height + Sex)

# Avec formula API (comme en SAS)
model = smf.ols(formula='Weight ~ Height + Sex', data=data).fit()

print("\n==> Résumé du modèle linéaire (PROC GLM)")
print(model.summary())

# Visualisation des résidus
sns.residplot(x=model.fittedvalues, y=model.resid, lowess=True)
plt.xlabel("Valeurs prédites")
plt.ylabel("Résidus")
plt.title("Analyse des résidus")
plt.show()

# === 3. Prédictions (comme PREDICT dans PROC SCORE ou GLM) ===
data['PredictedWeight'] = model.predict(data)
print("\n==> Prédictions de poids")
print(data[['Height', 'Sex', 'Weight', 'PredictedWeight']])
