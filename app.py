import streamlit as st
import pandas as pd
import plotly.express as px

# Encabezado de la aplicación
st.header("Análisis de anuncios de vehículos")

# Cargar el conjunto de datos
car_data = pd.read_csv("data/vehicles_us.csv")

# Botón para histograma
hist_button = st.button("Construir histograma de kilometros")

if hist_button:
    st.write("Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True, key="hist_button")

# Botón para gráfico de dispersión 
scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Creación de un gráfico de dispersión entre el año del modelo y el precio")
    fig = px.scatter(car_data, x="model_year", y="price")
    st.plotly_chart(fig, use_container_width=True, key="scatter_button")

# Casilla para histograma
build_histogram = st.checkbox("Construir un histograma de precios")

if build_histogram:
    st.write("Creación de un histograma para los precios")
    fig = px.histogram(car_data, x="price")
    st.plotly_chart(fig, use_container_width=True, key="hist_checkbox")

# Casilla para histograma de días listados
build_days = st.checkbox("Distribución de días listados")

if build_days:
    st.write("¿Cuánto tiempo permanecen los anuncios publicados?")
    fig = px.histogram(car_data, x="days_listed")
    st.plotly_chart(fig, use_container_width=True, key="days_listed")

# Casilla para gráfico de dispersión
build_scatter = st.checkbox("Construir gráfico de dispersión")

if build_scatter:
    st.write("Creación de un gráfico de dispersión entre la condición del auto y el precio")
    fig = px.scatter(car_data, x="condition", y="price")
    st.plotly_chart(fig, use_container_width=True, key="scatter_checkbox")

