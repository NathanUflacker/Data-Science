import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

# Configuração da página
st.set_page_config(
    page_title="Experiência",
    page_icon="💼",
    layout="wide"
)
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


# Formação e Experiência Profissional
st.title("Formação e Experiência Profissional")

st.header("⭐ - Engenharia de Software")
st.subheader("Faculdade de Informática e Administração Paulista")
st.write("_Duração da Formação_ \n \n  `Início`: 07/2023 \n \n `Previsão de Conclusão`: 07/2027")

st.divider()

# Licenças e Certificados

st.title("Licenças e Certificados")


st.header("🛠️- Estrutura de Computadores")
st.subheader("Faculdade de Informática e Administração Paulista")
st.write("Estudo sobre como os vários componentes do computador interagem entre sí para realizar tarefas computacionais")
st.write("`Emissão:` 02/2025")

st.write("#")
st.header("🛠️- Gestão e Infraestrutura de TI")
st.subheader("Faculdade de Informática e Administração Paulista")
st.write("conjunto de processos e atividades que envolvem o planejamento, operação e manutenção de recursos e ativos de uma organizaçã")
st.write("`Emissão:` 05/2024")

st.write("#")
st.header("🌍- Formação Social e Sustentabilidade")
st.subheader("Faculdade de Informática e Administração Paulista")
st.write("Como a tecnologia interage com a natureza e como podem trabalhar juntos para evitar uma catástrofe global usando a criatividade e soluções verdes.")
st.write("`Emissão:` 03/2024")

st.write("#")
st.header("🏗️- Design Thinking Process")
st.subheader("Faculdade de Informática e Administração Paulista")
st.write("é uma metodologia que usa técnicas de design para criar soluções inovadoras. O processo é colaborativo e envolve várias etapas, como empatia, definição, ideação, prototipação e teste.")
st.write("`Emissão:` 10/2023")

st.write("#")
st.header("🧠- Imersão Inteligência Artifial 2ª Edição")
st.subheader("Alura")
st.write("Entendendo como funciona a inteligência artificial, engenharia de prompt e como utilizá-la como ferramenta para o dia-a-dia")
st.write("`Emissão:` 05/2024")
