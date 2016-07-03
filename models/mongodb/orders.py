import datetime

from models.mongodb.base_model import MongodbModel
from models.mongodb.services import ServicesModel


class OrdersModel:
    def __init__(self, _id=None, name=None, count=None, service=None, phone=None, address=None, description=None,
                 secure_cookie=None):
        self.id = _id
        self.name = name
        self.count = count
        self.service = service
        self.phone = phone
        self.address = address
        self.description = description
        self.secure_cookie = secure_cookie

    def insert(self):
        try:
            __body = {
                "name": self.name,
                "service": self.service,
                "count": self.count,
                "phone": self.phone,
                "address": self.address,
                "secure_cookie": self.secure_cookie,
                "date": datetime.datetime.now(),
                "description": self.description
            }
            MongodbModel(body=__body, collection="orders").insert()
            return True
        except:
            return False
    
    @staticmethod
    def get_all():
        try:
            __body = {}
            __a = MongodbModel(body=__body, collection="orders").get_all()
            __r = []
            for __i in __a:
                try:
                    service_name = ServicesModel(_id=__i['service']).get_one()['name']
                except:
                    service_name = '-'
                __r.append(dict(
                    _id=__i['_id'],
                    name=__i['name'],
                    service=__i['service'],
                    service_name=service_name,
                    count=__i['count'],
                    phone=__i['phone'],
                    address=__i['address'],
                    description=__i['description'],
                ))
            return __r
        except:
            return []

    def delete(self):
        try:
            __body = {"_id": self.id}
            MongodbModel(body=__body, collection="orders").delete()
            return True
        except:
            return False

    def get_one(self):
        try:
            __body = {"_id": self.id}
            return MongodbModel(body=__body, collection="orders").get_one()
        except:
            return False

    @staticmethod
    def is_duplicate(secure_cookie=None):
        try:
            __body = {"secure_cookie": secure_cookie, "date": {"$gte": datetime.datetime.now() - datetime.timedelta(hours=24)}}
            __c = MongodbModel(body=__body, collection="orders").count()
            if __c:
                return True
            return False
        except:
            return False
