from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os
import logging

# Cargar variables de entorno desde .env
load_dotenv()

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    filename='app.log',
    format='%(asctime)s %(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

# Configuración básica de la app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "dev-secret")

# Simular base de datos con usuario seguro (contraseña hasheada)
users = {
    "admin": generate_password_hash("1234")
}

@app.route("/")
def home():
    logger.info("Página principal visitada")
    return "Aplicación segura funcionando correctamente con HTTPS y buenas prácticas."

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        logger.warning("Intento de login con datos incompletos")
        return jsonify({"message": "Faltan credenciales"}), 400

    stored = users.get(username)
    if stored and check_password_hash(stored, password):
        logger.info(f"Inicio de sesión exitoso: {username}")
        return jsonify({"message": "Acceso concedido"}), 200
    else:
        logger.warning(f"Intento fallido de inicio de sesión: {username}")
        return jsonify({"message": "Credenciales inválidas"}), 401

if __name__ == "__main__":
    app.run(debug=True)
