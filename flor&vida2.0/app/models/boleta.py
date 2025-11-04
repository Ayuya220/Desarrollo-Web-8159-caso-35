from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Boleta(Base):
    """
    Representa la boleta digital emitida después de un pago exitoso.
    """
    __tablename__ = "boletas"

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    total = Column(Float, nullable=False)
    numero_boleta = Column(String, unique=True, index=True)
    fecha_emision = Column(DateTime, default=datetime.now)

    pedido = relationship("Pedido", backref="boleta")
