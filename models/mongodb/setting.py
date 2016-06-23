from models.mongodb.base_model import MongodbModel


class SettingModel:
    def __init__(self, _id=None):
        self.id = _id

    @staticmethod
    def get_one_login(username=None):
        try:
            __body = {"key": "ADMIN_AUTHENTICATED", "username": username}
            return MongodbModel(body=__body, collection="setting").get_one()
        except:
            return False

    @staticmethod
    def count_login(username=None):
        try:
            __body = {"key": "ADMIN_AUTHENTICATED", "username": username}
            return MongodbModel(body=__body, collection="setting").get_one()
        except:
            return False
