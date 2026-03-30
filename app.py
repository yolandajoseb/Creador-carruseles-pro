import streamlit as st
import google.generativeai as genai

# 1. Configuración de Marca y Estética
st.set_page_config(page_title="Generador de Carruseles Elite", layout="wide")

st.markdown("""
    <style>
    @import url('https://googleapis.com');
    .stApp { background-color: #FAF8F5; }
    h1 { font-family: 'Playfair Display', serif; color: #8B6F47; text-align: center; }
    p, label, .stSelectbox { font-family: 'Lato', sans-serif; color: #8B6F47; }
    .stButton>button {
        background-color: #D4A574;
        color: white;
        border-radius: 30px;
        width: 100%;
        font-weight: bold;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Título
st.title("✨ Creador de Carruseles Mágico")

# 3. Conexión Segura con la IA
model = None
if "GOOGLE_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"], transport='rest')
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"Error al configurar la IA: {e}")
else:
    st.warning("⚠️ Configura la 'GOOGLE_API_KEY' en los Secrets de Streamlit.")

# 4. Interfaz de Usuario
col1, col2 = st.columns(2)
with col1:
    idea = st.text_area("¿Cuál es la idea base?", placeholder="Ej: 5 tips para vender más")
    red_social = st.selectbox("Red Social", ["Instagram", "LinkedIn", "Facebook", "TikTok"])
with col2:
    angulo = st.selectbox("Ángulo", ["Disruptivo", "Dolor", "Solución", "Marketing", "Testimonio"])
    num_slides = st.slider("Número de Slides", 7, 10, 8)

# 5. Botón de Generar
if st.button("Generar mi Carrusel Profesional"):
    if not idea:
        st.warning("Escribe una idea primero.")
    elif model is None:
        st.error("La IA no está lista. Revisa tus Secrets.")
    else:
        with st.spinner('Creando contenido estratégico...'):
            try:
                prompt = f"Genera un carrusel de {num_slides} slides para {red_social} con ángulo {angulo}. Idea: {idea}. Para cada slide da: Título, Cuerpo de texto y búsqueda en Unsplash."
                response = model.generate_content(prompt)
                st.success("¡Tu carrusel está listo!")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error al generar contenido: {e}")
