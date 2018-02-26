import json

import pytest


@pytest.fixture(autouse=True, scope='module')
def feed_db(app):
    app.mongo_client['test-sa_test']['etl_config'].insert({'title': 'etl config de prod poto!'})
    app.mongo_client['test-sa_test']['etl_config-staging'].insert(
        {'title': 'etl config de staging ma gueule!'})
    yield app
    app.mongo_client.drop_database('test-sa_test')


def test_etl_config_prod(client):
    res = client.get('sa_test/etl-config')
    assert res.status_code == 200
    assert json.loads(res.data) == {'title': 'etl config de prod poto!'}


def test_etl_config_staging(client):
    res = client.get('sa_test/etl-config?stage=staging')
    assert res.status_code == 200
    assert json.loads(res.data) == {'title': 'etl config de staging ma gueule!'}
