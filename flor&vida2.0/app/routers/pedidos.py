from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, models
from app.database import get_db
from typing import List

router = APIRouter(
    prefix="/api/pedidos",
    tags=["Pedidos"]
)

@router.post("/", response_model=schemas.PedidoResponse)
def crear_pedido(pedido: schemas.PedidoCreate, db: Session = Depends(get_db)):
    nuevo_pedido = models.pedido.Pedido(
        usuario_id=pedido.usuario_id,
        total=pedido.total,
        estado=pedido.estado
    )
    db.add(nuevo_pedido)
    db.commit()
    db.refresh(nuevo_pedido)

    for detalle in pedido.detalles:
        detalle_obj = models.pedido.DetallePedido(
            pedido_id=nuevo_pedido.id,
            producto_id=detalle.producto_id,
            cantidad=detalle.cantidad,
            subtotal=detalle.subtotal
        )
        db.add(detalle_obj)

    db.commit()
    db.refresh(nuevo_pedido)
    return nuevo_pedido

@router.get("/", response_model=List[schemas.PedidoResponse])
def listar_pedidos(db: Session = Depends(get_db)):
    return db.query(models.pedido.Pedido).all()
