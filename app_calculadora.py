import streamlit as st
from calculadora_cuotas import obtener_cuota_mensual_total, \
                                obtener_detalles_cuotas


# Crear la interfaz de usuario
st.title("Calculadora de Cuotas de Préstamo")

monto = st.number_input("Monto del préstamo", min_value=0.0, step=1000.0)
plazo = st.number_input("Plazo en meses", min_value=6, step=6)
aporte_inicial = st.number_input("Aporte inicial", min_value=0.0, step=100.0)
tasa_interes = st.number_input("Tasa de interés anual (%)", value=16, disabled=True)

if st.button("Calcular cuota mensual"):
    cuota_mensual, detalles = obtener_cuota_mensual_total(monto, plazo, aporte_inicial=aporte_inicial)
    st.write(f"La cuota mensual total es: ${cuota_mensual:.2f}")

    #detalles = obtener_detalles_cuotas(monto, plazo, aporte_inicial, tasa_interes)
    
    with st.expander("Detalles de la cuota"):
        for key, value in detalles.items():
            st.write(f"{key}: ${value:.2f}")