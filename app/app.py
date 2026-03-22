from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD']
    )
    return conn

@app.route('/tareas', methods=['GET'])
def get_tareas():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM tareas;')
    tareas = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(tareas)

@app.route('/tareas', methods=['POST'])
def add_tarea():
    nueva_tarea = request.json['descripcion']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO tareas (descripcion) VALUES (%s)', (nueva_tarea,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"mensaje": "Tarea creada"}), 201

if __name__ == '__main__':
    # Ejecutamos en el puerto 5000
    app.run(host='0.0.0.0', port=5000)