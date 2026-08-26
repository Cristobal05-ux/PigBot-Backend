from fastapi import FastAPI
from app.routes.chat import router as chat_router

app = FastAPI(
    title="PigBot API",
    description="API para crear el chatbot de apoyo a criadores de cerdos",
    version="1.0.0"
)

@app.get("/")
def inicio():
    return {
        "message": "Bienvenido a PigBot API"
    }

app.include_router(chat_router)