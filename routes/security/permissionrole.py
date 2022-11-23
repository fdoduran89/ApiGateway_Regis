from flask import request, jsonify, Blueprint
import requests
from settings import SECURITY_URL

permissionrole_bp = Blueprint("permissionrole_blueprint",__name__)

@permissionrole_bp.route("/roles/<string:roleid>/permissions/<string:permissionid>", methods=["POST"])
def create_permissionrole():
    body = request.get_json()
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(
        url=f"{SECURITY_URL}/permissions-roles",
        json=body,
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al crear el permiso-rol"
        }), 500
    else:
        return jsonify(response.json()), response.status_code

@permissionrole_bp.route("", methods=["GET"])
def permissionroles():
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{SECURITY_URL}/permissions-roles",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al obtener la información del permiso-rol"
        }), 500
    else:
        return jsonify(response.json()), response.status_code

@permissionrole_bp.route("/<string:permissionrole_id>", methods=["GET"])
def rpermissionrole(permissionrole_id):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{SECURITY_URL}/permissions-roles/{permissionrole_id}",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({
            "message": "Hubo un error al obtener la información del permiso-rol"
        }), 500

@permissionrole_bp.route("/<string:permissionrole_id>", methods=["DELETE"])
def delete_permissionrole(permissionrole_id):
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.delete(
        url=f"{SECURITY_URL}/permissions-roles/{permissionrole_id}",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al borrar el permiso-rol"
        }), 500
    else:
        return jsonify(response.json()), response.status_code

@permissionrole_bp.route("/<string:permissionrole_id>/role/<string:role_id>", methods=["PUT"])
def change_permissionrole(permissionrole_id, role_id):
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.delete(
        url=f"{SECURITY_URL}/permissions-roles/{permissionrole_id}",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al borrar el permiso-rol"
        }), 500
    else:
        return jsonify(response.json()), response.status_code