from models.mongodb.base_model import MongodbModel


class ServicesModel:
    def __init__(self, _id=None, name=None, description=None, image=None, main_page=None):
        self.id = _id
        self.name = name
        self.image = image
        self.main_page = main_page
        self.description = description

    def insert(self):
        try:
            __body = {
                "name": self.name,
                "description": self.description,
                "main_page": self.main_page,
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
