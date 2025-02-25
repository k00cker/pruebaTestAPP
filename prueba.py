import streamlit as st
import openai
import os

openai.api_key = st.secrets["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"]

# Configuración de la aplicación en Streamlit
st.title("Generador de Contenido RPG con IA")
st.write("Esta aplicación genera ambientaciones, personajes y enemigos para juegos de rol como Calabozos y Dragones.")

# Entrada de usuario
prompt = st.text_area("Ingresa un prompt para generar contenido RPG:", 
                      "Genera una ambientación de un bosque encantado, incluyendo una descripción detallada del entorno, criaturas que habitan en él y posibles eventos mágicos que puedan ocurrir.")

# Botón para generar contenido
if st.button("Generar Contenido"):
    if prompt:
        with st.spinner("Generando contenido..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "system", "content": "Eres un narrador experto en juegos de rol."},
                              {"role": "user", "content": prompt}]
                )
                st.subheader("Resultado:")
                st.write(response["choices"][0]["message"]["content"])
            except Exception as e:
                st.error(f"Error al generar contenido: {e}")
    else:
        st.warning("Por favor, ingresa un prompt antes de generar contenido.")

# Explicación de cómo funciona
st.sidebar.header("¿Cómo funciona?")
st.sidebar.write("1. Ingresa un prompt con la ambientación, personaje o enemigo que deseas crear.")
st.sidebar.write("2. Haz clic en 'Generar Contenido'.")
st.sidebar.write("3. La IA generará un texto basado en tu solicitud.")
st.sidebar.write("4. Puedes modificar el prompt para obtener diferentes resultados.")
