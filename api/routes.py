from flask import g, jsonify, request


def add_routes(app):
    @app.before_request
    def before_request():
        g.small_app_id = request.view_args.pop('small_app_id', None)
        g.stage = request.args.get('stage')
        g.db = app.mongo_client.get_db(g.small_app_id)
        app.logger.debug(f'SMALL APP: {g.small_app_id}, STAGE: {g.stage}')

    # GENERAL ROUTES
    @app.route('/')
    def index():
        return 'Main'

    @app.route('/small-apps')
    def get_small_apps():
        all_small_apps = [x for x in g.db.small_app.find({}, {'_id': 0})]
        return jsonify(all_small_apps)

    # SMALL APP ROUTES
    from .small_app.front_config import front_config
    from .small_app.etl_config import etl_config

    app.register_blueprint(front_config, url_prefix='/<small_app_id>')
    app.register_blueprint(etl_config, url_prefix='/<small_app_id>')
