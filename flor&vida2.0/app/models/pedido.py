from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Pedido(Base):
    """
    Representa un pedido realizado por un cliente.
    """
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    estado = Column(String, default="pendiente")  # pendiente, pagado, enviado, completado, anulado
    total = Column(Float, nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.now)

    # Relaciones
    usuario = relationship("Usuario", backref="pedidos")
    detalles = relationship("DetallePedido", back_populates="pedido", cascade="all, delete")

class DetallePedido(Base):
    """
    Representa cada producto dentro de un pedido.
    """
    __tablename__ = "detalles_pedido"

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad = Column(Integer, nullable=False)
    subtotal = Column(Float, nullable=False)

    pedido = relationship("Pedido", back_populates="detalles")
