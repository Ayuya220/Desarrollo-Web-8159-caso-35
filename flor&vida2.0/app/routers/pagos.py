from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, models
from app.database import get_db
from datetime import datetime
from typing import List

router = APIRouter(
    prefix="/api/pagos",
    tags=["Pagos"]
)

@router.post("/", response_model=schemas.PagoResponse)
def registrar_pago(pago: schemas.PagoCreate, db: Session = Depends(get_db)):
    nuevo_pago = models.pago.Pago(**pago.dict(), fecha_pago=datetime.now())
    db.add(nuevo_pago)
    db.commit()
    db.refresh(nuevo_pago)
    return nuevo_pago

@router.get("/", response_model=List[schemas.PagoResponse])
def listar_pagos(db: Session = Depends(get_db)):
    return db.query(models.pago.Pago).all()
