from flask import Flask, Response
from flask_cors import CORS

import json

app = Flask(__name__) # Inicializacion de la aplicación de Flask
CORS(app) # Habilitando la peticion de recursos cruzados

@app.route("/", methods = ["GET"])
def main():
    return Response(json.dumps({"mensaje": "Software Avanzado - Tarea Práctica 5 - 201700965 - José Carlos I Alonzo Colocho"}), status = 200)

if __name__ == "__main__":
    app.run(port = 3000, host = "0.0.0.0")