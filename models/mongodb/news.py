import random

from models.mongodb.base_model import MongodbModel


class NewsModel:
    def __init__(self, _id=None, title=None, image=None, summary=None, body=None, main_page=None):
        self.id = _id
        self.title = title
        self.image = image
        self.summary = summary
        self.body = body
        self.main_page = main_page

    def insert(self):
        try:
            __body = {
                "title": self.title,
                "image": self.image,
                "main_page": self.main_page,
                "summary": self.summary,
                "body": self.body
            }
            MongodbModel(body=__body, collection="news").insert()
            return True
        except:
            return False
    
    @staticmethod
    def get_all():
        try:
            __body = {}
            __a = MongodbModel(body=__body, collection="news").get_all()
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
            __a = MongodbModel(body=__body, collection="news").get_all()
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
            __a = MongodbModel(body=__body, collection="news", page=page, size=size, sort="name", ascending=1)\
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
            return MongodbModel(body=__body, collection="news").count()
        except:
            return 0

    def update(self):
        try:
            __body = {
                "$set": {
                    "title": self.title,
                    "main_page": self.main_page,
                    "summary": self.summary,
                    "body": self.body
                }
            }
            if len(self.image):
                __body['$set']['image'] = self.image[0]
            __condition = {"_id": self.id}
            MongodbModel(body=__body, condition=__condition, collection="news").update()
            return True
        except:
            return False

    def delete(self):
        try:
            __body = {"_id": self.id}
            MongodbModel(body=__body, collection="news").delete()
            return True
        except:
            return False

    def get_one(self):
        try:
            __body = {"_id": self.id}
            return MongodbModel(body=__body, collection="news").get_one()
        except:
            return False
