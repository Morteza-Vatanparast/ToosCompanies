from bson import ObjectId

from models.mongodb.base_model import MongodbModel
from models.mongodb.companies import CompaniesModel
from models.mongodb.news import NewsModel
from models.mongodb.services import ServicesModel
from models.mongodb.unit_companies import UnitCompaniesModel


class SettingModel:
    def __init__(self, _id=None):
        self.id = _id

    @staticmethod
    def get_one_login(username=None):
        try:
            __body = {"key": "ADMIN_AUTHENTICATED", "username": username}
            return MongodbModel(body=__body, collection="setting").get_one()
        except:
            return False

    @staticmethod
    def count_login(username=None):
        try:
            __body = {"key": "ADMIN_AUTHENTICATED", "username": username}
            return MongodbModel(body=__body, collection="setting").get_one()
        except:
            return False

    @staticmethod
    def get_format_slide_show():
        try:
            __body = {"key": "SLIDE_SHOW"}
            return MongodbModel(body=__body, collection="setting").get_one()['formats']
        except:
            return []

    @staticmethod
    def add_format_slide_show(_format=None, areas=None):
        try:
            __condition = {"key": "SLIDE_SHOW"}
            __body = {"$push": {
                "formats": {
                    "_id": ObjectId(),
                    "areas": areas,
                    "format": _format,
                }
            }}
            return MongodbModel(body=__body, condition=__condition, collection="setting").update()
        except:
            return False

    @staticmethod
    def delete_format_slide_show(_format=None):
        try:
            __condition = {"key": "SLIDE_SHOW"}
            __body = {"$pull": {
                "formats": {"_id": _format}
            }}
            return MongodbModel(body=__body, condition=__condition, collection="setting").update()
        except:
            return False

    @staticmethod
    def get_main_page():
        unit_sections = []
        try:
            __body = {"key": "MAIN_PAGE"}
            __a = MongodbModel(body=__body, collection="setting").get_one()
            __c = CompaniesModel()
            try:
                for i in __a['unit_sections']:
                    a = dict(
                        unit_name=UnitCompaniesModel(_id=i['unit']).get_one()['name'],
                        unit_id=i['unit'],
                        format=i['format'],
                        sort=i['sort'] if 'sort' in i.keys() else "",
                        companies=[]
                    )
                    for j in i['companies']:
                        _com = __c.get_one_main_page(j)
                        if _com is not False:
                            a['companies'].append(_com)
                    if len(a['companies']):
                        unit_sections.append(a)
            except:
                pass
            unit_sections = sorted(unit_sections, key=lambda k: k['sort'])
            return dict(
                unit_sections=unit_sections
            )
        except:
            return dict(
                unit_sections=unit_sections
            )

    @staticmethod
    def update_main_page(boxes=None, unit_sections=None):
        if boxes is None:
            boxes = []
        try:
            __condition = {"key": "MAIN_PAGE"}
            __body = {"$set": {
                "boxes": boxes,
                "unit_sections": unit_sections
            }}
            return MongodbModel(body=__body, condition=__condition, collection="setting").update()
        except:
            return False