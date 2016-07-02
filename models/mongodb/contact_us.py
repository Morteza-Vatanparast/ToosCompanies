#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

from models.mongodb.base_model import MongodbModel


class ContactUsModel:
    def __init__(self, _id=None, name=None, email=None, description=None, secure_cookie=None):
        self.id = _id
        self.name = name
        self.email = email
        self.description = description
        self.secure_cookie = secure_cookie

    def insert(self):
        try:
            __body = {
                "name": self.name,
                "email": self.email,
                "secure_cookie": self.secure_cookie,
                "description": self.description,
                "date": datetime.datetime.now(),
            }
            MongodbModel(body=__body, collection="contact_us").insert()
            return True
        except:
            return False
    
    @staticmethod
    def get_all():
        try:
            __body = {}
            __a = MongodbModel(body=__body, collection="contact_us").get_all()
            __r = []
            for __i in __a:
                __r.append(dict(
                    _id=__i['_id'],
                    name=__i['name'],
                    email=__i['email'] if __i['email'] is not None else u'وارد نشده',
                    description=__i['description'],
                ))
            return __r
        except:
            return []

    def delete(self):
        try:
            __body = {"_id": self.id}
            MongodbModel(body=__body, collection="contact_us").delete()
            return True
        except:
            return False

    @staticmethod
    def is_duplicate(secure_cookie=None):
        try:
            __body = {"secure_cookie": secure_cookie, "date": {"$gte": datetime.datetime.now() - datetime.timedelta(hours=24)}}
            __c = MongodbModel(body=__body, collection="contact_us").count()
            if __c:
                return True
            return False
        except:
            return False
