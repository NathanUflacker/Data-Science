import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

# Configuração da página
st.set_page_config(page_title="Digital CV | Nathan Uflacker",layout="wide")
st.sidebar.markdown("Desenvolvido por Nathan Uflacker.")

# Importando o CSS e ensinando o programa a ler o arquivo
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Adicionando logo com streamlit-extras
# add_logo("logo.jpeg")

# Adicionando o logo
st.logo("logo.png")

# Ler nosso curriculo em PDF
@st.cache_data
def get_data():
    df = pd.DataFrame(
        pd.read_csv("Curriculo_linkedin_nathanuflacker.csv")
    )
    return df

@st.cache_data
def convert_for_download(df):
    return df.to_csv().encode("utf-8")

# Informações ao lado da logo

col1, col2, col3 = st.columns(3, gap="small")

with col1:
    st.image("foto_perfil.jpg", width=300)

with col2: 
    st.title("_Nathan Uflacker_")
    st.write("Estudante Engenharia de Software")
    st.caption("_Status_: 4/8 Cursado")
    st.write("📬", "nathanuflacker@hotmail.com")
    st.markdown("Download do meu `Curriculo.csv` logo abaixo: ")


    df = get_data()
    csv = convert_for_download(df)

    st.download_button(
        label="📝| Download CSV",
        data=csv,
        file_name="Curriculo_NathanUflacker.csv",
        mime="Curriculo_linkedin_nathanuflacker/csv")
    



with col3:
    st.title("Mídias Sociais:")


    emoji_linkedin = st.markdown("""<a href="https://www.linkedin.com/in/nathanuflacker/"><img src="https://cdn3.emoji.gg/emojis/70322-linkedin.png" width="64px" height="64px" alt="LinkedIn"></a>""", unsafe_allow_html=True)
    emoji_github = st.markdown("""<a href="https://github.com/NathanUflacker?tab=repositories"><img src="https://cdn3.emoji.gg/emojis/6705-githubblack.png" width="64px" height="64px" alt="githubwhite"></a>""", unsafe_allow_html=True)

##########################################

st.title("CV Digital | _Nathan Uflacker_")
st.divider()

# Adicionando o logo no body
# st.image("foto_perfil.jpg", width=150)


st.header("Sobre mim")
st.write("🙋‍♂️Sou um estudante de Engenharia de Software apaixonado pela tecnologia e todo o seu potencial, comprometido a transformar ideias em soluções inovadoras.")
st.write("📚 Atualmente estou cursando o 3º Semestre do curso de Engenharia de Software pela Faculdade de Informática e Administração Paulista (FIAP).")

st.write("📚 A curiosidade e a vontade de aprender me guiam de forma que desenvolvi competências em áreas como Design Thinking, Tecnologia Sustentável e Gestão de Infraestrutura de TI")

st.write("💬 Estou sempre animado com a perspectiva de novas oportunidades de aprendizado e com a energia necessária para ir atrás de novos conhecimentos e fazer a diferença.")