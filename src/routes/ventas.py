from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from src.models.producto import Producto
from src.models.factura import Factura
from src.models.detalles import Detalle
from src.utils.db import db
from datetime import datetime

ventas = Blueprint('ventas', __name__)

@ventas.route('/venta')
def vistaVentas():
    numeroFacturas = len(Factura.query.all())
    clave = f'FACT-{str(numeroFacturas+1).zfill(4)}'
    return render_template('venta/vistaVenta.html', claveSiguiente=clave)

@ventas.route('/generar-venta', methods=['POST'])
def generarVenta():
    if request.method == 'POST':
        clave = request.json['clave']
        detalles = request.json['detalles']
        total = 0
        for detalle in detalles:
            producto = Producto.query.filter_by(idProducto=detalle['id']).first()
            total += int(detalle['cantidad']) * producto.precio
        factura = Factura(
            clave=clave,
            fechaFactura=datetime.now().date(),
            total=total
        )
        for detalle in detalles:
            producto = Producto.query.filter_by(idProducto=detalle['id']).first()
            cantidad = int(detalle['cantidad'])
            subtotal = cantidad * producto.precio
            db.session.add(Detalle(producto=producto, factura=factura, cantidad=cantidad, subtotal=subtotal))
        try:
            db.session.commit()
            return jsonify({'message': 'Factura guardada correctamente'})
        except:
            db.session.rollback()
            return jsonify({'message': 'Ya existe una factura con esa clave'})


