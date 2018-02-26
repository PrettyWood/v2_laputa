from pymongo import MongoClient


class CustomMongoClient(MongoClient):
    def __init__(self, *args, **kwargs):
        self.instance_db = kwargs.pop('instance_db', None)
        super().__init__(*args, **kwargs)

    def get_db(self, small_app_id=None):
        if small_app_id is not None:
            return self[f'{self.instance_db }-{small_app_id}']
        else:
            return self[self.instance_db]

    def small_app_col(self, small_app_id, collection_name, stage=None):
        if stage is not None:
            collection_name += f'-{stage}'
        return self.get_db(small_app_id)[collection_name]

    def retrieve_last_config(self, small_app_id, config_name, stage=None):
        config_collection = self.small_app_col(small_app_id, config_name, stage=stage)
        return config_collection.find({}, {'_id': False}).sort([('_id', -1)]).limit(1)[0]
