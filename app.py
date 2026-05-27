from flask import Flask, render_template, request, jsonify
from jinja2 import ChoiceLoader, FileSystemLoader
import mock_data

app = Flask(__name__)

app.jinja_loader = ChoiceLoader([
    FileSystemLoader("components"),
    FileSystemLoader("templates")
])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/verificar")
def verificar():
    identificacion = request.
    #No se como seguirle aqui XDDDDDDDDDD

if __name__ == '__main__':
    app.run(debug=True)