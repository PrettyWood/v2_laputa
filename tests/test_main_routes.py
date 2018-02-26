import json
from copy import deepcopy


def test_index(client):
    res = client.get('/')
    assert res.status_code == 200
    assert res.data.decode() == 'Main'


def test_small_apps(app, client):
    small_apps = [{'id': 'zbruh', 'name': 'zbruh'}, {'id': 'kikoo', 'name': 'kikoo'}]
    app.mongo_client.get_db()['small_app'].insert(deepcopy(small_apps))

    res = client.get('/small-apps')
    assert res.status_code == 200
    assert json.loads(res.data) == small_apps

    app.mongo_client.get_db().drop_collection('small_app')
