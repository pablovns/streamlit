import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import geobr


st.title("Tópicos Especiais em Informática")
st.caption("Atividade sobre ")

# download dos geodataframes
gdf_municipios = geobr.read_municipality()
gdf_estados = geobr.read_state()

gdf_municipios = gdf_municipios.sort_values(by="name_muni", ascending=True)
municipios = gdf_municipios["name_muni"]

# escolher os municípios
muni_escolhidos = st.multiselect("Escolha os municípios: ", municipios)

# plotar os municípios escolhidos
fig, ax = plt.subplots()

gdf_muni_escolhidos = gdf_municipios[gdf_municipios["name_muni"].isin(muni_escolhidos)]
gdf_muni_escolhidos.plot(ax=ax, color="k", alpha=1)

gdf_estados_escolhidos = gdf_estados[gdf_estados["abbrev_state"].isin(gdf_muni_escolhidos["abbrev_state"])]
gdf_estados_escolhidos.plot(ax=ax, color="g", alpha=0.4)

st.subheader("Mapa dos munícipios e seus estados: ")

# apresentar a figura
st.pyplot(fig)
