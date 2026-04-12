from pydantic import BaseModel


class PacienteCreate(BaseModel):
    nombre: str
    cedula: str
    celular: str


class PacienteResponse(BaseModel):
    id: int
    nombre: str
    cedula: str
    celular: str

    class Config:
        from_attributes = True
