# mini-ufo3 🛸

> Entorno de desarrollo con IA y ejecución segura en Docker

## 🚀 Características principales

- **Generación de código** con DeepSeek API
- **Ejecución segura** en contenedores Docker aislados  
- **Open Interpreter** para corrección automática de errores
- **Soporte multi-tecnología**: Python, Node.js, Java, Bases de Datos
- **Gestión de proyectos** con estructura organizada
- **Interfaz web** con Streamlit

## 📦 Instalación

```bash
# Clonar repositorio
git clone https://github.com/dumbocan/mini-ufo3.git
cd mini-ufo3

# Crear entorno virtual
python -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar API keys
echo "DEEPSEEK_API_KEY=tu_api_key_aqui" > .env
🎯 Uso básico
bash
# Ejecutar aplicación
streamlit run app.py --server.address=127.0.0.1

# Abrir en navegador: http://127.0.0.1:8501
🏗️ Estructura del proyecto
text
mini-ufo3/
├── app.py                 # Interfaz principal Streamlit
├── docker_executor.py     # Ejecución segura en Docker
├── openinterpreter_client.py # Integración con Open Interpreter
├── project_manager.py     # Gestión de proyectos
├── requirements.txt       # Dependencias Python
├── templates/            # Plantillas Dockerfile
│   ├── Dockerfile.python
│   ├── Dockerfile.node
│   ├── Dockerfile.java
│   └── Dockerfile.db
├── proyectos/            # Proyectos de usuario
└── README.md            # Este archivo

🔧 Dependencias principales

streamlit - Interfaz web

docker - Cliente Python para Docker

requests - Cliente HTTP para APIs

open-interpreter - Ejecución y corrección automática

python-dotenv - Variables de entorno