from models.mongodb.base_model import MongodbModel


class TablesModel:
    def __init__(self, _id=None, name=None):
        self.id = _id

    @staticmethod
    def insert(**__body):
        try:
            MongodbModel(body=__body, collection="tables").insert()
            return True
        except:
            return False

    @staticmethod
    def get_all():
        try:
            __body = {}
            return MongodbModel(body=__body, collection="tables").get_all()
        except:
            return []

    def get_one(self):
        try:
            __body = {"_id": self.id}
            return MongodbModel(body=__body, collection="tables").get_one()
        except:
            return False

    def update(self, **__body):
        try:
            _body = {"$set": {
                "name": __body["name"],
                "base_link": __body["base_link"],
                "active": __body["active"],
                "trs": __body["trs"],
            }}
            __condition = {"_id": self.id}

            MongodbModel(body=_body, condition=__condition, collection="tables").update()
            return True
        except:
            return False

    def update_trs(self, __trs):
        try:
            _body = {"$set": {
                "trs": __trs
            }}
            __condition = {"_id": self.id}

            MongodbModel(body=_body, condition=__condition, collection="tables").update()
            return True
        except:
            return False

    def delete(self):
        try:
            __body = {"_id": self.id}
            MongodbModel(body=__body, collection="tables").delete()
            return True
        except:
            return False
