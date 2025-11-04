from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException
from datetime import datetime

def crear_pedido(db: Session, pedido: schemas.PedidoCreate):
    """Crea un pedido con sus detalles asociados."""
    nuevo_pedido = models.pedido.Pedido(
        usuario_id=pedido.usuario_id,
        total=pedido.total,
        estado=pedido.estado,
        fecha_creacion=datetime.now()
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


def listar_pedidos(db: Session):
    """Retorna todos los pedidos registrados."""
    return db.query(models.pedido.Pedido).all()


def obtener_pedido_por_id(db: Session, pedido_id: int):
    """Busca un pedido por su ID."""
    pedido = db.query(models.pedido.Pedido).filter(models.pedido.Pedido.id == pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado.")
    return pedido
