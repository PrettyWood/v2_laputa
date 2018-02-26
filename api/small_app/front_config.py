from flask import Blueprint, current_app, jsonify

front_config = Blueprint('front_config', __name__)


@front_config.route('/front-config')
def get_front_config():
    last_front_config = current_app.mongo.retrieve_last_config('front_config')
    return jsonify(last_front_config)
