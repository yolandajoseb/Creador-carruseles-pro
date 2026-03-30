import streamlit as st
import urllib.parse

# 1. Estética de Marca (Tus colores y fuentes)
st.set_page_config(page_title="Generador Elite", layout="wide")
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    .stApp { background-color: #F5E8E1; }
    h1 { font-family: 'Playfair Display', serif; color: #8B6F47; text-align: center; }
    .slide-box { 
        background-color: white; 
        padding: 20px; 
        border-radius: 15px; 
        border-left: 5px solid #D4A574;
        margin-bottom: 20px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    .stButton>button {
        background-color: #D4A574; color: white; border-radius: 30px; width: 100%; font-weight: bold; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ Creador de Carruseles Mágico")

# 2. Interfaz de Usuario
col1, col2 = st.columns(2)
with col1:
    idea = st.text_input("¿Cuál es la idea base?", placeholder="Ej: Vender productos raros en eBay")
    red_social = st.selectbox("Red Social", ["Instagram", "LinkedIn", "Facebook", "TikTok"])
with col2:
    angulo = st.selectbox("Ángulo", ["Disruptivo", "Dolor", "Solución", "Marketing", "Testimonio"])
    num_slides = st.slider("Número de Slides", 7, 10, 8)

# 3. Lógica de Generación (Sin errores de API)
if st.button("Generar Estructura de Carrusel"):
    if idea:
        st.success(f"¡Estructura para {angulo} generada con éxito!")
        
        # Simulamos la estructura estratégica por slide
        for i in range(1, num_slides + 1):
            # Término de búsqueda dinámico basado en la idea y el slide
            search_term = urllib.parse.quote(f"{idea} aesthetic professional")
            unsplash_url = f"https://unsplash.com{search_term}"
            pinterest_url = f"https://pinterest.com{search_term}"
            
            with st.container():
                st.markdown(f"""
                <div class="slide-box">
                    <h3 style='color: #8B6F47;'>Slide {i}: {'¡El Gancho!' if i==1 else 'Contenido de Valor' if i < num_slides else 'Llamado a la Acción'}</h3>
                    <p style='color: #4A4A4A;'>Aquí va el texto estratégico optimizado para <b>{red_social}</b> basado en tu idea: <i>"{idea}"</i>.</p>
                    <hr>
                    <p style='font-size: 0.9em; color: #8B6F47;'><b>Sugerencia Visual:</b> Busca una imagen que transmita profesionalismo y calma.</p>
                    <p>
                        <a href="{unsplash_url}" target="_blank">📸 Ver en Unsplash ↗️</a> | 
                        <a href="{pinterest_url}" target="_blank">📌 Ver en Pinterest ↗️</a>
                    </p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("Por favor, escribe una idea primero.")
