from flask import Flask, jsonify
from flask_cors import CORS
import requests
from settings import URL, PORT, VOTES_URL, SECURITY_URL
from routes.elections.mesas import mesas_bp
from routes.security.user import user_bp
from routes.elections.partidos import partidos_bp

app = Flask(__name__)
cors = CORS(app)


@app.route("/", methods=["GET"])
def ping():
    return jsonify({
        "message": "pong..."
    })


app.register_blueprint(mesas_bp, url_prefix ="/regisNal")
app.register_blueprint(partidos_bp, url_prefix = "/regisNalP")
app.register_blueprint(user_bp, url_prefix ="/users")

EXCLUDED_URLS = ["/", "/login"]

'''@app.before_request
def middleware():
    if request.path not in EXCLUDED_URLS:
        token = request.headers.get("Authorization")
        if token:
            pass
        else:
            responseObject = {
                "message": "Al parecer no has inicado sesión"
            }
            return make_response(jsonify(responseObject)), 401'''


if __name__ == "__main__":
    app.run(
        debug=True,
        port=PORT,
        host=URL
    )