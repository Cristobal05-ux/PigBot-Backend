# PigBot Backend

Backend del chatbot especializado en porcicultura, desarrollado con Python y FastAPI.

El sistema permite procesar consultas mediante texto y audio, utilizar inteligencia artificial para generar respuestas y mantener información relevante de las conversaciones mediante un sistema de memoria.

## Tecnologías

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- OpenAI API
- Uvicorn

## Funcionalidades

- Chat mediante texto.
- Chat mediante audio.
- Transcripción de audio mediante OpenAI.
- Generación de respuestas mediante inteligencia artificial.
- Persistencia de conversaciones y mensajes.
- Memoria conversacional de corto plazo.
- Memoria permanente mediante resúmenes automáticos.
- Actualización de información relevante de las conversaciones.
- Arquitectura basada en proveedores para el servicio de transcripción.
- Manejo de errores durante la comunicación con los servicios de inteligencia artificial.

## Instalación y ejecución

Crear y activar el entorno virtual:

python3 -m venv venv
source venv/bin/activate

Instalar las dependencias:

pip install -r requirements.txt

Crear un archivo .env con las credenciales necesarias:

OPENAI_API_KEY=tu_clave_de_openai
DATABASE_URL=tu_url_de_postgresql

Iniciar el servidor:

uvicorn app.main:app --reload

## Integración con Flutter

El frontend puede consumir la API mediante solicitudes HTTP. Para acceder desde otro dispositivo en la misma red, ejecutar:

uvicorn app.main:app --host 0.0.0.0 --port 8000

Después, utilizar la IP local de la computadora como dirección base.

## Estado del proyecto

Backend funcional con chat de texto y audio, persistencia en PostgreSQL y memoria conversacional, preparado para su integración con Flutter.


## Estructura del proyecto

```text
PigBotBackend/
│
├── app/
│   ├── config/
│   ├── conversation/
│   ├── database/
│   ├── models/
│   ├── prompts/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   │   └── providers/
│   └── main.py
│
├── .env.example
├── .gitignore
└── requirements.txt
