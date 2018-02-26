from flask import Blueprint, current_app, g, jsonify

etl_config = Blueprint('etl_config', __name__)


@etl_config.route('/etl-config')
def get_etl_config():
    last_etl_config = current_app.mongo_client.retrieve_last_config(
        g.small_app_id, 'etl_config', stage=g.stage)
    return jsonify(last_etl_config)
