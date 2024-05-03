from flask import Flask, request, jsonify
import psycopg2
import uuid
import pandas as pd

app = Flask(__name__)
import psycopg2


@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()  # Obtén el JSON del cuerpo de la petición POST

    # Conéctate a tu base de datos PostgreSQL
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="sqlDB",
        user="postgres",
        password="sharky"
    )
    # print(data)
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