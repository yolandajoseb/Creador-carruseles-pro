import streamlit as st
import urllib.parse

# 1. Aesthetic Configuration of your Brand (#8B6F47, #D4A574)
st.set_page_config(page_title="Generador de Carruseles Elite", layout="wide")

st.markdown("""
    <style>
    @import url('https://googleapis.com');
    .stApp { background-color: #FAF8F5; }
    h1 { font-family: 'Playfair Display', serif; color: #8B6F47; text-align: center; margin-bottom: 20px; }
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

# 2. User Interface
col1, col2 = st.columns(2)
with col1:
    idea = st.text_area("¿Cuál es la idea base de tu contenido?", placeholder="Ej: Contacto cero con la familia de origen")
    red_social = st.selectbox("Red Social", ["Instagram", "LinkedIn", "Facebook", "TikTok Series"])
with col2:
    angulo = st.selectbox("Ángulo de Contenido", ["Disruptivo", "Dolor del cliente", "Solución al problema", "Marketing", "Testimonio"])
    num_slides = st.slider("Número de Slides", 7, 10, 10)

# 3. Logic of Content Structure (Without external APIs)
if st.button("¡Generar Estructura de Carrusel!"):
    if idea:
        st.success(f"Estructura generada para: {idea}")
        
        # We define strategic titles according to the slide
        for i in range(1, num_slides + 1):
            if i == 1:
                titulo = "🪝 El Gancho (Hook)"
                descripcion = f"Presenta el problema de '{idea}' de forma impactante para detener el scroll."
            elif i == num_slides:
                titulo = "📢 Llamado a la Acción (CTA)"
                descripcion = f"Diles qué hacer ahora: 'Sígueme para más consejos sobre {idea}' o 'Comenta tu experiencia'."
            else:
                titulo = f"💡 Slide de Valor {i-1}"
                descripcion = f"Punto clave número {i-1} sobre cómo abordar '{idea}' desde un ángulo {angulo}."

            # CREATION OF CORRECT LINKS
            # We clean the idea so that the URL is valid
            query_limpia = idea.replace(",", "").replace(".", "")
            search_query = f"{query_limpia} aesthetic professional"
            query_encoded = urllib.parse.quote(search_query)
            
            # Final corrected URLs
            unsplash_url = f"https://unsplash.com{query_encoded}"
            pinterest_url = f"https://pinterest.com{query_encoded}"
            
            st.markdown(f"""
            <div class="slide-card">
                <h3 style='color: #8B6F47;'>{titulo}</h3>
                <p style='color: #4A4A4A; font-family: "Lato", sans-serif;'>{descripcion}</p>
                <hr style='border: 0.5px solid #F5E8E1;'>
                <p style='font-size: 0.85em; color: #8B6F47;'><b>Sugerencia de Imágenes Profesionales:</b></p>
                <a href="{unsplash_url}" target="_blank" style="color: #D4A574; text-decoration: none; font-weight: bold;">📸 Buscar en Unsplash ↗️</a> | 
                <a href="{pinterest_url}" target="_blank" style="color: #D4A574; text-decoration: none; font-weight: bold;">📌 Buscar en Pinterest ↗️</a>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("Por favor, escribe una idea para comenzar.")
