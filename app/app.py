from flask import Flask, render_template, request, jsonify
import redis
import os
import json
import time

app = Flask(__name__)

redis_client = redis.Redis(
    host=os.environ.get('REDIS_HOST', 'redis'),
    port=int(os.environ.get('REDIS_PORT', 6379)),
    decode_responses=True
)

@app.route('/')
def index():
    anuncios = get_anuncios()
    return render_template('index.html', anuncios=anuncios)

def get_anuncios():
    anuncios = []
    ids = redis_client.lrange('anuncios', 0, -1)
    for aid in ids:
        data = redis_client.get(f'anuncio:{aid}')
        if data:
            anuncios.append(json.loads(data))
    return anuncios

@app.route('/anuncios', methods=['GET'])
def listar():
    return jsonify(get_anuncios())

@app.route('/anuncios', methods=['POST'])
def crear():
    data = request.get_json()
    aid = str(int(time.time() * 1000))
    anuncio = {'id': aid, 'titulo': data['titulo'], 'descripcion': data['descripcion'], 'autor': data['autor']}
    redis_client.set(f'anuncio:{aid}', json.dumps(anuncio))
    redis_client.lpush('anuncios', aid)
    return jsonify({'message': 'Anuncio creado', 'id': aid}), 201

@app.route('/anuncios/<aid>', methods=['DELETE'])
def eliminar(aid):
    redis_client.delete(f'anuncio:{aid}')
    redis_client.lrem('anuncios', 0, aid)
    return jsonify({'message': 'Anuncio eliminado'})

@app.route('/anuncios/<aid>', methods=['PUT'])
def actualizar(aid):
    data = request.get_json()
    anuncio = {'id': aid, 'titulo': data['titulo'], 'descripcion': data['descripcion'], 'autor': data['autor']}
    redis_client.set(f'anuncio:{aid}', json.dumps(anuncio))
    return jsonify({'message': 'Anuncio actualizado'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
