import streamlit as st

# Fundo preto + texto branco
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
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Empresas Parceiras")

col1, col2, col3 = st.columns(3)

with col1:
    # Usando link direto de imagem
    st.image("https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg", use_container_width=True)
    st.title("Apple")
    st.link_button("Acessar", "https://www.apple.com/br/")
    st.write("Empresa responsável por uma das maiores produções de eletrônicos do mundo")

with col2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg", use_container_width=True)
    st.title("Netflix")
    st.link_button("Acessar", "https://www.netflix.com/br/")
    st.write("Plataforma de filmes, séries e streaming online.")

with col3:
    st.image("https://upload.wikimedia.org/wikipedia/commons/d/de/SpaceX-Logo.svg", use_container_width=True)
    st.title("SpaceX")
    st.link_button("Acessar", "https://www.spacex.com/")
    st.write("Empresa espacial que desenvolve foguetes e missões espaciais.")                                                                  
