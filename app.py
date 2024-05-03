from flask import Flask, request, jsonify
import psycopg2
import uuid
import pandas as pd
import os
from dotenv import load_dotenv

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup():
    load_dotenv()
    data = request.get_json()
    API_KEY = os.getenv('URL')
    conn = psycopg2.connect(API_KEY)
    curr = conn.cursor()
    curr.execute(
        "INSERT INTO Usuario (ID_Usuario, Nombre, contrasena, contacto) VALUES (%s, %s, %s, %s)",
        (data['ID_Usuario'], data['Nombre'], data['contrasena'], data['contacto'])
    )
 
    conn.commit()
    conn.close()

    return 'JSON subido a la base de datos con éxito!', 200

@app.route('/upload', methods=['POST'])
def upload():
    load_dotenv()
    data = request.get_json()
    API_KEY = os.getenv('URL')
    conn = psycopg2.connect(API_KEY)
    curr = conn.cursor()
 
    curr.execute(
        "INSERT INTO Usuario (ID_Usuario, Nombre, contrasena, contacto) VALUES (%s, %s, %s, %s)",
        (data['ID_Usuario'], data['Nombre'], data['contrasena'], data['contacto'])
    )
 
    conn.commit()
    conn.close()

    return 'JSON subido a la base de datos con éxito!', 200


if __name__ == '__main__':
    
    app.run(debug=True)