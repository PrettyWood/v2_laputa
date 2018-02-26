import pytest

from api import app


@pytest.fixture(scope='session', name='app')
def test_app():
    yield app
    # teardown (just in case)
    test_dbs = [db for db in app.mongo_client.database_names()
                if db.startswith(app.mongo_client.instance_db)]
    for test_db in test_dbs:
        app.mongo.drop_database(test_db)


@pytest.fixture(scope='session')
def client():
    return app.test_client()
