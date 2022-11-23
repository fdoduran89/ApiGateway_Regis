from flask import request, jsonify, Blueprint
import requests
from settings import VOTES_URL

results_bp = Blueprint("results_blueprint", __name__)

# Resultados todos sin filtro
@results_bp.route("", methods=["GET"])
def regisNalR():
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/regisNalR",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:  # status_code == 500
        return jsonify({
            "message": "Hubo un error al obtener la lista de resultados"
        }), 500

# Resultado por id de resultado
@results_bp.route("/<id>", methods=["GET"])
def regisNalR_id(id):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/regisNalR/{id}",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "message": "Hubo un error al obtener el resultado"
        }), 500

# Cargar resultados de votacion
@results_bp.route("", methods=["POST"])
def insert_resultado():
    body = request.get_json()
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(
        url=f"{VOTES_URL}/regisNalR",
        json=body,
        headers=headers
    )
    if response.status_code == 201:
        return jsonify(response.json()), 201
    else:
        return jsonify({
            "message": "Hubo un error al crear el resultado"
        }), 500

# Modificar resultados por id de resultado
@results_bp.route("/<id>", methods=["PUT"])
def update_resultado(id):
    body = request.get_json()
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.put(
        url=f"{VOTES_URL}/regisNalR/{id}",
        json=body,
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "message": "Hubo un error al actualizar el resultado"
        }), 500

# Eliminar resultados por id de resultado
@results_bp.route("/<id>", methods=["DELETE"])
def delete_resultado(id):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.delete(
        url=f"{VOTES_URL}/regisNalR/{id}",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "message": "Hubo un error al eliminar el resultado"
        }), 500

# Reporte Votos por Candidato Partido Descendente
@results_bp.route("/candidato_partido_votos_desc", methods=["GET"])
def candidato_partido_votos_desc():
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/regisNalR/candidato_partido_votos_desc",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "message": "Hubo un error al obtener la lista de resultados"
        }), 500

# Reporte Votos por Candidato Mesa y Partido
@results_bp.route("/candidato_mesa_partido_votos", methods=["GET"])
def candidato_mesa_partido_votos():
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/regisNalR/candidato_mesa_partido_votos",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "message": "Hubo un error al obtener la lista de resultados"
        }), 500

# Reporte Votos por Mesa
@results_bp.route("/mesa_votos", methods=["GET"])
def mesa_votos():
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/regisNalR/mesa_votos",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "message": "Hubo un error al obtener la lista de resultados"
        }), 500

# Reporte Votos por Partido
@results_bp.route("/partido_votos", methods=["GET"])
def partido_votos():
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/regisNalR/partido_votos",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "message": "Hubo un error al obtener la lista de resultados"
        }), 500

# Reporte Votos por Partido Y Mesa
@results_bp.route("/partido_mesa_votos", methods=["GET"])
def partido_mesa_votos():
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/regisNalR/partido_mesa_votos",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "message": "Hubo un error al obtener la lista de resultados"
        }), 500

# Reporte porcentaje general por partido
@results_bp.route("/percentage_by_partido", methods=["GET"])
def percentage_by_partido():
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/regisNalR/percentage_by_partido",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "message": "Hubo un error al obtener la lista de resultados"
        }), 500

# Reporte por id de mesa y id de candidato
@results_bp.route("/mesa/<id_mesa>/candidato/<id_candidato>", methods=["GET"])
def find_resultado_by_mesa_and_candidato(id_mesa, id_candidato):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/regisNalR/mesa/{id_mesa}/candidato/{id_candidato}",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "message": "Hubo un error al obtener la lista de resultados"
        }), 500
