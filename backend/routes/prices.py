from flask import Blueprint, jsonify

bp = Blueprint('prices', __name__)

@bp.route('/', methods=['GET'])
def get_prices():
    return jsonify({"message": "PRICES YIPPEE!"})