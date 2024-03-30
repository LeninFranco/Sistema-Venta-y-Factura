from src.utils.db import db
from uuid import uuid4

def getDefaultID() -> str:
    return uuid4().hex

class Producto(db.Model):
    __tablename__ = 'Productos'
    idProducto = db.Column(db.String(32), primary_key=True, default=getDefaultID)
    clave = db.Column(db.String(100), nullable=False, unique=True)
    nombre = db.Column(db.String(30), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    idCategoria = db.Column(db.Integer, db.ForeignKey('Categorias.idCategoria'), nullable=False)

    def __init__(self, clave, nombre, stock, precio, idCategoria) -> None:
        self.clave = clave
        self.nombre = nombre
        self.stock = stock
        self.precio = precio
        self.idCategoria = idCategoria