# iam/interfaces/services.py


from flask import Blueprint, request, jsonify
from iam.application.services import AuthApplicationService


iam_api = Blueprint("iam_api", __name__)

auth_app_service = AuthApplicationService()

def authenticate_request():

    if not request.is_json:
        return jsonify({"error": "Invalid request: Missing JSON body."}), 400

    device_id = request.json.get("device_id")
    api_key = request.headers.get("X-API-Key")

    if not device_id or not api_key:
        return jsonify({"error": "Authentication failed: Missing device_id in body or X-API-Key in headers."}), 401

    if not auth_app_service.authenticate(device_id, api_key):
        return jsonify({"error": "Authentication failed: Invalid device_id or API key."}), 401

    return None