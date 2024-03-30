from src.utils.db import db
from src.models.producto import Producto
from src.models.factura import Factura

class Detalle(db.Model):
    __tablename__ = 'Detalles'
    idDetalle = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idFactura = db.Column(db.String(32), db.ForeignKey('Facturas.idFactura'))
    idProducto = db.Column(db.String(32), db.ForeignKey('Productos.idProducto'))
    factura = db.relationship('Factura', backref='detalles_p')
    producto = db.relationship('Producto', backref='detalles_f')
    cantidad = db.Column(db.Integer, nullable=False)
    subtotal = db.Column(db.Float, nullable=False)