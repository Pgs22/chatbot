# Práctica Final RA3 Análisis predictivo de la información

## Descripción
Proyecto **Generación Aumentada por Recuperación (RAG)**. El objetivo es permitir que un usuario realice preguntas en inglés sobre una base de conocimiento específica (almacenada en `documentos.json`). 

Resumen de funciones:
1.  **Recuperación**: Encuentra los documentos más similares a la consulta del usuario utilizando embeddings de `sentence-transformers`.
2.  **Aumentación**: Inyecta los documentos relevantes en un prompt diseñado para el modelo de lenguaje.
3.  **Generación**: Un modelo de lenguaje (LLM) genera una respuesta precisa basada exclusivamente en el contexto proporcionado.

## Estructura de Archivos
* `rag_engine.py`: Motor lógico que contiene las funciones de recuperación y generación.
* `app.py`: Interfaz gráfica de usuario construida con Gradio.
* `documents.json`: Base de datos de conocimiento en formato JSON.
* `requirements.txt`: Lista de dependencias necesarias para ejecutar el proyecto.

## Subir a Github
cambia el fichero .gitognore.txt a .gitignore antes de subirlo al repositorio
### Desde la PowerShell
```bash
mv .\.gitignore.txt .\.gitignore
```
### Terminal Linux o Git Bash
```bash
mv .gitignore.txt .gitignore
```

# Limpiar la caché de Git para aplicar cambios .gitignore
```bash
git rm -r --cached .
git add .
git commit -m "Fix: renamed gitignore and cleared cache"
```

## Instrucciones de Instalación y Ejecución

### 1. Requisitos Previos
Tener instalado Python 3.9 o superior.

### 2. Instalación de Dependencias
Ejecuta el siguiente comando en tu terminal para instalar las librerías necesarias:

```bash
pip install -r requirements.txt
```

### 3. Ejecución del Proyecto
```bash
python app.py
```

## Instrucciones Space Hugging Face con Gradio

# When prompted for a password, use an access token with write permissions.
# Generate one from your settings: https://huggingface.co/settings/tokens
```bash
git clone https://huggingface.co/spaces/Patriciagsbcn/practica-chat
```

# Make sure the hf CLI is installed
```bash
powershell -ExecutionPolicy ByPass -c "irm https://hf.co/cli/install.ps1 | iex"
```

# Download the Space
```bash
hf download Patriciagsbcn/practica-chat --repo-type=space
```

# Create your gradio app.py file:
import gradio as gr

def greet(name):
    return "Hello " + name + "!!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch()

# Then commit and push:
```bash
git add app.py && git commit -m 'Add application file' && git push
```

## Dependencies
You can add a requirements.txt file at the root of the repository to specify Python dependencies
If needed, you can also add a packages.txt file at the root of the repository to specify Debian dependencies.
The gradio package is pre-installed and its version is set in the sdk_version field in the README.md file.
Personalize your Space
Make your Space stand out by customizing its emoji, colors, and description by editing metadata in its README.md file.
Documentation
Read the full documentation for gradio Spaces here --> https://www.gradio.app/docs

### Readme
https://huggingface.co/docs/hub/spaces-config-reference
title: Practica Chat
emoji: 📉
colorFrom: pink
colorTo: yellow
sdk: gradio
sdk_version: 6.10.0
app_file: app.py
pinned: false
short_description: ChatBot
Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference