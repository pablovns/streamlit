import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import geobr


st.title('Apresentação de dados') #Título para a página
st.caption('Análise realizada')
st.write('Utilizando este sistema, é possível visualizar os resultados da análise realizada, de maneira interativa')
st.latex('2^5=/frac{2^6}{2}')

filme = st.text_input('Digite o nome de um filme')
st.write('Filme:', filme)

valor = st.text_input('Digite um valor')
st.write(f'Valor ao quadrado: {int(valor)**2}')

data = st.date_input('Escolha a data')
st.write(data)

horario = st.time_input('Escolha o horário')
st.write(horario)

cor = st.color_picker('Escolha uma cor')
st.write(cor)

tipo = st.radio('Qual seu estilo de filme favorito?', ['Drama', 'Comédia','Suspense', 'Documentário'] )
st.write('Tipo escolhido:', tipo)

filmes = st.multiselect('Qual destes filmes você recomendaria?', ['Matrix', 'Kill Bill', 'TeneT'])
st.write('Eu recomendaria:', filmes)

qtde = st.slider('Quantos filmes você assistiu no último ano?', 0, 20, 5)
st.write(qtde)

qtde_ideal = st.slider('Escolha os valores inicial e final', 0, 20, [8,12])
st.write('A quantidade ideal',qtde_ideal)

st.metric(label='Temperatura', value='22 °C', delta='4 °C')

# ------------------ DataFrames ------------------
df_ex = pd.DataFrame(np.random.randn(15, 4),columns=['a', 'b', 'c', 'd'])
st.dataframe(df_ex)
st.table(df_ex)


st.image('https://p0.piqsels.com/preview/1013/231/679/adorable-animal-animal-photography-breed.jpg')

st.line_chart(df_ex)

st.bar_chart(df_ex)
fig, ax = plt.subplots()           #Cria figura e a referência
ax.scatter(df_ex['a'], df_ex['b']) #Gera o gráfico utilizando a referência
ax.plot([0,2,5], [0,1,2], c='r')
st.pyplot(fig)

gdf_estados = geobr.read_state() #Obtém mapa

fig, ax = plt.subplots() #Cria figura e referência
gdf_estados.plot(ax=ax)  #Gera o mapa utilizando a referência
st.pyplot(fig)           #Apresenta o mapa