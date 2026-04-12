from pydantic import BaseModel


class DoctorCreate(BaseModel):
    nombre: str
    especializacion: str
    duracion_cita: int


class DoctorResponse(BaseModel):
    id: int
    nombre: str
    especializacion: str
    duracion_cita: int

    class Config:
        from_attributes = True
