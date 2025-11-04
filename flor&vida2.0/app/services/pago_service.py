from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime

def registrar_pago(db: Session, pago: schemas.PagoCreate):
    """Registra un nuevo pago para un pedido."""
    nuevo_pago = models.pago.Pago(
        pedido_id=pago.pedido_id,
        monto=pago.monto,
        metodo=pago.metodo,
        estado=pago.estado,
        fecha_pago=datetime.now()
    )
    db.add(nuevo_pago)
    db.commit()
    db.refresh(nuevo_pago)
    return nuevo_pago


def listar_pagos(db: Session):
    """Obtiene todos los pagos realizados."""
    return db.query(models.pago.Pago).all()
