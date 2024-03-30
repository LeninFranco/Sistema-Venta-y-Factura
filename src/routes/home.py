from flask import Blueprint, render_template
from src.models.categoria import Categoria
from src.models.factura import Factura
from src.utils.db import db

home = Blueprint('home', __name__)

@home.route('/')
def vistaHome():
    categorias = []
    cantidad = []
    for categoria in Categoria.query.all():
        categorias.append(categoria.nombre)
        cantidad.append(len(categoria.productos))
    facturas = []
    balance = 0
    for factura in Factura.query.all():
        facturas.append((factura.clave, factura.total))
        balance += factura.total
    return render_template('home/home.html', grafica=(categorias, cantidad), facturas=facturas, balance=balance)