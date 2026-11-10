FROM python:3.11-alpine

WORKDIR /app

# Copiar primero las dependencias para aprovechar la caché de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY app.py .

# FastAPI corre por defecto en el puerto 8000
EXPOSE 8000

# Arrancamos la aplicación con Uvicorn en modo producción
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
