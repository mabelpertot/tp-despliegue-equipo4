import os
import sentry_sdk
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# 1. Lectura de variables de entorno desde PaaS (Render)
SENTRY_DSN = os.getenv("SENTRY_DSN")

# 2. Inicialización de Sentry SDK si la variable DSN está presente
if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        traces_sample_rate=1.0,
        environment=os.getenv("ENVIRONMENT", "production")
    )

app = FastAPI(
    title="API TP Despliegue - Equipo 4",
    version="1.0.0"
)

# 3. Configuración de CORS para permitir peticiones desde el Frontend 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint raíz
@app.get("/")
def read_root():
    return {
        "estado": "online",
        "equipo": "Equipo N° 4",
        "mensaje": "Backend FastAPI desplegado exitosamente con Sentry"
    }

# Endpoint obligatorio para probar Sentry 
@app.get("/sentry-debug")
def trigger_error():
    try:
        # Forzamos el error que Sentry va a capturar
        division_by_zero = 1 / 0
    except Exception as e:
        # Sentry captura el error explícitamente
        sentry_sdk.capture_exception(e)
        # Devolvemos una respuesta JSON 
        return {
            "estado": "error_capturado",
            "mensaje": "⚠️ Se ha provocado un error de prueba de forma controlada.",
            "detalle": "El incidente fue registrado exitosamente en Sentry con éxito para la demo del Equipo Nº 4."
        }