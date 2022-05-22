from flask import Flask, jsonify, request, render_template,redirect,session
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_claims
)
import timedelta
from src.controllers.customerController import customerController
import os
import hashlib


app = Flask(__name__)
app.secret_key = "any random string"
app.config['JWT_SECRET_KEY'] = 'cambiar_no_olvidar' 
app.config["IMAGE_UPLOADS"] = "/tmp"
jwt = JWTManager(app)

# Read leer listar obtener  -> GET

@app.route('/customer', methods=['GET'])
def get_customers():
    return customerController().get_customers()


# CREAR INSERTAR Insert   -> POST request

@app.route('/customer', methods=['POST'])
def add_customer():
    return customerController().add_customer(request)

# MODIFICAR UPDATE ACTUALIZAR    -> PUT request

@app.route('/customer', methods=['PUT'])
def update_customer():
    return customerController().update_customer(request)

# Eliminar delete    -> DELETE
# url/user/

@app.route('/customer/<index>', methods=['DELETE'])
#@jwt_required
def delete_customer(index):
    return customerController().delete_customer(index)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

