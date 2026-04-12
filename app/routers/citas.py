from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.cita import Cita
from app.models.doctor import Doctor
from app.schemas.cita import CitaCreate, CitaResponse, EstadoCita
from app.routers.auth import get_current_user

router = APIRouter(prefix="/citas", tags=["Citas"])


@router.post("/", response_model=CitaResponse)
def agendar_cita(cita: CitaCreate, db: Session = Depends(get_db), usuario=Depends(get_current_user)):
    doctor = db.query(Doctor).filter(Doctor.id == cita.doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")

    if cita.paciente_id:
        from app.models.paciente import Paciente
        paciente = db.query(Paciente).filter(
            Paciente.id == cita.paciente_id).first()
        if not paciente:
            raise HTTPException(
                status_code=404, detail="Paciente no encontrado")

    conflicto = db.query(Cita).filter(
        Cita.doctor_id == cita.doctor_id,
        Cita.fecha_hora == cita.fecha_hora
    ).first()
    if conflicto:
        raise HTTPException(
            status_code=400, detail="El doctor ya tiene una cita en ese horario")

    nueva = Cita(**cita.model_dump())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


@router.get("/", response_model=list[CitaResponse])
def listar_citas(db: Session = Depends(get_db), usuario=Depends(get_current_user)):
    return db.query(Cita).all()


@router.get("/{cita_id}", response_model=CitaResponse)
def obtener_cita(cita_id: int, db: Session = Depends(get_db), usuario=Depends(get_current_user)):
    cita = db.query(Cita).filter(Cita.id == cita_id).first()
    if not cita:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita


@router.patch("/{cita_id}/estado", response_model=CitaResponse)
def actualizar_estado(cita_id: int, estado: EstadoCita, db: Session = Depends(get_db), usuario=Depends(get_current_user)):
    cita = db.query(Cita).filter(Cita.id == cita_id).first()
    if not cita:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    cita.estado = estado
    db.commit()
    db.refresh(cita)
    return cita
