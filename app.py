import streamlit as st
from fruit_manager import *

st.set_page_config(page_title="Dashboard de la plantation", layout="wide")

st.title("Dashboard de la plantation")

inventaire = ouvrir_inventaire()
prix = ouvrir_prix()
tresorerie = ouvrir_tresorerie()

st.header("Tresorerie")
st.metric(label="montant disponible", value=f"{tresorerie:.2f} $")

st.header("Inventaire")
st.table(inventaire)


# ---sidebar---#
with st.sidebar:
    st.title("Actions")
    action = st.selectbox(
        "Choisir une action", options=["Récolter", "Vendre"], key="action_choisie"
    )
    fruit = st.selectbox(
        "Choisir un fruit", options=inventaire.keys(), key="fruit_choisi"
    )
    quantite = st.number_input("Quantité", min_value=1, step=1, key="quantite_choisie")
    if st.button("Valider"):
        if action == "Récolter":
            recolter(inventaire, fruit, quantite)
        elif action == "Vendre":
            inventaire, tresorerie = vendre(
                inventaire, fruit, quantite, tresorerie, prix
            )
        ecrire_inventaire(inventaire)
        ecrire_tresorerie(tresorerie)
        st.rerun()
