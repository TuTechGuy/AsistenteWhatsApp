# 🤖 Asistente para WhatsApp con Python, Twilio y OpenAI

Este proyecto te enseña cómo crear tu propio **asistente inteligente en WhatsApp** usando `Python`, `Twilio` y `OpenAI`. El asistente es capaz de entender tus mensajes y responder como si fuera un chatbot avanzado, ¡ideal para automatizar respuestas o crear tu propio bot personalizado!

📺 **Mira el video completo en YouTube:**  
👉 [Cómo crear un asistente para WhatsApp con Python y OpenAI](https://www.youtube.com/tu-enlace-al-video)

---

## 🚀 Tecnologías usadas

- **Python 3.12**
- **Twilio** – Para recibir y enviar mensajes por WhatsApp
- **OpenAI API** – Para generar respuestas inteligentes (GPT)
- **Flask** – Para crear una API simple que maneje los mensajes

---

## 🧠 ¿Qué hace el asistente?

✅ Recibe mensajes desde WhatsApp  
✅ Usa OpenAI (ChatGPT) para interpretar y responder  
✅ Responde de forma automática desde tu número de WhatsApp  
✅ Puede ser adaptado para casos reales como atención al cliente, bots educativos, etc.

---

## ⚙️ Instalación

1. **Clona el repositorio:**

```bash
git clone https://github.com/TuTechGuy/AsistenteWhatsApp.git
cd AsistenteWhatsApp
```

2. **Instala las dependencias:**

```bash
pip install -r requirements.txt
```

3. **Configura las variables de entorno (`.env`):**

```env
TWILIO_ACCOUNT_SID=tu_sid
TWILIO_AUTH_TOKEN=tu_token
TWILIO_PHONE_NUMBER=whatsapp:tu_numero_twilio
OPENAI_API_KEY=tu_clave_api
```

4. **Ejecuta la app localmente:**

```bash
python app.py
```

5. **Usa [ngrok](https://ngrok.com/) para exponer tu servidor:**

```bash
ngrok http 5000
```

6. **Configura el webhook en Twilio con la URL de ngrok.**

---

## 📦 Estructura del proyecto
```
📁 asistente-whatsapp
├── app.py
├── requirements.txt
├── .env
├── README.md
├── utils
│   └── utils.py
```

---

## 📹 Video tutorial

Este repositorio está conectado con un video en mi canal de YouTube donde explico paso a paso cómo funciona todo el sistema:

🎬 **Míralo aquí:** [https://www.youtube.com/tu-enlace-al-video](https://www.youtube.com/tu-enlace-al-video)

---

## 🧩 Próximas mejoras

- [ ] Memoria de conversación
- [ ] Integración con bases de datos
- [ ] Soporte para múltiples usuarios
- [ ] Panel de control para mensajes

---

## ⭐ Si te gustó este proyecto...

¡No olvides dejar una estrella ⭐ en el repo y suscribirte al canal! 🙌
