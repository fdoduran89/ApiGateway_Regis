from flask import request, jsonify, Blueprint
import requests
from settings import VOTES_URL

mesas_bp = Blueprint("mesas_blueprint", __name__)

@mesas_bp.route("", methods=["POST"])
def create_party():
    body = request.get_json()
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(
        url=f"{VOTES_URL}/regisNal",  # localhost:5000/parties (ms votaciones)
        json=body,
        headers=headers
    )
    if response.status_code == 201:
        return jsonify(response.json()), 201
    else:  # status_code == 500
        return jsonify({
            "message": "Hubo un error al crear la mesa"
        }), 500


@mesas_bp.route("", methods=["GET"])
def mesas():
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/regisNal",  # localhost:5000/mesas (ms votaciones)
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:  # status_code == 500
        return jsonify({
            "message": "Hubo un error al obtener la lista de mesas"
        }), 500

@mesas_bp.route("/<string:mesaId>", methods=["DELETE"])
def delete_mesa(mesaId):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.delete(
        url=f"{VOTES_URL}/regisNal/{mesaId}",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al borrar la mesa"
        }), 500
    else:
        return jsonify(response.json()), response.status_code

@mesas_bp.route("/<string:mesaId>", methods=["PUT"])
def update_partido(mesaId):
    body = request.get_json()
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.put(
        url=f"{VOTES_URL}/regisNal/{mesaId}",
        json=body,
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al actualizar la mesa"
        }), 500
    else:
        return jsonify(response.json()), response.status_code