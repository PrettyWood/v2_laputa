from pymongo import MongoClient


class CustomMongoClient(MongoClient):
    def __init__(self, *args, **kwargs):
        self.default_db = kwargs.pop('default_db', None)
        super().__init__(*args, **kwargs)
        self.small_app_id = None
        self.stage = None

    @property
    def db(self):
        if self.small_app_id is not None:
            return self[f'{self.default_db }-{self.small_app_id}']
        else:
            return self[self.default_db]

    def small_app_col(self, collection_name):
        if self.stage is not None:
            collection_name += f'-{self.stage}'
        return self.db[collection_name]

    def retrieve_last_config(self, config_name):
        config_collection = self.small_app_col(config_name)
        return config_collection.find({}, {'_id': False}).sort([('_id', -1)]).limit(1)[0]
