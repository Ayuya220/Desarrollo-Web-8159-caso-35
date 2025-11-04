from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app import models
from app.database import get_db
from sqlalchemy.orm import Session

# ==========================================================
# 🔒 CONFIGURACIÓN DEL TOKEN JWT
# ==========================================================
SECRET_KEY = "clave_secreta_floryvida_2025"   # ⚠️ cámbiala antes de producción
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/usuarios/login")


# ==========================================================
# 🧾 CREAR TOKEN DE ACCESO
# ==========================================================
def crear_token_acceso(data: dict, expires_delta: timedelta | None = None):
    """
    Crea un JWT con fecha de expiración.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# ==========================================================
# ✅ VERIFICAR TOKEN Y AUTENTICAR USUARIO
# ==========================================================
def obtener_usuario_actual(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Decodifica el token JWT y retorna el usuario autenticado.
    """
    credenciales_invalidas = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales inválidas o token expirado.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise credenciales_invalidas
    except JWTError:
        raise credenciales_invalidas

    usuario = db.query(models.usuario.Usuario).filter(models.usuario.Usuario.id == user_id).first()
    if usuario is None:
        raise credenciales_invalidas
    return usuario
