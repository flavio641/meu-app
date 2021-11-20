import streamlit as st
import pandas as pd
import matplotlib_inline

st.image('bannerflai.jpg')
st.sidebar.image('bannerflai.jpg')
df = pd.read_csv('prof-dados-resumido.csv')




paginas= ['Home','Rascunhos', 'Gráficos']


pagina = st.sidebar.selectbox('Selecione a Pagina que você deseja', paginas)

if pagina == 'Home':

    st.write(df)
    st.table(df.describe())


if pagina == 'Gráficos':
    variaveis = df.columns.tolist()
    var1 = st.sidebar.selectbox('Selecione o Campo desejado', variaveis)

    plot = df['Salário'].groupby(df[var1]).mean().plot(kind='barh')
    st.pyplot(plot.figure)
    var = st.sidebar.selectbox('Média De Salário ', ['Idade', 'Profissão', 'Escolaridade'])
    ms = df['Salário'].groupby(df[var]).mean()
    st.write(ms)












var = st.color_picker





