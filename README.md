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

Requisitos previos

Antes de ejecutar el proyecto, necesitas:

Python instalado.

Git.

Acceso a una base de datos PostgreSQL.

Una clave de API de OpenAI.

Conexión a Internet para comunicarte con los servicios externos.

Instalación

1. Clonar el repositorio

git clone https://github.com/Cristobal05-ux/PigBot-Backend.git
cd PigBot-Backend

2. Crear un entorno virtual

python3 -m venv venv

Activar el entorno virtual en macOS o Linux:

source venv/bin/activate

En Windows:

venv\Scripts\activate

3. Instalar las dependencias

python -m pip install -r requirements.txt

4. Configurar las variables de entorno

Crear un archivo .env en la raíz del proyecto, tomando como referencia .env.example.

OPENAI_API_KEY=tu_clave_de_openai
DATABASE_URL=tu_url_de_conexion_postgresql

Sustituye los valores de ejemplo por tus propias credenciales.

Importante: no compartas ni subas el archivo .env a GitHub. Las credenciales deben permanecer fuera del código fuente y del repositorio.

5. Ejecutar el backend

uvicorn app.main:app --reload

Por defecto, la aplicación estará disponible en:

http://127.0.0.1:8000

Documentación y pruebas de la API

FastAPI genera documentación interactiva automáticamente.

Una vez iniciado el servidor, accede a:

http://127.0.0.1:8000/docs

Desde Swagger puedes consultar los endpoints, enviar solicitudes y comprobar las respuestas de la API.

Endpoints principales

1. Chat mediante texto

Método: POST

Ruta: /chat

Permite enviar un mensaje de texto y recibir una respuesta generada por la inteligencia artificial.

Solicitud JSON:

{
  "mensaje": "Tengo 50 cerdos en etapa de engorda"
}

Respuesta:

{
  "respuesta": "..."
}

El contenido de respuesta corresponde al texto generado por el chatbot.

2. Chat mediante audio

Método: POST

Ruta: /chat/audio

Permite enviar un archivo de audio para su transcripción y procesamiento por el chatbot.

La solicitud debe utilizar multipart/form-data con un campo llamado file que contenga el archivo de audio.

Flujo de procesamiento:

Se recibe y valida el archivo.

El servicio de transcripción convierte el audio en texto.

El texto transcrito se procesa mediante el servicio de chat.

Se recupera y actualiza el contexto conversacional según corresponda.

Se devuelve la respuesta generada por la IA.

Respuesta:

{
  "respuesta": "..."
}

Sistema de memoria conversacional

PigBot cuenta con mecanismos para conservar información de las conversaciones y utilizarla como contexto en respuestas posteriores.

Memoria de corto plazo

Recupera mensajes recientes para proporcionar contexto al modelo de inteligencia artificial durante la generación de respuestas.

Memoria de largo plazo

Utiliza resúmenes almacenados en la base de datos para conservar información relevante de conversaciones anteriores.

El sistema utiliza un prompt especializado para generar y actualizar los resúmenes, procurando mantener los datos útiles y el contexto acumulado.

La actualización se activa según el umbral de mensajes configurado en el backend.

Arquitectura del servicio de transcripción

El servicio de transcripción utiliza una arquitectura basada en proveedores. Esto permite separar la lógica del chatbot de la implementación concreta del servicio de reconocimiento de audio.

Actualmente, se utiliza OpenAI como proveedor de transcripción. Esta estructura facilita la incorporación de otros proveedores en el futuro sin tener que modificar toda la lógica de procesamiento del chat.

Integración con Flutter

El frontend puede consumir los endpoints del backend mediante solicitudes HTTP.

Para la integración se necesita:

La URL base del backend.

El endpoint correspondiente.

El formato de la solicitud.

El formato de la respuesta.

La clave de OpenAI y las credenciales de PostgreSQL deben permanecer exclusivamente en el backend.

Acceso desde otro dispositivo en la misma red

Para permitir conexiones desde otro dispositivo conectado a la misma red local, ejecuta:

uvicorn app.main:app --host 0.0.0.0 --port 8000

Después, utiliza la dirección IP local de la computadora que ejecuta el backend, por ejemplo:

http://192.168.1.100:8000

La IP anterior es ilustrativa: debes sustituirla por la dirección real de tu computadora.

Para probar la API desde otro dispositivo:

http://IP_DE_TU_COMPUTADORA:8000/docs

Ambos dispositivos deben tener conectividad entre sí. Este método está destinado al desarrollo en una red local; para un despliegue público se requiere una configuración de producción adecuada.

Seguridad

Las credenciales se gestionan mediante variables de entorno.

El archivo .env no debe subirse al repositorio.

El archivo .env.example sirve como plantilla sin credenciales reales.

Las solicitudes y los archivos de audio deben validarse antes de procesarse.

Para un despliegue público, se recomienda configurar HTTPS, controles de acceso, límites de solicitudes y restricciones para los archivos recibidos.

Estado del proyecto

El backend cuenta con funcionalidades de chat mediante texto y audio, persistencia en PostgreSQL y memoria conversacional.

La API está preparada para utilizarse como servicio de backend de una aplicación frontend. La integración final con Flutter depende de conectar la interfaz con los endpoints documentados.
