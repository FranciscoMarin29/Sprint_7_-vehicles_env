import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Título / encabezado
st.header("🚗 Análisis de anuncios de vehículos – Sprint 7")

st.write("""
Esta aplicación web permite explorar el conjunto de datos de anuncios de coches
(vehicles_us.csv) y visualizar algunas relaciones importantes, como:

- Distribución del odómetro
- Relación entre kilometraje (odometer) y precio
""")

# Cargar el CSV
@st.cache_data
def load_data():
    # El CSV debe estar en la raíz del proyecto
    return pd.read_csv("vehicles_us.csv")

try:
    car_data = load_data()
    st.success("Datos cargados correctamente.")
except FileNotFoundError:
    st.error("No se encontró el archivo 'vehicles_us.csv' en el directorio del proyecto.")
    st.stop()

# Botón para histograma
if st.button("Mostrar histograma del odómetro"):
    fig_hist = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig_hist.update_layout(
        title_text='Distribución del Odómetro',
        xaxis_title='Odómetro',
        yaxis_title='Frecuencia'
    )
    st.write("### Histograma del odómetro")
    st.plotly_chart(fig_hist)

# Botón para scatter
if st.button("Mostrar scatter Odómetro vs Precio"):
    fig_scatter = go.Figure(
        data=[go.Scatter(
            x=car_data['odometer'],
            y=car_data['price'],
            mode='markers'
        )]
    )
    fig_scatter.update_layout(
        title_text='Relación entre Odómetro y Precio',
        xaxis_title='Odómetro',
        yaxis_title='Precio'
    )
    st.write("### Gráfico de dispersión Odómetro vs Precio")
    st.plotly_chart(fig_scatter)

