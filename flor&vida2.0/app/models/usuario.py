from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Usuario(Base):
    """
    Representa a un usuario del sistema (cliente o empleado).
    """
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, unique=True, index=True, nullable=False)
    contrasena = Column(String, nullable=False)
    tipo = Column(String, nullable=False)  # "cliente" o "empleado"
    activo = Column(Boolean, default=True)
