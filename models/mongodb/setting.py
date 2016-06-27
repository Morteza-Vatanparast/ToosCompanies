from bson import ObjectId

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

    @staticmethod
    def get_format_slide_show():
        try:
            __body = {"key": "SLIDE_SHOW"}
            return MongodbModel(body=__body, collection="setting").get_one()['formats']
        except:
            return []

    @staticmethod
    def add_format_slide_show(_format=None, areas=None):
        try:
            __condition = {"key": "SLIDE_SHOW"}
            __body = {"$push": {
                "formats": {
                    "_id": ObjectId(),
                    "areas": areas,
                    "format": _format,
                }
            }}
            return MongodbModel(body=__body, condition=__condition, collection="setting").update()
        except:
            return False

    @staticmethod
    def delete_format_slide_show(_format=None):
        try:
            __condition = {"key": "SLIDE_SHOW"}
            __body = {"$pull": {
                "formats": {"_id": _format}
            }}
            return MongodbModel(body=__body, condition=__condition, collection="setting").update()
        except:
            return False
