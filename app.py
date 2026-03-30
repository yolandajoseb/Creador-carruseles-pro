import streamlit as st
import urllib.parse

# 1. Configuración de Marca y Estética Premium
st.set_page_config(page_title="Generador de Carruseles Elite", layout="wide")

st.markdown("""
    <style>
    @import url('https://googleapis.com');
    .stApp { background-color: #FAF8F5; }
    h1 { font-family: 'Playfair Display', serif; color: #8B6F47; text-align: center; font-size: 3rem; margin-bottom: 10px; }
    .subtitle { font-family: 'Lato', sans-serif; color: #D4A574; text-align: center; margin-bottom: 40px; font-weight: bold; }
    .slide-card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        border-top: 8px solid #D4A574;
        margin-bottom: 25px;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.05);
        font-family: 'Lato', sans-serif;
    }
    .stButton>button {
        background-color: #8B6F47; color: white; border-radius: 50px; width: 100%; 
        font-weight: bold; border: none; padding: 15px; font-size: 1.1rem; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #D4A574; transform: translateY(-2px); }
    </style>
    """, unsafe_allow_html=True)

st.write("<h1>Estratega de Carruseles</h1>", unsafe_allow_html=True)
st.write("<p class='subtitle'>Crea contenido de alto impacto con tu esencia</p>", unsafe_allow_html=True)

# 2. Interfaz de Usuario
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        idea = st.text_input("✨ Idea base de tu contenido", placeholder="Ej: Contacto cero con la familia")
        red_social = st.selectbox("📱 Red Social", ["Instagram", "LinkedIn", "Facebook", "TikTok Series"])
    with col2:
        angulo = st.selectbox("🎯 Ángulo Estratégico", ["Disruptivo", "Dolor del cliente", "Solución al problema", "Marketing", "Testimonio"])
        num_slides = st.slider("🔢 Número de Slides", 7, 10, 8)

# 3. Lógica de Contenido por Ángulo (Sin APIs externas para evitar errores)
def generar_texto(idx, total, idea, angulo):
    if idx == 1:
        return f"HOOK: ¿Sabías que '{idea}' no tiene que ser un proceso solitario? Descubre por qué."
    if idx == total:
        return f"CTA: Si te sentiste identificada con este mensaje sobre '{idea}', guarda este post y sígueme."
    
    consejos = {
        "Disruptivo": f"Punto {idx-1}: Olvida lo que te dijeron. En el tema de {idea}, la clave es romper el patrón.",
        "Dolor del cliente": f"Punto {idx-1}: Entiendo el peso de {idea}. No es tu culpa sentirte así.",
        "Solución al problema": f"Paso {idx-1}: Para dominar {idea}, empieza por este pequeño cambio hoy.",
        "Marketing": f"Beneficio {idx-1}: Cómo mejorar tu vida aplicando esta técnica de {idea}.",
        "Testimonio": f"Lección {idx-1}: Lo que aprendí después de superar el reto de {idea}."
    }
    return consejos.get(angulo, f"Desarrollo del punto {idx-1} sobre {idea}")

# 4. Ejecución
if st.button("✨ GENERAR ESTRUCTURA MAESTRA"):
    if idea:
        st.write("---")
        for i in range(1, num_slides + 1):
            texto_final = generar_texto(i, num_slides, idea, angulo)
            
            # LINKS CORREGIDOS (Con el '/' después del .com)
            query_limpia = urllib.parse.quote(f"{idea} professional aesthetic")
            unsplash_url = f"https://unsplash.com{query_limpia}"
            pinterest_url = f"https://pinterest.com{query_limpia}"
            
            st.markdown(f"""
            <div class="slide-card">
                <h3 style='color: #8B6F47; margin-top:0;'>Desliza {i} / {num_slides}</h3>
                <p style='font-size: 1.2rem; line-height: 1.6;'>{texto_final}</p>
                <div style='background-color: #FAF8F5; padding: 15px; border-radius: 10px; margin-top: 20px;'>
                    <p style='color: #8B6F47; font-weight: bold; font-size: 0.9rem; margin-bottom: 10px;'>📸 RECURSOS VISUALES SUGERIDOS:</p>
                    <a href="{unsplash_url}" target="_blank" style="color: #D4A574; text-decoration: none; font-weight: bold; margin-right: 20px;">Ver en Unsplash ↗️</a>
                    <a href="{pinterest_url}" target="_blank" style="color: #D4A574; text-decoration: none; font-weight: bold;">Ver en Pinterest ↗️</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Por favor, introduce una idea para que la magia comience.")
