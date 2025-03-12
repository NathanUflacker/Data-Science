import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson, binom, bernoulli

# Configuração do título do aplicativo
st.title("Análise de Crimes e Imigrantes Presos em Portugal")
# Carregar os dados (substituir pelo caminho correto do arquivo)

file_path = "analise_portugal.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

st.markdown("Devido ao aumento de `505%` nas denúncias de [xenofobia contra brasileiros em Portugal](https://www.estadao.com.br/brasil/video-brasileira-xenofobia-portugal-nao-e-portuguesa-nao-deve-ca-estar-nprm/), evidenciou-se um aumento tanto da violência, quanto do discurso xenofóbico no país. Portanto, apresento-lhes este breve estudo matemático com o intuito de enfraquecer e erradicar o discurso contra imigrantes no país.")
st.table(df)

# Gráfico de Correlação entre Ano e Quantidade de Crimes
st.subheader("Correlação entre Ano e Quantidade de Crimes")
fig2, ax2 = plt.subplots()
ax2.plot(df["Ano"], df["Qntd_crimes"], color='red', marker='s', linestyle='-')
ax2.set_xlabel('Ano')
ax2.set_ylabel('Quantidade de Crimes')
ax2.set_title('Evolução da Quantidade de Crimes ao Longo dos Anos')
ax2.grid(True)
st.pyplot(fig2)

st.markdown("A partir do gráfico mostrando a correlação entre A progressão dos Anos e a Quantidade de crimes, podemos inferir que houve uma pequena oscilação na quantidade desde 2015 até 2019, sem ultrapassar a marca de 120 mil crimes reportados. Contudo, houve um boom de crimes reportados às autoridades em 2020, devido à pandemia do Covid-19, segundo a CNN portugal como se segue em [CNN](https://cnnportugal.iol.pt/crime-em-lisboa/crime-no-porto/hoje-esta-provado-que-ha-mais-crime-disse-moedas-mas-os-factos-mostram-que-em-lisboa-regressou-aos-niveis-da-pre-pandemia/20240807/66b24db5d34e94b82903e850).")

# Definir os eixos do gráfico
x5 = df["Ano"]
y5 = df["Residentes_estrangeiros"]


st.subheader("Aumento da imigração ao longo dos anos")
fig5, ax = plt.subplots()
ax.plot(x5, y5, color='purple', marker='o', linestyle='-')
ax.set_xlabel('Ano')
ax.set_ylabel('Residentes Estrangeiros')
ax.set_title('Aumento de estrangeiros ao longo do tempo')
ax.grid(True)
st.pyplot(fig5)

st.markdown("Como podemos observar, ao longo dos anos houve uma forte onda migratória para Portugal enquanto, coincidentemente, os casos de criminalidades não paravam de subir. Porém, NÃO SE ENGANE, esse foi um discurso bastante utilizado para servir de suporte à discursos xenofóbicos. A imigração pode sim ter aumentado ao mesmo tempo que a criminalidade, mas não é por isso que as duas mantém uma correlação entre si, é preciso analisar os dados!!!!")

# Definir os eixos do gráfico
x = df["Qntd_crimes"]
y = df["Imigrantes_presos"]


st.subheader("Correlação entre a Quantidade de Crimes e Imigrantes Presos")
fig, ax = plt.subplots()
ax.plot(x, y, color='blue', marker='o', linestyle='-')
ax.set_xlabel('Quantidade de Crimes')
ax.set_ylabel('Imigrantes Presos')
ax.set_title('Correlação entre Crimes e Imigrantes Presos em Portugal')
ax.grid(True)

# Mostrar o gráfico no Streamlit
st.pyplot(fig)

st.markdown("Os imigrantes compuseram uma parte do contingente de detidos em portugal, porém, ao longo do tempo, com o aumento da criminalidade, o número de imigrantes presos diminuiu. Isto é, o número de imigrantes presos e a quantidade de crimes mantém uma relação inversamente proporcional.")
st.markdown("`Quanto maior o número de crimes sendo cometidos, menor o número de imigrantes preso.`")
st.markdown("Então, se quanto mais crimes, menos imigrantes presos, podemos inferir que os imigrantes não estão associados à tais crimes, então quem está????")



# Gráfico de Correlação entre Portugueses Presos e Quantidade de Crimes
st.subheader("Correlação entre Portugueses Presos e Quantidade de Crimes")
fig3, ax3 = plt.subplots()
ax3.plot(df["Qntd_crimes"], df["Portugueses_presos"], color='green', marker='^', linestyle='-')
ax3.set_xlabel('Quantidade de Crimes')
ax3.set_ylabel('Portugueses Presos')
ax3.set_title('Correlação entre Portugueses Presos e Quantidade de Crimes')
ax3.grid(True)
st.pyplot(fig3)

st.markdown("Segundo o [Relatório Indicadores de Integração de Imigração de 2022](https://www.portugal.gov.pt/download-ficheiros/ficheiro.aspx?v=%3D%3DBQAAAB%2BLCAAAAAAABAAzNDazMAQAhxRa3gUAAAA%3D), `84.7%` dos reclusos nas prisões portuguesas são portugueses, contra `15.3%` de estrangeiros. Isto é, os portuguesas lideraram, em parâmetros de nacionalidade, o número de presos em seu país.")

st.divider()

st.header("Conclusão")
st.markdown("#")
st.write("Embora o discurso xenofóbico tenha ganhado força se baseando em confusões matemáticas, os números comprovam que o aumento do número de estrangeiros migrando para o país não sustenta correlação com o aumento da criminalidade local. Em verdade, o número de imigrantes se mantém inversamente proporcional ao número de quantidade de crimes, desmentindo a falsa ideia de `Quanto mais imigrantes, mais crimes`")

st.divider()

st.header("Distribuição Binomial")
st.image('binomial.png')
st.markdown('Este modelo de distribuição pode ser útil se quisermos entender a ocorrência de crimes em um conjunto finito de possibilidades (por exemplo, se há um limite de crimes possíveis devido à população ou recursos disponíveis para registro).')
st.markdown("No gráfico da distribuição binomial, estamos analisando a probabilidade de ocorrência de diferentes quantidades de crimes dentro de um conjunto finito de tentativas (no caso, considerando o número total de crimes possíveis). Isso nos ajuda a entender: \n \n - A quantidade de crimes que é certeza que irão acontecer. \n \n - Como a variação no número de crimes se distribui ao longo do tempo. \n \n - Se há uma concentração de probabilidades em torno de certos valores, indicando um comportamento padrão no número de crimes. \n \n Essa distribuição é útil, por exemplo, para prever quantos crimes podem ocorrer no futuro com base nos dados de `2015 - 2023`. Podemos observar pelo gráfico que a quantidade de crimes com a maior probabilidade de acontecer é de `80%` para 50 casos de crimes.")

st.write("#")

st.header("Distribuição de Poisson")
st.image('poisson.png')
st.markdown("Na distribuição de poisson nós analisamos quantos crimes ocorrem em, por exemplo, um ano sem limite fixo de tentativas")
st.markdown("O gáfico significa uma previsão do número de crimes, assumindo que o comportamento que provocou esses crimes continue o mesmo, mas o gráfico nos ajuda a entender esse comportamento e prever o número de crimes para auxiliar o serviço de segurança pública a se planejar e prevenir tais crimes.")

# # Distribuição Binomial aplicada aos crimes
# st.subheader("Distribuição Binomial para a Quantidade de Crimes")

# media_crimes = df["Qntd_crimes"].mean()

# n = int(max(df["Qntd_crimes"]))  # Número de tentativas baseado no máximo de crimes
# p = media_crimes / n  # Probabilidade de sucesso 


# x_bin = np.arange(0, n + 1)
# y_bin = binom.pmf(x_bin, n, p)

# # Plotar
# fig6, ax6 = plt.subplots()
# ax6.bar(x_bin, y_bin, color='blue', alpha=0.7)
# ax6.set_xlabel('Quantidade de Crimes')
# ax6.set_ylabel('Probabilidade')
# ax6.set_title('Distribuição Binomial para Crimes')
# ax6.grid(True)
# st.pyplot(fig6)

# # Distribuição de Bernoulli aplicada aos crimes
# st.subheader("Distribuição de Bernoulli para Ocorrência de Crimes")


# p_bernoulli = media_crimes / max(df["Qntd_crimes"])  # Probabilidade de ocorrência
# x_bernoulli = [0, 1]
# y_bernoulli = bernoulli.pmf(x_bernoulli, p_bernoulli)


# st.subheader("Distribuição de Bernoulli para Ocorrência de Crimes")


# p_bernoulli = media_crimes / df["Qntd_crimes"].max()  # Probabilidade de ocorrência
# x_bernoulli = [0, 1]
# y_bernoulli = bernoulli.pmf(x_bernoulli, p_bernoulli)

# # Plotar a distribuição de Bernoulli
# fig7, ax7 = plt.subplots()
# ax7.bar(x_bernoulli, y_bernoulli, color='red', alpha=0.7)
# ax7.set_xticks([0, 1])
# ax7.set_xticklabels(['Nenhum Crime', 'Crime Ocorreu'])
# ax7.set_ylabel('Probabilidade')
# ax7.set_title('Distribuição de Bernoulli para Ocorrência de Crimes')
# ax7.grid(True)
# st.pyplot(fig7)


