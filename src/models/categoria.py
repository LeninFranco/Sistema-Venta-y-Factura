from src.utils.db import db
from src.models.producto import Producto

class Categoria(db.Model):
    __tablename__ = 'Categorias'
    idCategoria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(25), nullable=False)
    productos = db.relationship('Producto', backref='categoria')

    def __init__(self, nombre) -> None:
        self.nombre = nombre