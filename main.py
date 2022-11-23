from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import requests
from settings import URL, PORT
from routes.elections.mesas import mesas_bp
from routes.security.user import user_bp
from routes.elections.partidos import partidos_bp
from routes.elections.candidato import candidato_bp
from routes.security.role import role_bp
from routes.security.permission import permission_bp
from routes.security.permissionrole import permissionrole_bp
from routes.elections.results import results_bp

app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(mesas_bp, url_prefix ="/regisNal")
app.register_blueprint(partidos_bp, url_prefix = "/regisNalP")
app.register_blueprint(user_bp, url_prefix ="/users")
app.register_blueprint(candidato_bp, url_prefix= "/regisNalC")
app.register_blueprint(role_bp, url_prefix="/roles")
app.register_blueprint(permission_bp, url_prefix="/permissions")
app.register_blueprint(permissionrole_bp, url_prefix="/permissions-roles")
app.register_blueprint(results_bp, url_prefix="/regisNalR")

EXCLUDED_URLS = ["/", "/login"]

@app.before_request
def middleware():
    if request.path not in EXCLUDED_URLS:
        token = request.headers.get("Authorization")
        if token:
            response = validate_permissions(token, clean_path(request.path), request.method)
            if response.status_code != 200:
                if response.status_code != 200:
                    return jsonify(response.json()), response.status_code


def validate_permissions(token, url, method):
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    response = requests.post(
        url=f"{SECURITY_URL}/permissions-roles/verify",
        headers=headers,
        json={
            "url": url,
            "method": method
        }
    )
    return response


def clean_path(path):
    parts = path.split("/")
    return "/" + parts[1]


if __name__ == "__main__":
    app.run(
        debug=True,
        port=PORT,
        host=URL
    )
    