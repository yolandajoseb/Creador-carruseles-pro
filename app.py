import streamlit as st
import google.generativeai as genai

# Configuración Visual de Marca
st.set_page_config(page_title="Generador de Carruseles Elite", layout="wide")

# Estética con tus colores (#8B6F47, #D4A574)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com');
    .stApp { background-color: #FAF8F5; }
    h1 { font-family: 'Playfair Display', serif; color: #8B6F47; text-align: center; }
    p, label, .stSelectbox { font-family: 'Lato', sans-serif; color: #8B6F47; }
    .stButton>button {
        background-color: #D4A574;
        color: white;
        border-radius: 30px;
        width: 100%;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Título de la App
st.title("✨ Creador de Carruseles Mágico")

# Conectar con tu API Key secreta (Invisible para el usuario)
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("Error de configuración: Asegúrate de añadir tu GOOGLE_API_KEY en los Secrets de Streamlit.")

# Interfaz del usuario
col1, col2 = st.columns(2)
with col1:
    idea = st.text_area("¿Cuál es la idea base?", placeholder="Ej: Por qué tus cursos no funcionan")
    red_social = st.selectbox("Red Social", ["Instagram", "LinkedIn", "Facebook", "TikTok"])
with col2:
    angulo = st.selectbox("Ángulo", ["Disruptivo", "Dolor", "Solución", "Marketing", "Testimonio"])
    num_slides = st.slider("Número de Slides", 7, 10, 8)

if st.button("Generar mi Carrusel Profesional"):
    if idea:
        with st.spinner('Creando contenido estratégico...'):
            try:
                # Usamos el modelo más moderno y rápido de 2026
                model = genai.GenerativeModel('gemini-1.5-flash-latest')
                prompt = f"Crea un carrusel de {num_slides} slides para {red_social} con ángulo {angulo}. Idea: {idea}. Incluye sugerencias de fotos de Unsplash por cada slide."
                response = model.generate_content(prompt)
                st.success("¡Listo! Aquí tienes tu contenido:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error al generar: {e}")
    else:
        st.warning("Escribe una idea primero.")
