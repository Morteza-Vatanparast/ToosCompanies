from models.mongodb.base_model import MongodbModel
from models.mongodb.type_products import TypeProductsModel


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

    def get_one(self):
        try:
            __body = {"_id": self.id}
            __c = MongodbModel(body=__body, collection="products").get_one()

            def __get(__n, __d):
                return __c[__n] if __n in __c.keys() else __d
            try:
                type_name = TypeProductsModel(_id=__c['type']).get_one()['name']
            except:
                type_name = '-'
            try:
                sub_type_name = TypeProductsModel(_id=__c['sub_type']).get_one()['name']
            except:
                sub_type_name = '-'
            return dict(
                _id=__get("_id", None),
                name=__get("name", ""),
                image=__get("image", ""),
                type=__get("type", ""),
                type_name=type_name,
                sub_type_name=sub_type_name,
                sub_type=__get("sub_type", "")
            )
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
                    "name": self.name,
                    "type": self.type,
                    "sub_type": self.sub_type
                }
            }
            if len(self.image):
                __body['$set']['image'] = self.image
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

    @staticmethod
    def get_all_by_like(_like):
        try:
            __body = {
                'name': {"$regex": '^' + _like},
            }
            __key = {"_id": 1, "name": 1, "image": 1}
            x = MongodbModel(collection='products', body=__body, key=__key, page=1, size=20).get_all_key_limit()
            v = []
            if x:
                for r in x:
                    v.append(dict(
                        id=r['_id'],
                        name=r['name'],
                        image=r['image']
                    ))
            return v
        except:
            return []

    @staticmethod
    def admin_search(name="all", _type="all", _sub_type="all"):
        try:
            __body = {"$and": []}
            if name != 'all':
                __body['$and'].append({'name': {"$regex": '^' + name}})
            if _type != 'all':
                __body['$and'].append({'type': _type})
            if _sub_type != 'all':
                __body['$and'].append({'sub_type': _sub_type})
            if not len(__body['$and']):
                __body = {}
            __a = MongodbModel(body=__body, collection="products").get_all()
            __r = []
            for __i in __a:
                __r.append(dict(
                    _id=__i['_id'],
                    name=__i['name'],
                    image=__i['image'],
                ))
            return __r
        except:
            return []