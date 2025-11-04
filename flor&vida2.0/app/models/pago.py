from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Pago(Base):
    """
    Representa un pago realizado por un cliente.
    """
    __tablename__ = "pagos"

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    monto = Column(Float, nullable=False)
    metodo = Column(String, default="WebPay")  # WebPay, Servipag, etc.
    estado = Column(String, default="pendiente")  # pendiente, aprobado, rechazado
    fecha_pago = Column(DateTime, default=datetime.now)

    pedido = relationship("Pedido", backref="pago")
