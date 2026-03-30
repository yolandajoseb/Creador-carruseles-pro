import streamlit as st
import google.generativeai as genai

# 1. Estética de Marca (Tus colores y fuentes)
st.set_page_config(page_title="Generador Elite", layout="wide")
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    .stApp { background-color: #F5E8E1; }
    h1 { font-family: 'Playfair Display', serif; color: #8B6F47; text-align: center; }
    p, label, .stSelectbox { font-family: 'Lato', sans-serif; color: #8B6F47; }
    .stButton>button {
        background-color: #D4A574;
        color: white;
        border-radius: 30px;
        width: 100%;
        font-weight: bold;
        border: none;
        padding: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ Creador de Carruseles Mágico")

# 2. Conexión Estable con la IA
if "GOOGLE_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        # Esta es la línea que corrige el error 404:
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"Error de conexión: {e}")
else:
    st.warning("⚠️ Configura la API Key en los Secrets de Streamlit.")

# 3. Interfaz
col1, col2 = st.columns(2)
with col1:
    idea = st.text_area("¿Cuál es la idea base?", placeholder="Ej: 5 consejos para vender en eBay")
    red_social = st.selectbox("Red Social", ["Instagram", "LinkedIn", "Facebook", "TikTok"])
with col2:
    angulo = st.selectbox("Ángulo", ["Disruptivo", "Dolor", "Solución", "Marketing", "Testimonio"])
    num_slides = st.slider("Número de Slides", 7, 10, 8)

if st.button("Generar mi Carrusel Profesional"):
    if idea and "GOOGLE_API_KEY" in st.secrets:
        with st.spinner('Escribiendo contenido de alto nivel...'):
            try:
                prompt = f"Genera un carrusel de {num_slides} slides para {red_social} con ángulo {angulo}. Idea: {idea}. Dame el texto por cada slide y una sugerencia de foto de Unsplash."
                response = model.generate_content(prompt)
                st.success("¡Tu contenido está listo!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error al generar: {e}")
    else:
        st.warning("Asegúrate de escribir una idea.")
