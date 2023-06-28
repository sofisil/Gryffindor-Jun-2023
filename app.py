from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)



class Datos_veterinarias(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      nombre = db.Column(db.String, nullable=False)
      ciudad = db.Column(db.String, nullable=False)
      direccion = db.Column(db.String, nullable=False)
      contacto = db.Column(db.Integer, nullable=False)
      especialidades = db.Column(db.String, nullable=True)
      estudios = db.Column(db.String, nullable=True)

      def __init__(self, nombre, ciudad, direccion, contacto, especialidades, estudios):
           self.nombre = nombre
           self.ciudad = ciudad
           self.contacto = contacto
           self.direccion = direccion
           self.especialidades = especialidades
           self.estudios = estudios

class Datos_refugios(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      nombre = db.Column(db.String, nullable=False)
      direccion = db.Column(db.String, nullable=False)
      ciudad = db.Column(db.String, nullable=False)
      contacto = db.Column(db.Integer, nullable=False)
      animales = db.Column(db.Integer, nullable=True)
      cantidad = db.Column(db.Integer, nullable=True)
      datos = db.Column(db.String, nullable=True)

      def __init__(self, nombre, direccion, ciudad, contacto, animales, cantidad, datos):
           self.nombre = nombre
           self.direccion = direccion
           self.ciudad = ciudad
           self.contacto = contacto
           self.animales = animales
           self.cantidad = cantidad
           self.datos = datos

class Datos_hogares(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      nombre = db.Column(db.String, nullable=False)
      ciudad = db.Column(db.String, nullable=False)
      direccion = db.Column(db.String, nullable=False)
      contacto = db.Column(db.Integer, nullable=False)
      animales = db.Column(db.String, nullable=True)
      datos = db.Column(db.String, nullable=True)

      def __init__(self, nombre, ciudad, direccion, contacto, animales, datos):
           self.nombre = nombre
           self.ciudad = ciudad
           self.direccion = direccion
           self.contacto = contacto
           self.animales = animales
           self.datos = datos

#Rutas
@app.route('/')
def index():
    return render_template('index.html')






@app.route("/cargar_datos_veterinarias", methods=["GET", "POST"])
def cargar_datos_veterinarias():
    if request.method == "POST":
        nombre = request.form["nombre"]
        ciudad = request.form["ciudad"]
        direccion = request.form["direccion"]
        contacto = request.form["contacto"]
        especialidades = request.form["especialidades"]
        estudios = request.form["estudios"]

        nueva_veterinaria = Datos_veterinarias(nombre, ciudad, direccion, contacto, especialidades, estudios)
        db.session.add(nueva_veterinaria)
        db.session.commit()
        return ("Datos cargados correctamente")
    return render_template('cargar_datos_veterinarias.html')

@app.route("/cargar_datos_refugios", methods=["GET", "POST"])
def cargar_datos_refugios():
    if request.method == "POST":
        nombre = request.form["nombre"]
        direccion = request.form["direccion"]
        ciudad = request.form["ciudad"]
        contacto = request.form["contacto"]
        animales = request.form["animales"]
        datos = request.form["datos"]
        cantidad = request.form["cantidad"]

        nuevo_refugio = Datos_refugios(nombre, direccion, ciudad, contacto, animales, cantidad, datos)
        db.session.add(nuevo_refugio)
        db.session.commit()
        return ("Datos cargados correctamente")
    return render_template('cargar_datos_refugios.html')

@app.route("/cargar_datos_hogares", methods=["GET", "POST"])
def cargar_datos_hogares():
    if request.method == "POST":
        nombre = request.form["nombre"]
        ciudad = request.form["ciudad"]
        direccion = request.form["direccion"]
        contacto = request.form["contacto"]
        animales = request.form["animales"]
        datos = request.form["datos"]

        nuevo_hogar = Datos_hogares(nombre, ciudad, direccion, contacto, animales, datos)
        db.session.add(nuevo_hogar)
        db.session.commit()
        return ("Datos cargados correctamente")
    return render_template('cargar_datos_hogares.html')




@app.route("/lista_hogares")
def lista_hogares(): 
    hogares = Datos_hogares.query.all()
    return render_template('lista_hogares.html', hogares=hogares)

@app.route("/lista_veterinarias")
def lista_veterinarias(): 
    veterinarias = Datos_veterinarias.query.all()
    return render_template('lista_veterinarias.html', veterinarias=veterinarias)

@app.route("/lista_refugios")
def lista_refugios(): 
    refugios = Datos_refugios.query.all()
    return render_template('lista_refugios.html', refugios=refugios)

@app.route('/campanas')
def campanas(): 
    return render_template('campanas.html')

#CREAMOS LA BASE
with app.app_context():
    db.create_all(bind_key='__all__')

if __name__ == "__main":
    app.run(debug=True, port=5000)