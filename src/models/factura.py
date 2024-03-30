from src.utils.db import db
from uuid import uuid4

def getDefaultID() -> str:
    return uuid4().hex

class Factura(db.Model):
    __tablename__ = 'Facturas'
    idFactura = db.Column(db.String(32), primary_key=True, default=getDefaultID)
    clave = db.Column(db.String(100), nullable=False, unique=True)
    fechaFactura = db.Column(db.Date, nullable=False)
    total = db.Column(db.Float, nullable=False)

    def __init__(self, clave, fechaFactura, total) -> None:
        self.clave = clave
        self.fechaFactura = fechaFactura
        self.total = total