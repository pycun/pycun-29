# 🤖 WispHub Chatbot

Un chatbot inteligente creado a partir de los manuales de WispHub usando **Gradio**, la librería de **OpenAI**, el modelo de **Gemini** y desplegado en **Hugging Face**.

## 🚀 Tecnologías Utilizadas
- 🖥️ **Gradio** - Para la interfaz web interactiva.
- 🤯 **OpenAI** - Para el manejo del modelo de lenguaje.
- 🌌 **Gemini** - Modelo avanzado para procesar el lenguaje natural.
- 🧠 **Hugging Face** - Para el despliegue del chatbot en la nube.

## 📋 Instalación
Sigue estos pasos para instalar y ejecutar el proyecto:

```bash
# Clonar el repositorio
git clone https://huggingface.co/spaces/Daniel00611/ManualChatbot
cd wisphub-chatbot

# Instalar dependencias
pip install gradio openai huggingface_hub
```

## ⚙️ Configuración
1. Obtén tu clave de API de OpenAI y configúra la variable de entorno:

```bash
export OPENAI_API_KEY=tu_clave_aqui
```

2. Si utilizas el Hub de Hugging Face, inicia sesión con:
```bash
huggingface-cli login
```

## ▶️ Ejecución
Para iniciar la aplicación ejecuta:
```bash
python app.py
```

La interfaz estará disponible en tu navegador en: [http://localhost:7860](http://localhost:7860)

## 📝 Uso
1. Escribe tu pregunta relacionada con WispHub en el campo de texto.
2. Haz clic en **"Enviar"**.
3. Recibe respuestas claras y precisas basadas en los manuales de WispHub.

## 📦 Requisitos
- `huggingface_hub==0.25.2`
- `openai==1.61.1`

## 🧩 Futuras Mejoras
- 🔍 Incorporar búsqueda avanzada en los manuales.
- 📚 Optimizar la organización del contenido para mayor precisión.

## 📄 Licencia
Este proyecto está bajo la licencia **cc-by-nc-4.0**.

---

💬 **¡Gracias por visitar este proyecto! Si tienes preguntas o sugerencias, no dudes en contactarme.**

