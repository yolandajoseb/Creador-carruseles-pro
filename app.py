import streamlit as st
import google.generativeai as genai

# Configuración Visual
st.set_page_config(page_title="Generador de Carruseles", layout="wide")

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
    }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ Creador de Carruseles Mágico")

# Intentar conectar con la API
try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("Falta la configuración 'GOOGLE_API_KEY' en los Secrets de Streamlit.")
except Exception as e:
    st.error(f"Error al conectar con la IA: {e}")

# Interfaz
col1, col2 = st.columns(2)
with col1:
    idea = st.text_area("¿Cuál es la idea base?", placeholder="Ej: Consejos de marketing")
    red_social = st.selectbox("Red Social", ["Instagram", "LinkedIn", "Facebook", "TikTok"])
with col2:
    angulo = st.selectbox("Ángulo", ["Disruptivo", "Dolor", "Solución", "Marketing", "Testimonio"])
    num_slides = st.slider("Número de Slides", 7, 10, 8)

if st.button("Generar mi Carrusel"):
    if idea:
        with st.spinner('Creando contenido...'):
            try:
                prompt = f"Genera un carrusel de {num_slides} slides para {red_social} con ángulo {angulo}. Idea: {idea}. Incluye textos por slide y sugerencia de imagen."
                response = model.generate_content(prompt)
                st.success("¡Listo!")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error al generar: {e}")
    else:
        st.warning("Escribe una idea primero.")
