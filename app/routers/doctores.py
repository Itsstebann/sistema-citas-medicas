from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate, DoctorResponse
from app.routers.auth import get_current_user

router = APIRouter(prefix="/doctores", tags=["Doctores"])


@router.post("/", response_model=DoctorResponse)
def crear_doctor(doctor: DoctorCreate, db: Session = Depends(get_db), usuario=Depends(get_current_user)):
    nuevo = Doctor(**doctor.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@router.get("/", response_model=list[DoctorResponse])
def listar_doctores(db: Session = Depends(get_db), usuario=Depends(get_current_user)):
    return db.query(Doctor).all()


@router.get("/{doctor_id}", response_model=DoctorResponse)
def obtener_doctor(doctor_id: int, db: Session = Depends(get_db), usuario=Depends(get_current_user)):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    return doctor


@router.delete("/{doctor_id}")
def eliminar_doctor(doctor_id: int, db: Session = Depends(get_db), usuario=Depends(get_current_user)):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    db.delete(doctor)
    db.commit()
    return {"mensaje": "Doctor eliminado"}
