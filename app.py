from flask import Flask
from src.utils.db import db
from src.routes.home import home
from src.routes.productos import productos
from src.routes.ventas import ventas
from src.routes.facturas import facturas
import os
import secrets

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder='src/templates', static_folder='src/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'src', 'database', 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = secrets.token_hex(16)

app.register_blueprint(home)
app.register_blueprint(productos)
app.register_blueprint(ventas)
app.register_blueprint(facturas)

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)