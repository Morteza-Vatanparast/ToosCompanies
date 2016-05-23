from models.mongodb.base_model import MongodbModel


class ProvinceCityModel:
    def __init__(self, _id=None, province=None):
        self.id = _id
        self.province = province

    @staticmethod
    def get_all_province():
        try:
            __body = {}
            return MongodbModel(body=__body, collection="province").get_all()
        except:
            return []

    def get_all_city(self):
        try:
            __body = {"province": self.province}
            return MongodbModel(body=__body, collection="city").get_all()
        except:
            return []
