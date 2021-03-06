from models.mongodb.base_model import MongodbModel


class IndustrialTownCompaniesModel:
    def __init__(self, _id=None, name=None):
        self.id = _id
        self.name = name

    def insert(self):
        try:
            __body = {
                "name": self.name
            }
            MongodbModel(body=__body, collection="industrial_town_companies").insert()
            return True
        except:
            return False

    @staticmethod
    def get_all():
        try:
            __body = {}
            return [i for i in MongodbModel(body=__body, collection="industrial_town_companies").get_all()]
        except:
            return []

    def get_one(self):
        try:
            __body = {"_id": self.id}
            return MongodbModel(body=__body, collection="industrial_town_companies").get_one()
        except:
            return False

    def update(self):
        try:
            __body = {
                "$set": {
                    "name": self.name
                }
            }
            __condition = {"_id": self.id}
            MongodbModel(body=__body, condition=__condition, collection="industrial_town_companies").update()
            return True
        except:
            return False

    def delete(self):
        try:
            __body = {"_id": self.id}
            MongodbModel(body=__body, collection="industrial_town_companies").delete()
            return True
        except:
            return False
