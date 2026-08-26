from sqlalchemy import text

from app.database.database import engine

try:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        print("✅ Conexión exitosa con Neon.")
except Exception as e:
    print("❌ Error de conexión:")
    print(e)