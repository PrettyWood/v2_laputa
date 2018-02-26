from flask import Blueprint, current_app, g, jsonify

front_config = Blueprint('front_config', __name__)


@front_config.route('/front-config')
def get_front_config():
    last_front_config = current_app.mongo_client.retrieve_last_config(
        g.small_app_id, 'front_config', stage=g.stage)
    return jsonify(last_front_config)
