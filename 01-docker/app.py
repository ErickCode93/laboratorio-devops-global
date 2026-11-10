from fastapi import FastAPI, Response # <-- Importamos Response
import time

app = FastAPI(title="API Corporativa de Ventas", version="1.0.0")
start_time = time.time()

@app.get("/")
def read_root():
    return {
        "status": "online",
        "canal": "ventas",
        "timestamp": time.time(),
        "mensaje": "Conexión exitosa con el Backend de FastAPI"
    }

@app.get("/healthz")
def health_check():
    return {"status": "healthy", "uptime": f"{round(time.time() - start_time, 2)}s"}

@app.get("/metrics")
def metrics():
    uptime = time.time() - start_time
    contenido = f"# HELP app_uptime_seconds Uptime de la aplicacion\n# TYPE app_uptime_seconds gauge\napp_uptime_seconds {uptime}\n"
    
    # 🚀 FORZAMOS EL FORMATO CORPORATIVO QUE EXIGE PROMETHEUS
    return Response(content=contenido, media_type="text/plain")
