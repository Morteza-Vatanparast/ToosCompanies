from models.mongodb.base_model import MongodbModel


class ProductsModel:
    def __init__(self, _id=None, name=None, image=None, _type=None, _sub_type=None):
        self.id = _id
        self.name = name
        self.image = image
        self.type = _type
        self.sub_type = _sub_type

    def insert(self):
        try:
            __body = {
                "name": self.name,
                "image": self.image,
                "type": self.type,
                "sub_type": self.sub_type
            }
            MongodbModel(body=__body, collection="products").insert()
            return True
        except:
            return False

    @staticmethod
    def get_all():
        try:
            __body = {}
            return MongodbModel(body=__body, collection="products").get_all()
        except:
            return []

    def update(self):
        try:
            __body = {
                "$set": {
                    "name": self.name
                }
            }
            __condition = {"_id": self.id}
            MongodbModel(body=__body, condition=__condition, collection="products").update()
            return True
        except:
            return False

    def delete(self):
        try:
            __body = {"_id": self.id}
            MongodbModel(body=__body, collection="products").delete()
            return True
        except:
            return False
