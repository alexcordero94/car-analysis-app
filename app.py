
import pandas as pd
import plotly.express as px
import streamlit as st


car_data = pd.read_csv('vehicles_us (4).csv')  

st.header('Análisis de vehículos')


hist_button = st.button('Construir histograma')

if hist_button: 
   
    st.write('Creando un histograma para la columna odómetro de los vehículos')


    fig = px.histogram(car_data, x="odometer")  
    
    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button: 

    st.write('Creando un gráfico de dispersión entre las columnas "odometer" y "price"')

  
    fig = px.scatter(car_data, x="odometer", y="price", title="Relación entre odómetro y precio")

  
    st.plotly_chart(fig, use_container_width=True)
