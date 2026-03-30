import streamlit as st
import google.generativeai as genai

# Configuración de Marca y Estética
st.set_page_config(page_title="Generador de Carruseles Elite", layout="wide")

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com');
    
    .stApp {{ background-color: #FAF8F5; }}
    h1 {{ font-family: 'Playfair Display', serif; color: #8B6F47; text-align: center; }}
    p, label, .stSelectbox {{ font-family: 'Lato', sans-serif; color: #8B6F47; }}
    
    .stButton>button {{
        background-color: #D4A574;
        color: white;
        border-radius: 30px;
        border: none;
        padding: 10px 30px;
        font-family: 'Lato', sans-serif;
        font-weight: bold;
    }}
    .slide-card {{
        background-color: #F5E8E1;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #E6AABC;
        margin-bottom: 20px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }}
    </style>
    """, unsafe_allow_html=True)

# Lógica de la App
st.title("✨ Creador de Carruseles Pro")
st.subheader("Transforma ideas simples en contenido de alto nivel")

col1, col2 = st.columns(2)

with col1:
    idea = st.text_area("¿Cuál es la idea base de tu carrusel?", placeholder="Ej: 5 consejos para organizar tu oficina")
    red_social = st.selectbox("Red Social", ["Instagram", "Facebook", "LinkedIn", "TikTok Series", "Pinterest"])
    angulo = st.selectbox("Ángulo de Contenido", ["Disruptivo", "Dolor del cliente", "Solución al problema", "Mensaje de Marketing", "Testimonio"])

with col2:
    audiencia = st.text_input("¿A quién va dirigido?", placeholder="Ej: Mujeres emprendedoras")
    num_slides = st.slider("Número de Slides", 7, 10, 8)
    api_key = st.text_input("Introduce tu API Key de Google (Solo para pruebas)", type="password")

if st.button("Generar Carrusel Mágico"):
    if not api_key or not idea:
        st.error("Por favor, introduce tu API Key e idea.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')
            
            prompt = f"""
            Actúa como estratega de contenido. Crea un carrusel de {num_slides} slides para {red_social}.
            Idea: {idea}. Ángulo: {angulo}. Audiencia: {audiencia}.
            Reglas: Slide 1 es el Gancho. Slide final es el CTA.
            Para cada slide entrega: 
            1. Título del Slide
            2. Texto del cuerpo
            3. Sugerencia de búsqueda en Unsplash (en inglés).
            """
            
            response = model.generate_content(prompt)
            st.success("¡Tu carrusel está listo!")
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"Hubo un error: {e}")
