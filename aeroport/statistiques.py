import pandas as pd

from database import WithPandas

if __name__ == "__main__":
    db = WithPandas(host="127.0.0.1", login="root", password="", database="formation")
    df_vols = db.lire_vols()
    print(df_vols.head(10))

    df_vols.info()  # Types, nulls
    df_vols.describe()  # Statistiques sur colonnes numériques
    print(df_vols.columns)  # Liste des colonnes
    print(df_vols.shape)  # (lignes, colonnes)

    print("-----------------------")
    df_dests = df_vols['destination']
    print(df_dests)

    df_miami = df_vols[df_vols['destination'] == 'Miami']
    df_miami = df_miami.drop(columns=['destination'])

    df_miami['heure_creation'] = pd.to_datetime(df_miami['heure_creation'])
    df_miami['jour_semaine'] = df_miami['heure_creation'].dt.day_name()

    print("-----------------------")
    print(df_miami)

    gp = df_vols.groupby('destination')['numero'].count()
    print(gp)