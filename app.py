import streamlit as st
import google.generativeai as genai
import urllib.parse

# 1. Configuración Estética (Tus colores #8B6F47, #D4A574)
st.set_page_config(page_title="Generador de Carruseles Elite", layout="wide")

st.markdown("""
    <style>
    @import url('https://googleapis.com');
    .stApp { background-color: #FAF8F5; }
    h1 { font-family: 'Playfair Display', serif; color: #8B6F47; text-align: center; margin-bottom: 30px; }
    .slide-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #D4A574;
        margin-bottom: 20px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }
    .stButton>button {
        background-color: #D4A574; color: white; border-radius: 30px; width: 100%; font-weight: bold; border: none; padding: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ Creador de Carruseles Mágico")

# 2. Conexión con la IA (Usando tus Secrets)
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("Error: Asegúrate de tener tu GOOGLE_API_KEY en los Secrets de Streamlit.")

# 3. Interfaz de Usuario
col1, col2 = st.columns(2)
with col1:
    idea = st.text_area("¿Cuál es la idea base de tu contenido?", placeholder="Ej: Cómo prepararme para el contacto cero con la familia")
    red_social = st.selectbox("Red Social", ["Instagram", "LinkedIn", "Facebook", "TikTok Series"])
with col2:
    angulo = st.selectbox("Ángulo de Contenido", ["Disruptivo", "Dolor del cliente", "Solución al problema", "Marketing", "Testimonio"])
    num_slides = st.slider("Número de Slides", 7, 10, 8)

# 4. Generación de Contenido Real
if st.button("¡Generar mi Carrusel Profesional!"):
    if idea:
        with st.spinner('La IA está redactando tus slides estratégicos...'):
            try:
                # Prompt mejorado para obtener texto real por slide
                prompt = f"""
                Actúa como estratega de contenido viral. Crea un carrusel de {num_slides} slides para {red_social}.
                Tema: {idea}. Ángulo: {angulo}. 
                Para cada slide, genera:
                - Título del Slide
                - Texto del cuerpo (máximo 30 palabras, directo y potente)
                - Una palabra clave sencilla en inglés para buscar una imagen.
                
                IMPORTANTE: Separa los slides claramente con la palabra 'SLIDE_BREAK'.
                """
                
                response = model.generate_content(prompt)
                slides_raw = response.text.split('SLIDE_BREAK')
                
                st.success("¡Contenido generado con éxito!")
                
                for idx, contenido in enumerate(slides_raw[:num_slides]):
                    # Crear links de búsqueda limpios
                    search_query = f"{idea} professional aesthetic"
                    query_encoded = urllib.parse.quote(search_query)
                    
                    unsplash_url = f"https://unsplash.com{query_encoded}"
                    pinterest_url = f"https://pinterest.com{query_encoded}"
                    
                    st.markdown(f"""
                    <div class="slide-card">
                        <h3 style='color: #8B6F47;'>Slide {idx+1}</h3>
                        <div style='color: #4A4A4A; font-family: "Lato", sans-serif; white-space: pre-wrap;'>{contenido.strip()}</div>
                        <hr style='border: 0.5px solid #F5E8E1;'>
                        <p style='font-size: 0.85em; color: #8B6F47;'><b>Sugerencia Visual:</b></p>
                        <a href="{unsplash_url}" target="_blank" style="color: #D4A574; text-decoration: none;">📸 Ver en Unsplash ↗️</a> | 
                        <a href="{pinterest_url}" target="_blank" style="color: #D4A574; text-decoration: none;">📌 Ver en Pinterest ↗️</a>
                    </div>
                    """, unsafe_allow_html=True)
                    
            except Exception as e:
                st.error(f"Hubo un problema con la IA: {e}")
    else:
        st.warning("Escribe una idea antes de generar.")
