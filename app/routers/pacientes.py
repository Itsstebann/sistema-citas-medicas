from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.paciente import Paciente
from app.schemas.paciente import PacienteCreate, PacienteResponse
from app.routers.auth import get_current_user

router = APIRouter(prefix="/pacientes", tags=["Pacientes"])


@router.post("/", response_model=PacienteResponse)
def crear_paciente(paciente: PacienteCreate, db: Session = Depends(get_db), usuario=Depends(get_current_user)):
    existe = db.query(Paciente).filter(
        Paciente.cedula == paciente.cedula).first()
    if existe:
        raise HTTPException(
            status_code=400, detail="Ya existe un paciente con esa cédula")
    nuevo = Paciente(**paciente.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@router.get("/", response_model=list[PacienteResponse])
def listar_pacientes(db: Session = Depends(get_db), usuario=Depends(get_current_user)):
    return db.query(Paciente).all()


@router.get("/{paciente_id}", response_model=PacienteResponse)
def obtener_paciente(paciente_id: int, db: Session = Depends(get_db), usuario=Depends(get_current_user)):
    paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente
