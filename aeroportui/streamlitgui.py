
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#ALTERNATIVES : PandasGUI, D-Tale, Notebook+qgrid/ipywidgets
import random

st.set_page_config(layout="wide")

# 🔹 Charger un DataFrame
st.title("Explorateur de DataFrame interactif")

uploaded_file = st.file_uploader("Téléversez un fichier CSV (;)", type=["csv"])
if uploaded_file:
    df =              pd.read_csv(uploaded_file,delimiter=";")


    st.subheader("Aperçu des données")
    st.dataframe(df)

    # 🔹 Statistiques descriptives
    if st.checkbox("Afficher les statistiques descriptives"):
        st.write(df.describe())

    # 🔹 Colonnes numériques et non numériques
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    object_cols = df.select_dtypes(exclude='number').columns.tolist()

    # 🔹 Filtrage simple
    st.subheader("Filtrage rapide")
    col_to_filter = st.selectbox("Choisir une colonne à filtrer", df.columns)
    if df[col_to_filter].dtype == "object":
        val = st.selectbox("Valeur", df[col_to_filter].unique())
        st.dataframe(df[df[col_to_filter] == val])
    else:
        min_val, max_val = df[col_to_filter].min(), df[col_to_filter].max()
        val_range = st.slider("Intervalle", float(min_val), float(max_val), (float(min_val), float(max_val)))
        st.dataframe(df[df[col_to_filter].between(*val_range)])

    # 🔹 Graphique
    st.subheader("Visualisation")
    col_x = st.selectbox("Axe X", numeric_cols)
    col_y = st.selectbox("Axe Y", numeric_cols)
    hue_col = st.selectbox("Couleur (optionnelle)", [""] + object_cols)

    fig, ax = plt.subplots()
    if hue_col == "":
        sns.scatterplot(data=df, x=col_x, y=col_y, ax=ax)
    else:
        sns.scatterplot(data=df, x=col_x, y=col_y, hue=hue_col, ax=ax)
    st.pyplot(fig)