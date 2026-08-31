Claro! Aqui está o código completo em uma única parte, já com as imagens menores:

import streamlit as st

# Fundo branco + texto preto
st.markdown("""
    <style>
    .stApp {
        background-color: white;
        color: black;
    }

    /* Botões */
    .stLinkButton a {
        background-color: #262730;
        color: white !important;
        text-decoration: none;
    }

    .stLinkButton a:hover {
        background-color: #ff4b4b;
        color: white !important;
    }

    h1, h2, h3, p, div {
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.title("Empresas Parceiras")

# Criando 3 colunas
col1, col2, col3 = st.columns(3)

# Apple
with col1:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg",
        width=100
    )
    st.title("Apple")
    st.link_button("Acessar", "https://www.apple.com/br/")
    st.write(
        "Empresa responsável por uma das maiores produções de eletrônicos do mundo."
    )

# Netflix
with col2:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg",
        width=150
    )
    st.title("Netflix")
    st.link_button("Acessar", "https://www.netflix.com/br/")
    st.write(
        "Plataforma de filmes, séries e streaming online."
    )

# SpaceX
with col3:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/d/de/SpaceX-Logo.svg",
        width=150
    )
    st.title("SpaceX")
    st.link_button("Acessar", "https://www.spacex.com/")
    st.write(
        "Empresa espacial que desenvolve foguetes e missões espaciais."
    )

