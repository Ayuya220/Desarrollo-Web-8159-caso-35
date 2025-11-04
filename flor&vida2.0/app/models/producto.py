from sqlalchemy import Column, Integer, String, Float, Boolean
from app.database import Base

class Producto(Base):
    """
    Representa un producto del catálogo de Flor y Vida.
    """
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    activo = Column(Boolean, default=True)
