from flask import request, jsonify, Blueprint
import requests
from settings import SECURITY_URL

user_bp = Blueprint("user_blueprint", __name__)

@user_bp.route("/<string:roleid>", methods=["POST"])
def create_user(roleid):
    body = request.get_json()
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.post(
        url=f"{SECURITY_URL}/users?roleId={roleid}",
        json=body,
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al crear usuario"
        }), 500
    else:
        return jsonify(response.json()), response.status_code

@user_bp.route("", methods=["GET"])
def users():
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.get(
        url=f"{SECURITY_URL}/users",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al obtener la información de los usuarios"
        }), 500
    else:
        return jsonify(response.json()), response.status_code

@user_bp.route("/<string:user_id>", methods=["GET"])
def user(user_id):
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.get(
        url=f"{SECURITY_URL}/users/{user_id}",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "message": "Hubo un error al obtener la información del usuario"
        }), 500

@user_bp.route("/<string:userid>", methods=["DELETE"])
def delete_user(userid):
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.delete(
        url=f"{SECURITY_URL}/users/{userid}",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al borrar usuario"
        }), 500
    else:
        return jsonify(response.json()), response.status_code


@user_bp.route("/<string:userId>", methods=["PUT"])
def update_user(userId):
    body = request.get_json()
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.put(
        url=f"{SECURITY_URL}/users/{userId}",
        json=body,
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al modificar el usuario"
        }), 500
    else:
        return jsonify(response.json()), response.status_code


