# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import usuarios, productos, pedidos, pagos, boletas

# ==========================================================
# 🌸 Inicialización de la aplicación principal
# ==========================================================
app = FastAPI(
    title="🌸 Flor y Vida API",
    description="Backend oficial de Flor y Vida — Maneja usuarios, productos, pedidos y pagos.",
    version="1.0.0"
)

# ==========================================================
# 🔓 Configuración de CORS (permite conexión desde el Frontend)
# ==========================================================
# Si tu frontend está en localhost o en otro dominio, agrégalo aquí:
origins = [
    "https://ayuya220.github.io",  # Tu frontend en GitHub Pages
    "http://localhost",            # Para pruebas locales
    "http://127.0.0.1:5500"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================================
# 🔗 Registro de routers (modulares)
# ==========================================================
app.include_router(usuarios.router)
app.include_router(productos.router)
app.include_router(pedidos.router)
app.include_router(pagos.router)
app.include_router(boletas.router)

# ==========================================================
# 🏁 Ruta raíz
# ==========================================================
@app.get("/")
def home():
    return {
        "mensaje": "🌸 Bienvenida al backend de Flor y Vida 💐",
        "version": "1.0.0",
        "autor": "Equipo Flor y Vida"
    }