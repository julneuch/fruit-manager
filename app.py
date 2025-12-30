import streamlit as st
from fruit_manager import *

st.title("Dashboard de la plantation")

inventaire = ouvrir_inventaire()
prix = ouvrir_prix()
tresorerie = ouvrir_tresorerie()

st.header("Tresorerie")
st.metric(label="montant disponible", value=f"{tresorerie:.2f} $")

st.header("Inventaire")
st.table(inventaire)
