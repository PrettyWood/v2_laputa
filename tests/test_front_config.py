import json

import pytest


@pytest.fixture(autouse=True, scope='module')
def feed_db(app):
    app.mongo_client['test-sa_test']['front_config'].insert({'title': 'front config de prod poto!'})
    app.mongo_client['test-sa_test']['front_config-staging'].insert(
        {'title': 'front config de staging ma gueule!'})
    yield app
    app.mongo_client.drop_database('test-sa_test')


def test_front_config_prod(client):
    res = client.get('sa_test/front-config')
    assert res.status_code == 200
    assert json.loads(res.data) == {'title': 'front config de prod poto!'}


def test_front_config_staging(client):
    res = client.get('sa_test/front-config?stage=staging')
    assert res.status_code == 200
    assert json.loads(res.data) == {'title': 'front config de staging ma gueule!'}
