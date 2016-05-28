from models.mongodb.base_model import MongodbModel


class ServicesModel:
    def __init__(self, _id=None, name=None, description=None, image=None):
        self.id = _id
        self.name = name
        self.image = image
        self.description = description

    def insert(self):
        try:
            __body = {
                "name": self.name,
                "description": self.description,
                "image": self.image
            }
            MongodbModel(body=__body, collection="services").insert()
            return True
        except:
            return False
    
    @staticmethod
    def get_all():
        try:
            __body = {}
            __a = MongodbModel(body=__body, collection="services").get_all()
            __r = []
            for __i in __a:
                __r.append(__i)
            return __r
        except:
            return []

    def update(self):
        try:
            __body = {
                "$set": {
                    "name": self.name,
                    "description": self.description
                }
            }
            if len(self.image):
                __body['$set']['image'] = self.image
            __condition = {"_id": self.id}
            MongodbModel(body=__body, condition=__condition, collection="services").update()
            return True
        except:
            return False

    def delete(self):
        try:
            __body = {"_id": self.id}
            MongodbModel(body=__body, collection="services").delete()
            return True
        except:
            return False

    def get_one(self):
        try:
            __body = {"_id": self.id}
            return MongodbModel(body=__body, collection="services").get_one()
        except:
            return False
