import streamlit as st
import os
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Carruseles Concreta", layout="centered")

st.title("Generador de Carruseles")

tema = st.text_input("Tema del carrusel")

red = st.selectbox("Red social", ["Instagram", "LinkedIn"])

angulo = st.selectbox("Ángulo", [
    "Tema disruptivo",
    "Dolor del cliente",
    "Solución al problema",
    "Mensaje de marketing",
    "Testimonio"
])

num_slides = st.slider("Número de diapositivas", 7, 10, 8)

def generar_prompt():
    return f"""
Actúa como estratega de contenido especializado en carruseles.

Tema: {tema}
Red: {red}
Ángulo: {angulo}
Número de diapositivas: {num_slides}

REGLAS:
- Máximo 12 palabras por diapositiva
- Lenguaje claro, emocional y directo
- Sin relleno

FORMATO:

Diapositiva 1:
Texto: ...
Imagen: ...
Busqueda: ...

(continuar...)
"""

if st.button("Generar carrusel"):

    with st.spinner("Creando carrusel..."):
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": generar_prompt()}
            ],
            temperature=0.7
        )

        resultado = response.choices[0].message.content

    st.subheader("Resultado")
    st.text_area("Carrusel generado", resultado, height=400)
