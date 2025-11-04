from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field

# ==========================================================
# 🧍‍♀️ USUARIOS
# ==========================================================

class UsuarioBase(BaseModel):
    nombre: str
    correo: EmailStr
    tipo: str = Field(..., description="Puede ser 'cliente' o 'empleado'")

class UsuarioCreate(UsuarioBase):
    contrasena: str

class UsuarioResponse(UsuarioBase):
    id: int
    activo: bool

    class Config:
        orm_mode = True  # Permite convertir modelos SQLAlchemy → Pydantic


# ==========================================================
# 🌸 PRODUCTOS
# ==========================================================

class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    stock: int

class ProductoCreate(ProductoBase):
    pass  # No necesita campos adicionales

class ProductoResponse(ProductoBase):
    id: int
    activo: bool

    class Config:
        orm_mode = True


# ==========================================================
# 📦 PEDIDOS
# ==========================================================

class DetallePedidoBase(BaseModel):
    producto_id: int
    cantidad: int
    subtotal: float

class DetallePedidoCreate(DetallePedidoBase):
    pass

class DetallePedidoResponse(DetallePedidoBase):
    id: int

    class Config:
        orm_mode = True


class PedidoBase(BaseModel):
    usuario_id: int
    total: float
    estado: Optional[str] = "pendiente"

class PedidoCreate(PedidoBase):
    detalles: List[DetallePedidoCreate]

class PedidoResponse(PedidoBase):
    id: int
    fecha_creacion: datetime
    detalles: List[DetallePedidoResponse]

    class Config:
        orm_mode = True


# ==========================================================
# 💳 PAGOS
# ==========================================================

class PagoBase(BaseModel):
    pedido_id: int
    monto: float
    metodo: Optional[str] = "WebPay"
    estado: Optional[str] = "pendiente"

class PagoCreate(PagoBase):
    pass

class PagoResponse(PagoBase):
    id: int
    fecha_pago: datetime

    class Config:
        orm_mode = True


# ==========================================================
# 🧾 BOLETAS
# ==========================================================

class BoletaBase(BaseModel):
    pedido_id: int
    total: float

class BoletaCreate(BoletaBase):
    numero_boleta: str

class BoletaResponse(BoletaBase):
    id: int
    numero_boleta: str
    fecha_emision: datetime

    class Config:
        orm_mode = True
