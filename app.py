import streamlit as st
import requests
import os
from dotenv import load_dotenv
from docker_executor import ejecutar_codigo_seguro

# Configuración de la página
st.set_page_config(page_title="mini-ufo3", page_icon="🛸")
st.title("🛸 mini-ufo3")
st.write("Escribe tu prompt y ejecuta el código generado de forma segura en Docker.")

# Cargar variables de entorno
load_dotenv()

# Input para el prompt del usuario
prompt = st.text_area("¿Qué código quieres generar y ejecutar?", 
                     placeholder="Ej: Un script de Python que calcule los primeros 10 números de Fibonacci")

# Botón para ejecutar
if st.button("🚀 Generar y Ejecutar Código"):
    if not prompt:
        st.warning("Por favor, escribe un prompt primero.")
    else:
        # 1. Llamar a la API de DeepSeek
        with st.spinner("Generando código con DeepSeek..."):
            try:
                api_key = os.getenv("DEEPSEEK_API_KEY")
                if not api_key:
                    st.error("Error: No se encontró DEEPSEEK_API_KEY en el archivo .env")
                    st.stop()
                
                headers = {
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                }
                
                payload = {
                    "model": "deepseek-coder",
                    "messages": [
                
                    {"role": "system", "content": "Eres un asistente de programación. Genera solo código Python sin explicaciones. El código debe ser autónomo y NO debe requerir input interactivo del usuario. Usa valores de ejemplo o define las variables directamente en el código."},
                    {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.7
                }
                
                response = requests.post(
                    "https://api.deepseek.com/v1/chat/completions",
                    headers=headers,
                    json=payload
                )
                response.raise_for_status()
                
                # Extraer el código de la respuesta
                codigo_generado = response.json()["choices"][0]["message"]["content"]
                
                # Limpiar el código (remover ```python y ```)
                if "```python" in codigo_generado:
                    codigo_generado = codigo_generado.split("```python")[1].split("```")[0]
                elif "```" in codigo_generado:
                    codigo_generado = codigo_generado.split("```")[1].split("```")[0]
                
            except Exception as e:
                st.error(f"Error al generar el código: {str(e)}")
                st.stop()
        
        # 2. Mostrar el código generado
        st.subheader("Código Generado:")
        st.code(codigo_generado, language="python")
        
        # 3. Ejecutar el código en Docker
        with st.spinner("Ejecutando código en contenedor seguro..."):
            resultado = ejecutar_codigo_seguro(codigo_generado)
        
        # 4. Mostrar resultados
        st.subheader("Resultado de la Ejecución:")
        if resultado["salida"]:
            st.success("Ejecución exitosa:")
            st.text(resultado["salida"])
        elif resultado["error"]:
            st.error("Error durante la ejecución:")
            st.text(resultado["error"])
        else:
            st.warning("No hubo salida ni error.")