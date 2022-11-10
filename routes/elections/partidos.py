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
    else:  # status_code == 500
        return jsonify({
            "message": "Hubo un error al crear la mesa"
        }), 500


@partidos_bp.route("", methods=["GET"])
def partidos():
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/regisNalP",  # localhost:5000/partidos
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:  # status_code == 500
        return jsonify({
            "message": "Hubo un error al obtener la lista de partidos"
        }), 500