from sqlalchemy import Column, Integer, String
from app.database import Base


class Doctor(Base):
    __tablename__ = "doctores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    especializacion = Column(String(100), nullable=False)
    duracion_cita = Column(Integer, nullable=False)
