from passlib.context import CryptContext

# Configuramos el algoritmo de encriptación (bcrypt)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def encriptar_contrasena(contrasena: str) -> str:
    """
    Recibe una contraseña en texto plano y devuelve su versión encriptada.
    """
    return pwd_context.hash(contrasena)

def verificar_contrasena(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica si una contraseña coincide con su versión encriptada.
    """
    return pwd_context.verify(plain_password, hashed_password)
