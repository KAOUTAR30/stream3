import streamlit as st
import pandas as pd
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
donnee_compte_utilisateur = pd.read_csv("utilisateurs.csv", sep=';')
donnee_compte_utilisateur = {
    'usernames': {
        row ['name']:{
            'name' : row['name'],
            'password': row['password'],
            'email': row['email'],
            'role': row['role'],
        }
        for index, row in donnee_compte_utilisateur.iterrows()}}
authenticator = Authenticate(
    donnee_compte_utilisateur, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire
)
authenticator.login()
if st.session_state["authentication_status"]:
    with st.sidebar:
         # Le bouton de déconnexion
        authenticator.logout("Déconnexion")
        selection = option_menu(
            st.write(f"Bienvenu {st.session_state['name']}"),
            options = ["Accueil", "Les photos de ses animaux"]
        )
    if selection == "Accueil":
        st.title("Bienvenue sur la page de IAN")
        st.image("https://www.mytalk1071.com/wp-content/uploads/2024/10/CMG9adc8a8d-6917-4e51-97f3-fed88aa125cf.jpg")
    if selection == "Les photos de ses animaux":
        st.title("Bienvenue dans l'album de ses animaux")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://static.streamlit.io/examples/cat.jpg")
        with col2:
            st.image("https://static.streamlit.io/examples/dog.jpg")
        with col3:
            st.image("https://static.streamlit.io/examples/owl.jpg")
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')

