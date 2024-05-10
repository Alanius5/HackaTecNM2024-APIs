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
    conn = psycopg2.connect(
        dbname="defaultdb",
    user="avnadmin",
    password="AVNS__4aIWZKzxammKr4C5Rt",
    host="pg-24c5d2c-hackatec2024.d.aivencloud.com",
    port="22997",
    )
    curr = conn.cursor()
    
    curr.execute("SELECT * FROM Usuario WHERE correo = %s", (data['correo'],))
    if curr.fetchone() is not None:
        return 'Usuario ya existe', 400

    # Insertar el nuevo usuario en la base de datos
    curr.execute(
        "INSERT INTO Usuario (ID_Usuario, Nombre, contrasena, contacto, correo) VALUES (%s, %s, %s, %s, %s)",
        (data['ID_Usuario'], data['Nombre'], data['contrasena'], data['contacto'], data['correo'])
    )
    
    conn.commit()
    conn.close()
    return 'Usuario creado', 201
    
 
    
    

@app.route('/login', methods=['POST'])
def login():
    load_dotenv()
    data = request.get_json()
    API_KEY = os.getenv('URL')
    conn = psycopg2.connect(
        dbname="defaultdb",
    user="avnadmin",
    password="AVNS__4aIWZKzxammKr4C5Rt",
    host="pg-24c5d2c-hackatec2024.d.aivencloud.com",
    port="22997",
    )
    curr = conn.cursor()
    
    curr.execute("SELECT * FROM Usuario WHERE correo = %s", (data['correo'],))

    if curr.fetchone() is None:
        return 'Usuario no valido', 400
    
    conn.close()
    return 'Usuario valido', 201
    


@app.route('/upload', methods=['POST'])
def upload():
    load_dotenv()
    data = request.get_json()
    API_KEY = os.getenv('URL')
    conn = psycopg2.connect(
        dbname="defaultdb",
    user="avnadmin",
    password="AVNS__4aIWZKzxammKr4C5Rt",
    host="pg-24c5d2c-hackatec2024.d.aivencloud.com",
    port="22997",
    )
    curr = conn.cursor()
 
    curr.execute(
        "INSERT INTO Usuario (ID_Usuario, Nombre, contrasena, contacto) VALUES (%s, %s, %s, %s)",
        (data['ID_Usuario'], data['Nombre'], data['contrasena'], data['contacto'])
    )
 
    conn.commit()
    conn.close()

    return 'JSON subido a la base de datos con éxito!', 200


@app.route('/upload/miembro_info', methods=['POST'])
def upload_miembro_info():
    load_dotenv()
    data = request.get_json()
    conn = psycopg2.connect(
        dbname="defaultdb",
    user="avnadmin",
    password="AVNS__4aIWZKzxammKr4C5Rt",
    host="pg-24c5d2c-hackatec2024.d.aivencloud.com",
    port="22997",
    )
    curr = conn.cursor()

    try:
        curr.execute(
            "INSERT INTO MiembroInfo (ID_Miembro, edad, estatura, peso, temperatura, updated_at) VALUES (%s, %s, %s, %s, %s, %s)",
            (data['ID_Miembro'], data['edad'], data['estatura'], data['peso'], data['temperatura'], data['updated_at'])
        )
        conn.commit()
        conn.close()
        return 'Datos subidos a la base de datos con éxito!', 200
    except psycopg2.Error as e:
        conn.rollback()
        conn.close()
        return f'Error al subir datos a la base de datos: {e}', 500

if __name__ == '__main__':
    
    app.run(debug=True)