from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, models
from app.database import get_db
from datetime import datetime
from typing import List

router = APIRouter(
    prefix="/api/boletas",
    tags=["Boletas"]
)

@router.post("/", response_model=schemas.BoletaResponse)
def generar_boleta(boleta: schemas.BoletaCreate, db: Session = Depends(get_db)):
    nueva_boleta = models.boleta.Boleta(
        pedido_id=boleta.pedido_id,
        total=boleta.total,
        numero_boleta=boleta.numero_boleta,
        fecha_emision=datetime.now()
    )
    db.add(nueva_boleta)
    db.commit()
    db.refresh(nueva_boleta)
    return nueva_boleta

@router.get("/", response_model=List[schemas.BoletaResponse])
def listar_boletas(db: Session = Depends(get_db)):
    return db.query(models.boleta.Boleta).all()
