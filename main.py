from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import pacientes_router, doctores_router, citas_router, auth_router

app = FastAPI(
    title="Sistema de Citas Médicas",
    description="API REST para gestión de citas médicas",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(pacientes_router)
app.include_router(doctores_router)
app.include_router(citas_router)


@app.get("/", tags=["General"])
def root():
    return {"mensaje": "Bienvenido al Sistema de Citas Médicas"}
