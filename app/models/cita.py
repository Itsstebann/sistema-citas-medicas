from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum


class EstadoCita(enum.Enum):
    libre = "libre"
    ocupada = "ocupada"


class Cita(Base):
    __tablename__ = "citas"

    id = Column(Integer, primary_key=True, index=True)
    fecha_hora = Column(DateTime, nullable=False)
    estado = Column(Enum(EstadoCita), default=EstadoCita.libre)
    sintomas = Column(String(500), nullable=True)
    urgencia = Column(Integer, nullable=True)

    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=True)
    doctor_id = Column(Integer, ForeignKey("doctores.id"), nullable=False)

    paciente = relationship("Paciente")
    doctor = relationship("Doctor")
