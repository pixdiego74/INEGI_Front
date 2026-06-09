from flask import Flask, render_template, request, jsonify
from jinja2 import ChoiceLoader, FileSystemLoader
import mock_data

app = Flask(__name__)

app.jinja_loader = ChoiceLoader([
    FileSystemLoader("components"),
    FileSystemLoader("templates")
])

def buscar_usuario_por_id(id_usuario):
    """Busca un usuario en mock_data por su ID"""
    for usuario in mock_data.mock_usuarios:
        if usuario["id"] == id_usuario:
            return usuario
    return None

@app.route("/", methods=["GET", "POST"])
def index():
    usuario_encontrado = None
    
    if request.method == "POST":
        id_usuario = request.form.get('id-input')
        if id_usuario:
            try:
                id_int = int(id_usuario)
                usuario_encontrado = buscar_usuario_por_id(id_int)
            except ValueError:
                usuario_encontrado = None
    return render_template("index.html", usuario=usuario_encontrado)

@app.route("/<int:id>")
def mostrar_id(id):
    id_str = str(id).zfill(4)

    return render_template('index.html', id=id_str)
      
@app.route("/verificar", methods=['POST'])
def verificar():
    id_usuario = request.form.get('id-input')
    usuario = None
    
    if id_usuario:
        try:
            id_int = int(id_usuario)
            usuario = buscar_usuario_por_id(id_int)
        except ValueError:
            pass
    return render_template("index.html", usuario=usuario)

if __name__ == '__main__':
    app.run(debug=True)

#Agregar App shell para carga mas rapida luego
#Posible localstorage para lo mismo????????