# 🚗 Sprint 7 – Análisis de anuncios de vehículos

Este proyecto desarrolla una aplicación web interactiva utilizando **Streamlit** para analizar el conjunto de datos `vehicles_us.csv`, el cual contiene información sobre anuncios de vehículos publicados en Estados Unidos.

---

## 🌐 Aplicación desplegada en Render

Puedes acceder a la aplicación web aquí:

👉 https://sprint-7-huxf.onrender.com

---

## 🔍 Análisis Exploratorio de Datos (EDA)

Realicé un EDA en Jupyter Notebook (archivo `notebooks/EDA.ipynb`) utilizando **pandas** y **plotly**, donde generé visualizaciones como:

- Histograma del odómetro  
- Gráfico de dispersión entre odómetro y precio  

Esto permitió identificar tendencias iniciales y el comportamiento de las variables principales.

---

## 💻 Desarrollo de la App Web

La aplicación construida en Streamlit (`app.py`) permite:

- Visualizar el histograma del odómetro  
- Visualizar el gráfico de dispersión (odometer vs price)  
- Interactuar con los gráficos mediante botones  
- Renderizar visualizaciones dinámicas usando Plotly  

---

## 📁 Organización del proyecto

El repositorio incluye:

- `app.py`  
- `vehicles_us.csv`  
- `requirements.txt`  
- `notebooks/EDA.ipynb`  
- Entorno virtual (`vehicles_env/`)  
- Archivo `.gitignore`  

---

## ▶️ Ejecución

Para correr la aplicación se deben instalar los paquetes del archivo `requirements.txt` y ejecutar:

```bash
streamlit run app.py

```


### ✔️ Resultado final

El proyecto es completamente funcional, sigue la estructura solicitada y permite explorar de forma visual y dinámica los anuncios de vehículos. Se cumplen todos los requisitos del Sprint 7.

