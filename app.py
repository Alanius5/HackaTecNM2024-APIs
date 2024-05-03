from flask import Flask, request, jsonify
import psycopg2
import uuid

app = Flask(__name__)
import psycopg2

# Conectarse a la base de datos
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="bank",
    user="root",
    password="sharky"
)

# Crear un cursor
cursor = conn.cursor()

# Ejecutar una consulta



# Cerrar la conexión
conn.close()



@app.route('/upload', methods=['POST'])
def consultar():
    pass

# @app.route('/upload', methods=['POST'])
# def predict():
#     # Obtener los datos de la solicitud POST
#     data = request.get_json()
#     print(f"Datos recibidos: {data}")

#     nreg = str(uuid.uuid4())

#     # Convertir los datos a un DataFrame de Pandas
#     df = pd.DataFrame([data])

#     # Realizar la conversión de valores para las columnas específicas
#     columns_to_convert = ['Sexo', 'Edad']
#     for column in df.columns:
#         if column not in columns_to_convert:
#             df[column] = df[column].map({1: False, 2: True})

#     # Generar una predicción usando el modelo cargado
#     prediction = model.predict(df)
#     r.hset(nreg, "sexo", data['Sexo'])
#     r.hset(nreg, "edad", data['Edad'])
#     r.hset(nreg, "fumador", data['Fumador'])
#     r.hset(nreg, "dedos_amarillos", data['dedos amarillos'])
#     r.hset(nreg, "ansiedad", data['Ansiedad'])
#     r.hset(nreg, "presion_de_grupo", data['presion de grupo'])
#     r.hset(nreg, "enfermedad_cronica", data['enfermedad cronica'])
#     r.hset(nreg, "fatiga", data['fatiga'])
#     r.hset(nreg, "alergia", data['Alergia'])
#     r.hset(nreg, "sibilancias", data['Sibilancias'])
#     r.hset(nreg, "consumo_alcohol", data['Consumo Alcohol'])
#     r.hset(nreg, "tos", data['Tos'])
#     r.hset(nreg, "dificultad_respirar", data['Dificultad respirar'])
#     r.hset(nreg, "dificultad_tragar", data['Dificultad tragar'])
#     r.hset(nreg, "dolor_en_pecho", data['Dolor en pecho'])
#     r.hset(nreg, "cancer_pulmon", int(prediction[0]))

#     # Retornar la predicción como JSON
#     return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    
    app.run(debug=True)