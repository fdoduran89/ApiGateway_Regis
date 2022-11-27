from flask import request, jsonify, Blueprint
import requests
from settings import VOTES_URL

partidos_bp = Blueprint("partidos_blueprint", __name__)

@partidos_bp.route("", methods=["POST"])
def create_party():
    body = request.get_json()
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(
        url=f"{VOTES_URL}/regisNalP",  # localhost:5000/parties (ms votaciones)
        json=body,
        headers=headers
    )
    if response.status_code == 201:
        return jsonify(response.json()), 201
    else:
        return jsonify({
            "message": "Hubo un error al crear el partido"
        }), 500


@partidos_bp.route("", methods=["GET"])
def partidos():
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/regisNalP",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "message": "Hubo un error al obtener la lista de partidos"
        }), 500

@partidos_bp.route("/<string:nombre_partido>", methods=["GET"])
def get_partido(nombre_partido):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/regisNalP/{nombre_partido}",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "message": "Hubo un error al obtener el partido"
        }), 500    

@partidos_bp.route("/id/<string:id_partido>", methods=["GET"])
def get_partido_id(id_partido):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/regisNalP/id/{id_partido}",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "message": "Hubo un error al obtener el partido"
        }), 500
    
@partidos_bp.route("/<string:nombre_partido>", methods=["DELETE"])
def delete_partido(nombre_partido):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.delete(
        url=f"{VOTES_URL}/regisNalP/{nombre_partido}",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "message": "Hubo un error al obtener la información del partido"
        }), 500

@partidos_bp.route("/<string:nombre_partido>", methods=["PUT"])
def update_partido(nombre_partido):
    body = request.get_json()
    headers = { "Content-Type": "application/json"}
    response = requests.put( url=f"{VOTES_URL}/regisNalP/{nombre_partido}",  # localhost:5000/parties (ms votaciones)
        json=body,
        headers=headers)
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al actualizar el partido"
        }), 500
    else:
        return jsonify(response.json()), response.status_code