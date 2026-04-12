from pydantic import BaseModel, field_validator
import re


class PacienteCreate(BaseModel):
    nombre: str
    cedula: str
    celular: str

    @field_validator("celular")
    @classmethod
    def validar_celular(cls, v):
        if not re.match(r"^\+?[0-9]{7,15}$", v):
            raise ValueError(
                "El celular debe contener solo números, entre 7 y 15 dígitos")
        return v


class PacienteResponse(BaseModel):
    id: int
    nombre: str
    cedula: str
    celular: str

    class Config:
        from_attributes = True
