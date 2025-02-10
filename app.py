import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# st.write("Hello World")

st.title("Instagram Analytcs")
# st.header("Muito massa")
# st.text("Corpo do texto")
# st.markdown("Clique aqui")

uploaded_file = st.file_uploader('Dados')

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.write(df.describe())
    st.header('Analytcs')
    st.write(df.head())

    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Reach'], y=df['Likes'])
    ax.set_xlabel('Alcance')
    ax.set_ylabel('Curtidas')
    
    st.pyplot(fig) # Figura, é o que manda