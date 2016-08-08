import random

from models.mongodb.base_model import MongodbModel


class ServicesModel:
    def __init__(self, _id=None, name=None, description=None, image=None, main_page=None,
                 special_offer=None, special_offer_text=None):
        self.id = _id
        self.name = name
        self.image = image
        self.main_page = main_page
        self.special_offer = special_offer
        self.special_offer_text = special_offer_text
        self.description = description

    def insert(self):
        try:
            __body = {
                "name": self.name,
                "description": self.description,
                "main_page": self.main_page,
                "special_offer": self.special_offer,
                "special_offer_text": self.special_offer_text,
                "image": self.image
            }
            MongodbModel(body=__body, collection="services").insert()
            return True
        except:
            return False

    @staticmethod
    def get_one_main_page(__id=None):
        try:
            __body = {'_id': __id}
            __key = {'name': 1, 'image': 1, "special_offer_text": 1}
            __i = MongodbModel(body=__body, key=__key, collection="services").get_one_key()
            return dict(
                _id=__i['_id'],
                name=__i['name'],
                special_offer_text=__i['special_offer_text'],
                image=__i['image'] if "image" in __i.keys() else "",
            )
        except:
            return False

    @staticmethod
    def get_all_like_main_page(_text=""):
        # try:
            __body = {'name': {"$regex": _text}, "main_page": True, "special_offer": True}
            __key = {'name': 1, 'image': 1, 'special_offer_text': 1}
            __a = MongodbModel(body=__body, key=__key, collection="services", sort="name", ascending=1, size=10).get_all_key_pagination()
            __r = []
            for __i in __a:
                __r.append(dict(
                    _id=__i['_id'],
                    name=__i['name'],
                    special_offer_text=__i['special_offer_text'],
                    image=__i['image'] if "image" in __i.keys() else "",
                ))
            return __r
        # except:
        #     return []
    
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

    @staticmethod
    def get_all_main_page():
        try:
            __body = {"main_page": True}
            __a = MongodbModel(body=__body, collection="services").get_all()
            __r = []
            for __i in __a:
                __r.append(__i)
            return __r
        except:
            return []

    @staticmethod
    def get_all_pagination(page=1, size=15):
        try:
            __body = {}
            __a = MongodbModel(body=__body, collection="services", page=page, size=size, sort="name", ascending=1)\
                .get_all_key_pagination()
            __r = []
            for __i in __a:
                __r.append(__i)
            return __r
        except:
            return []

    @staticmethod
    def count():
        try:
            __body = {}
            return MongodbModel(body=__body, collection="services").count()
        except:
            return 0

    def update(self):
        try:
            __body = {
                "$set": {
                    "name": self.name,
                    "main_page": self.main_page,
                    "description": self.description,
                    "special_offer": self.special_offer,
                    "special_offer_text": self.special_offer_text,
                }
            }
            if len(self.image):
                __body['$set']['image'] = self.image[0]
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

    @staticmethod
    def get_similar(count=4, _id=None):
        try:
            __body = {"image": {"$ne": None}, "_id": {"$ne": _id}}
            __key = {'name': 1, 'image': 1}
            __count = MongodbModel(body=__body, collection="services").count()
            __rand = []
            __r = []
            while len(__rand) < count:
                _num = random.randint(0, __count - 1)
                if _num not in __rand:
                    __rand.append(_num)

            for i in __rand:
                __i = MongodbModel(body=__body, key=__key, size=i, collection="services").get_all_key_random()
                try:
                    __r.append(dict(
                        _id=__i['_id'],
                        name=__i['name'],
                        image=__i['image'],
                    ))
                except:
                    pass
            return __r
        except:
            return []
