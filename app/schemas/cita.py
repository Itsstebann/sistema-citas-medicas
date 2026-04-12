from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from app.schemas.paciente import PacienteResponse
from app.schemas.doctor import DoctorResponse


class EstadoCita(str, Enum):
    libre = "libre"
    ocupada = "ocupada"


class CitaCreate(BaseModel):
    fecha_hora: datetime
    doctor_id: int
    sintomas: str | None = None
    urgencia: int | None = None


class CitaResponse(BaseModel):
    id: int
    fecha_hora: datetime
    estado: EstadoCita
    sintomas: str | None
    urgencia: int | None
    paciente: PacienteResponse | None
    doctor: DoctorResponse

    class Config:
        from_attributes = True
