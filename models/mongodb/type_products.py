from models.mongodb.base_model import MongodbModel


class TypeProductsModel:
    def __init__(self, _id=None, name=None, parent=None):
        self.id = _id
        self.name = name
        self.parent = parent

    def insert(self):
        try:
            __body = {
                "name": self.name,
                "parent": self.parent
            }
            MongodbModel(body=__body, collection="type_products").insert()
            return True
        except:
            return False

    @staticmethod
    def get_all():
        try:
            __body = {"parent": None}
            __r = MongodbModel(body=__body, collection="type_products").get_all()
            __l = []
            for i in __r:
                s_l = []
                s_r = MongodbModel(collection="type_products", body={"parent": i['_id']}).get_all()
                for j in s_r:
                    s_l.append(dict(
                        _id=j['_id'],
                        name=j['name'],
                        parent=j['parent'],
                    ))
                __l.append(dict(
                    _id=i['_id'],
                    name=i['name'],
                    parent=None,
                    child=s_l
                ))
            return __l
        except:
            return []

    def get_all_sub(self):
        try:
            __body = {"parent": self.parent}
            __r = MongodbModel(body=__body, collection="type_products").get_all()
            __l = []
            for i in __r:
                __l.append(dict(
                    _id=i['_id'],
                    name=i['name']
                ))
            return __l
        except:
            return []

    def get_one(self):
        try:
            __body = {"_id": self.id}
            return MongodbModel(body=__body, collection="type_products").get_one()
        except:
            return False

    def update(self):
        try:
            __body = {
                "$set": {
                    "name": self.name,
                    "parent": self.parent
                }
            }
            __condition = {"_id": self.id}
            MongodbModel(body=__body, condition=__condition, collection="type_products").update()
            return True
        except:
            return False

    def delete(self):
        try:
            __body = {"_id": self.id}
            MongodbModel(body=__body, collection="type_products").delete()
            return True
        except:
            return False
