from flask import Blueprint, jsonify

api = Blueprint('api', __name__, url_prefix='/api/v1')

#@api.route('/health')
@api.route('/health', methods=['POST'])
def health():

    return jsonify({"status": "ok"})