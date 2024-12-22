from flask import Blueprint, jsonify

bp = Blueprint('preferences', __name__)

@bp.route('/', methods=['GET'])
def get_preferences():
    return jsonify({"message": "PREFERENCES YIPPEE!"})