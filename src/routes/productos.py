from flask import Blueprint, redirect, url_for, render_template, request, Response, json
from src.models.categoria import Categoria
from src.models.producto import Producto
from src.utils.db import db

productos = Blueprint('productos', __name__)

@productos.route('/productos')
def vistaProductos():
    return render_template('productos/listaProductos.html', productos=Producto.query.all(), categorias=Categoria.query.all())

@productos.route('/get-productos', methods=['GET'])
def obtenerListaProductos():
    productos = []
    for producto in Producto.query.all():
        productos.append(producto.nombre)
    return Response(json.dumps(productos), mimetype='application/json')

@productos.route('/get-detail-producto', methods=['POST'])
def obtenerDetalleProducto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cantidad = int(request.form['cantidad'])
        producto = Producto.query.filter_by(nombre=nombre).first()
        if producto:
            response = {
                'id': producto.idProducto,
                'clave': producto.clave,
                'nombre': producto.nombre,
                'stock': producto.stock,
                'precio': producto.precio,
                'cantidad': cantidad,
                'subtotal': producto.precio * cantidad
            }   
            return Response(json.dumps(response), mimetype='application/json')
        return Response(json.dumps({'error': 'No se encontro el producto'}), mimetype='application/json')


@productos.route('/add-producto', methods=['POST'])
def addProducto():
    if request.method == 'POST':
        clave = request.form['clave']
        nombre = request.form['nombre']
        stock = int(request.form['stock'])
        precio = float(request.form['precio'])
        idCategoria = int(request.form['categoria'])
        p = Producto(
            clave=clave,
            nombre=nombre,
            stock=stock,
            precio=precio,
            idCategoria=idCategoria
        )
        try:
            db.session.add(p)
            db.session.commit()
            return redirect(url_for('productos.vistaProductos', save=True))
        except:
            db.session.rollback()
            return redirect(url_for('productos.vistaProductos', save=False))

@productos.route('/update-producto', methods=['POST'])
def updateProducto():
    if request.method == 'POST':
        idProducto = request.form['idProducto']
        clave = request.form['clave']
        nombre = request.form['nombre']
        stock = int(request.form['stock'])
        precio = float(request.form['precio'])
        idCategoria = int(request.form['categoria'])
        p = Producto.query.filter_by(idProducto=idProducto).first()
        try:
            if not p.clave == clave:
                p.clave = clave
            p.nombre = nombre
            p.stock = stock
            p.precio = precio
            p.idCategoria = idCategoria
            db.session.commit()
            return redirect(url_for('productos.vistaProductos', update=True))
        except:
            db.session.rollback()
            return redirect(url_for('productos.vistaProductos', update=False))