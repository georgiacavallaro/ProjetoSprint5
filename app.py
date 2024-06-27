import pandas as pd
import plotly.express as px
import streamlit as st

# Carregando os dados
vehicles = pd.read_csv("vehicles.csv")
colors_per_year = pd.read_csv("colors_per_year.csv")

# Definindo a paleta de cores personalizada
color_palette = {
    "black": "#000000",
    "white": "#FFFFFF",
    "silver": "#C0C0C0",
    "purple": "#800080",
    "red": "#FF0000",
    "orange": "#FFA500",
    "blue": "#0000FF",
    "unknown": "#BDB76B",
    "custom": "#EE82EE",
    "yellow": "#FFFF00",
    "green": "#008000",
    "brown": "#A52A2A",
    "grey": "#808080",
}

st.header("Dashboard de veículos")

# Botão do histograma
hist_button = st.button("Criar histograma")

if hist_button:
    st.write("Criando um histograma para o conjunto de dados")
    fig = px.histogram(vehicles, x="price", range_x=[0, 34600], nbins=500)
    st.plotly_chart(fig, use_container_width=True)

# Checkbox do gráfico de dispersão
build_scatter = st.checkbox("Criar um gráfico de dispersão")

if build_scatter:
    st.write("Criando um gráfico de dispersão para o conjunto de dados")
    fig = px.scatter(
        colors_per_year,
        x="model_year",
        y="count",
        color="paint_color",
        size="percentage",
        hover_data=["model_year"],
        color_discrete_map=color_palette,
    )
    st.plotly_chart(fig, use_container_width=True)
