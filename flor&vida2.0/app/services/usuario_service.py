from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException

def crear_usuario(db: Session, usuario: schemas.UsuarioCreate):
    """Crea un nuevo usuario en la base de datos."""
    existente = db.query(models.usuario.Usuario).filter(models.usuario.Usuario.correo == usuario.correo).first()
    if existente:
        raise HTTPException(status_code=400, detail="El correo ya está registrado.")

    nuevo = models.usuario.Usuario(
        nombre=usuario.nombre,
        correo=usuario.correo,
        contrasena=usuario.contrasena,
        tipo=usuario.tipo
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def obtener_usuarios(db: Session):
    """Retorna todos los usuarios registrados."""
    return db.query(models.usuario.Usuario).all()


def obtener_usuario_por_id(db: Session, usuario_id: int):
    """Busca un usuario por su ID."""
    usuario = db.query(models.usuario.Usuario).filter(models.usuario.Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    return usuario


def eliminar_usuario(db: Session, usuario_id: int):
    """Elimina un usuario existente."""
    usuario = obtener_usuario_por_id(db, usuario_id)
    db.delete(usuario)
    db.commit()
    return {"mensaje": "Usuario eliminado correctamente"}
