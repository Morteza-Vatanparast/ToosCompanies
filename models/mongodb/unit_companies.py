from bson import ObjectId

from models.mongodb.base_model import MongodbModel


class UnitCompaniesModel:
    FOOD = ObjectId("5742867f6dd534700def2733")
    METAL = ObjectId("574284876dd534700def272f")
    CHEMICAL = ObjectId("574286766dd534700def2732")
    ELECTRICAL = ObjectId("5742868e6dd534700def2734")
    TEXTILE = ObjectId("574286986dd534700def2735")
    MINERAL = ObjectId("574286a46dd534700def2736")

    def __init__(self, _id=None, name=None):
        self.id = _id
        self.name = name

    def insert(self):
        try:
            __body = {
                "name": self.name
            }
            MongodbModel(body=__body, collection="unit_companies").insert()
            return True
        except:
            return False

    @staticmethod
    def get_all():
        try:
            __body = {}
            return [i for i in MongodbModel(body=__body, collection="unit_companies").get_all()]
        except:
            return []

    def get_one(self):
        try:
            __body = {"_id": self.id}
            return MongodbModel(body=__body, collection="unit_companies").get_one()
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
            MongodbModel(body=__body, condition=__condition, collection="unit_companies").update()
            return True
        except:
            return False

    def delete(self):
        try:
            __body = {"_id": self.id}
            MongodbModel(body=__body, collection="unit_companies").delete()
            return True
        except:
            return False
