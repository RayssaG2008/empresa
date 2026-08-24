import streamlit as st

# ============================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================

st.set_page_config(
    page_title="Empresas Parceiras",
    layout="wide"
)


# ============================================
# FUNDO PRETO + TEXTO BRANCO
# ============================================

st.markdown("""
<style>

.stApp {
    background-color: black;
    color: white;
}

/* Títulos */
h1, h2, h3, p {
    color: white !important;
}

/* Botões */
.stLinkButton a {
    background-color: #262730;
    color: white !important;
    text-decoration: none;
    border-radius: 8px;
}

.stLinkButton a:hover {
    background-color: #ff4b4b;
    color: white !important;
}

/* Centraliza o conteúdo das colunas */
[data-testid="column"] {
    text-align: center;
}

/* Tamanho das imagens */
.logo {
    height: 120px;
    width: 100%;
    object-fit: contain;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)


# ============================================
# TÍTULO
# ============================================

st.title("Empresas Parceiras")


# ============================================
# 3 COLUNAS - TODAS NA MESMA LINHA
# ============================================

col1, col2, col3 = st.columns(3)


# ============================================
# APPLE
# ============================================

with col1:

    st.markdown("""
        <img
            class="apple.jpg"
            src="https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg"
            style="filter: invert(1);"
        >
    """, unsafe_allow_html=True)

    st.subheader("Apple")

    st.link_button(
        "Acessar",
        "https://www.apple.com/br/"
    )

    st.write(
        "Empresa responsável por uma das maiores "
        "produções de eletrônicos do mundo."
    )


# ============================================
# NETFLIX
# ============================================

with col2:

    st.markdown("""
        <img
            class="netflix(1).pjg"
            src="https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg"
        >
    """, unsafe_allow_html=True)

    st.subheader("Netflix")

    st.link_button(
        "Acessar",
        "https://www.netflix.com/br/"
    )

    st.write(
        "Plataforma de filmes, séries e "
        "streaming online."
    )


# ============================================
# SPACEX
# ============================================

with col3:

    st.markdown("""
        <img
            class="spacex.jpg"
            src="https://upload.wikimedia.org/wikipedia/commons/d/de/SpaceX-Logo.svg"
        >
    """, unsafe_allow_html=True)

    st.subheader("SpaceX")

    st.link_button(
        "Acessar",
        "https://www.spacex.com/"
    )

    st.write(
        "Empresa espacial que desenvolve "
        "foguetes e missões espaciais."
    )
