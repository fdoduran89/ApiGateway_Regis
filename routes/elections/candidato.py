from flask import request, jsonify, Blueprint
import requests
from settings import VOTES_URL

candidato_bp = Blueprint("candidato_blueprint", __name__)

@candidato_bp.route("", methods=["GET"])
def candidatos():
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/regisNalC",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:  # status_code == 500
        return jsonify({
            "message": "Hubo un error al obtener la lista de candidatos"
        }), 500

@candidato_bp.route("", methods=["POST"])
def create_candidato():
    body = request.get_json()
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(
        url=f"{VOTES_URL}/regisNalC",
        json=body,
        headers=headers
    )
    if response.status_code == 201:
        return jsonify(response.json()), 201
    else:  # status_code == 500
        return jsonify({
            "message": "Hubo un error al crear el candidato"
        }), 500


@candidato_bp.route("/<string:candidatoId>", methods=["DELETE"])
def delete_candidato(candidatoId):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.delete(
        url=f"{VOTES_URL}/regisNalC/{candidatoId}",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al borrar el candidato"
        }), 500
    else:
        return jsonify(response.json()), response.status_code

@candidato_bp.route("/<string:candidatoId>", methods=["PUT"])
def update_candidato(candidatoId):
    body = request.get_json()
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.put(
        url=f"{VOTES_URL}/regisNalC/{candidatoId}",
        json=body,
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "message": "Hubo un error al actualizar el candidato"
        }), 500
