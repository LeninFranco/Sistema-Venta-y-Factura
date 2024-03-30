from flask import Blueprint, redirect, url_for, render_template, request, Response, jsonify
from src.models.factura import Factura
from src.models.producto import Producto
from src.models.detalles import Detalle
from datetime import datetime
from src.utils.db import db

facturas = Blueprint('facturas', __name__)

@facturas.route('/facturas', methods=['GET'])
def vistaListaFacturas():
    facturas = {}
    facturas_r = Factura.query.all()
    for factura in facturas_r:
        detalles = []
        for detalle in factura.detalles_p:
            detalles.append(
                {
                    'clave': detalle.producto.clave,
                    'nombre': detalle.producto.nombre,
                    'precio': detalle.producto.precio,
                    'cantidad': detalle.cantidad,
                    'subtotal': detalle.subtotal
                }
            )
        facturas[factura.clave] = {
            'fecha': datetime.strftime(factura.fechaFactura, '%Y-%m-%d'),
            'detalles': detalles,
            'total': factura.total
        }
    return render_template('factura/listaFactura.html', facturas=facturas)