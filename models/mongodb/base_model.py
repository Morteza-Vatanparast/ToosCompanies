import pymongo

from config import Config

__author__ = 'Morteza'


class MongodbBaseModel:
    def __init__(self):
        mongodb_config = Config().mongodb
        connection = pymongo.MongoClient(host=mongodb_config['host'], port=mongodb_config['port'])
        self.db = connection[mongodb_config['db']]


class MongodbModel(MongodbBaseModel):
    def __init__(self, collection=None, body=None, condition=None, key=None, size=20, page=1, sort="date", option=None,
                 ascending=-1):
        MongodbBaseModel.__init__(self)
        self.__body = body
        self.__size = size
        self.__page = page
        self.__sort = sort
        self.__key = key
        self.__option = option
        self.__ascending = ascending

        self.__collection = collection
        self.__condition = condition
        if collection == 'companies':
            self.collection = self.db.companies
        if collection == 'unit_companies':
            self.collection = self.db.unit_companies
        if collection == 'industrial_town_companies':
            self.collection = self.db.industrial_town_companies
        if collection == 'province':
            self.collection = self.db.province
        if collection == 'city':
            self.collection = self.db.city
        if collection == 'tables':
            self.collection = self.db.tables

    def insert(self):
        try:
            return self.collection.insert(self.__body)
        except:
            return False

    def get_all(self):
        try:
            return self.collection.find(self.__body)
        except:
            return False

    def get_all_key(self):
        try:
            return self.collection.find(self.__body, self.__key)
        except:
            return False

    def get_all_pagination(self):
        try:
            return self.collection.find(self.__body).sort([(self.__sort, self.__ascending)]).skip(self.__size * (self.__page - 1)).limit(self.__size)
        except:
            return False

    def get_all_key_limit(self):
        try:
            return self.collection.find(self.__body, self.__key).skip(self.__size * (self.__page - 1)).limit(self.__size)
        except:
            return False

    def get_all_key_sort(self):
        try:
            return self.collection.find(self.__body, self.__key).sort([(self.__sort, self.__ascending)])
        except:
            return False

    def get_all_key_multi_sort(self):
        try:
            return self.collection.find(self.__body, self.__key).sort(self.__sort)
        except:
            return False

    def get_all_key_pagination(self):
        try:
            return self.collection.find(self.__body, self.__key).sort([(self.__sort, self.__ascending)]).skip(self.__size * (self.__page - 1)).limit(self.__size)
        except:
            return False

    def get_all_sort(self):
        try:
            return self.collection.find(self.__body).sort([(self.__sort, self.__ascending)])
        except:
            return False

    def get_one(self):
        try:
            return self.collection.find_one(self.__body)
        except:
            return False

    def get_one_key(self):
        try:
            return self.collection.find_one(self.__body, self.__key)
        except:
            return False

    def delete(self):
        try:
            return self.collection.remove(self.__body)
        except:
            return False

    def count(self):
        try:
            return self.collection.find(self.__body).count()
        except:
            return 0

    def update(self):
        try:
            return self.collection.update(self.__condition, self.__body)
        except:
            return False

    def update_option(self):
        try:
            return self.collection.update(self.__condition, self.__body, self.__option)
        except:
            return False

    def aggregate(self):
        try:
            return self.collection.aggregate(self.__body)
        except:
            return False


class BaseModel:
    def __init__(self):
        self.result = {'value': {}, 'status': False}

    @property
    def value(self):
        return self.result['value']

    @value.setter
    def value(self, value):
        self.result['value'] = value

    @property
    def status(self):
        return self.result['status']

    @status.setter
    def status(self, status):
        self.result['status'] = status