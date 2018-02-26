from flask import Blueprint, current_app, jsonify

etl_config = Blueprint('etl_config', __name__)


@etl_config.route('/etl-config')
def get_front_config():
    last_etl_config = current_app.mongo.retrieve_last_config('etl_config')
    return jsonify(last_etl_config)
