import random

from models.mongodb.base_model import MongodbModel
from models.mongodb.industrial_town_companies import IndustrialTownCompaniesModel
from models.mongodb.products import ProductsModel
from models.mongodb.province_city import ProvinceCityModel
from models.mongodb.unit_companies import UnitCompaniesModel


class CompaniesModel:
    def __init__(self, _id=None, name=None, main_page=None, slider=None, description=None, logo=None, images=None,
                 unit=None, active=None, industrial_town=None, address=None, phone=None, phone2=None, fax=None,
                 site=None, email=None, province=None, city=None, ceo=None, coordinator=None, owner=None, mobile=None,
                 products=None, materials=None, slider_image=None, about=None, image=None):
        self.id = _id
        self.name = name
        self.main_page = main_page
        self.slider = slider
        self.description = description
        self.about = about
        self.logo = logo
        self.images = images
        self.slider_image = slider_image
        self.image = image
        self.unit = unit
        self.active = active
        self.industrial_town = industrial_town
        self.address = address
        self.phone = phone
        self.phone2 = phone2
        self.mobile = mobile
        if products is None:
            products = []
        if materials is None:
            materials = []
        self.products = products
        self.materials = materials
        self.fax = fax
        self.site = site
        self.email = email
        self.province = province
        self.city = city
        self.ceo = ceo
        self.coordinator = coordinator
        self.owner = owner

    def insert(self, register=False):
        try:
            __body = {
                "name": self.name,
                "main_page": self.main_page,
                "slider": self.slider,
                "description": self.description,
                "about": self.about,
                "logo": self.logo,
                "slider_image": self.slider_image,
                "image": self.image,
                "images": self.images,
                "unit": self.unit,
                "industrial_town": self.industrial_town,
                "address": self.address,
                "phone": self.phone,
                "phone2": self.phone2,
                "mobile": self.mobile,
                "fax": self.fax,
                "site": self.site,
                "email": self.email,
                "province": self.province,
                "city": self.city,
                "ceo": self.ceo,
                "coordinator": self.coordinator,
                "owner": self.owner,
                "active": self.active,
                "products": self.products,
                "register": register,
                "materials": self.materials
            }
            MongodbModel(body=__body, collection="companies").insert()
            return True
        except:
            return False

    def get_all(self, page=1, size=30):
        try:
            __body = {"register": False}
            __a = MongodbModel(body=__body, collection="companies", sort="name", size=size, page=page, ascending=1).get_all_pagination()
            __r = []
            for __i in __a:
                company = self.get_company(__i)
                if company is not False:
                    __r.append(company)
            return __r
        except:
            return []

    def get_all_register(self, page=1, size=30):
        try:
            __body = {"register": True}
            __a = MongodbModel(body=__body, collection="companies", sort="name", size=size, page=page, ascending=1).get_all_pagination()
            __r = []
            for __i in __a:
                company = self.get_company(__i)
                if company is not False:
                    __r.append(company)
            return __r
        except:
            return []

    def update(self):
        try:
            __body = {
                "$set": {
                    "name": self.name,
                    "main_page": self.main_page,
                    "slider": self.slider,
                    "description": self.description,
                    "about": self.about,
                    "unit": self.unit,
                    "industrial_town": self.industrial_town,
                    "address": self.address,
                    "phone": self.phone,
                    "phone2": self.phone2,
                    "mobile": self.mobile,
                    "fax": self.fax,
                    "site": self.site,
                    "email": self.email,
                    "province": self.province,
                    "city": self.city,
                    "ceo": self.ceo,
                    "coordinator": self.coordinator,
                    "owner": self.owner,
                    "active": self.active,
                    "products": self.products
                }
            }
            if len(self.logo):
                __body['$set']['logo'] = self.logo[0]
            if len(self.slider_image):
                __body['$set']['slider_image'] = self.slider_image[0]
            if len(self.image):
                __body['$set']['image'] = self.image[0]
            if len(self.images):
                images = self.get_one()['images']
                __body['$set']['images'] = images + self.images
            __condition = {"_id": self.id}
            MongodbModel(body=__body, condition=__condition, collection="companies").update()
            return True
        except:
            return False

    def update_compare(self):
        try:
            __body = {
                "$set": {
                    "name": self.name,
                    "description": self.description,
                    "unit": self.unit,
                    "industrial_town": self.industrial_town,
                    "address": self.address,
                    "phone": self.phone,
                    "phone2": self.phone2,
                    "mobile": self.mobile,
                    "fax": self.fax,
                    "site": self.site,
                    "email": self.email,
                    "province": self.province,
                    "city": self.city,
                    "ceo": self.ceo,
                    "coordinator": self.coordinator,
                    "owner": self.owner,
                }
            }
            __condition = {"_id": self.id}
            MongodbModel(body=__body, condition=__condition, collection="companies").update()
            return True
        except:
            return False

    def delete(self):
        try:
            __body = {"_id": self.id}
            MongodbModel(body=__body, collection="companies").delete()
            return True
        except:
            return False

    @staticmethod
    def delete_all():
        try:
            MongodbModel(body={}, collection="companies").delete()
            return True
        except:
            return False

    @staticmethod
    def count():
        try:
            __body = {"register": False}
            return MongodbModel(body=__body, collection="companies").count()
        except:
            return 0

    @staticmethod
    def count_register():
        try:
            __body = {"register": True}
            return MongodbModel(body=__body, collection="companies").count()
        except:
            return 0

    def delete_image(self, image):
        try:
            __body = {
                "$pull": {
                    "images": image
                }
            }

            __condition = {'_id': self.id}
            MongodbModel(body=__body, condition=__condition, collection="companies").update()
            return True
        except:
            return False

    def add_product(self, product):
        try:
            __body = {
                "$push": {
                    "products": product
                }
            }

            __condition = {'_id': self.id}
            if product not in self.get_products():
                MongodbModel(body=__body, condition=__condition, collection="companies").update()
            return True
        except:
            return False

    def add_material(self, material):
        try:
            __body = {
                "$push": {
                    "materials": material
                }
            }

            __condition = {'_id': self.id}
            if material not in self.get_materials():
                MongodbModel(body=__body, condition=__condition, collection="companies").update()
            return True
        except:
            return False

    def delete_product(self, product):
        try:
            __body = {
                "$pull": {
                    "products": product
                }
            }

            __condition = {'_id': self.id}
            MongodbModel(body=__body, condition=__condition, collection="companies").update()
            return True
        except:
            return False

    def delete_material(self, material):
        try:
            __body = {
                "$pull": {
                    "materials": material
                }
            }

            __condition = {'_id': self.id}
            MongodbModel(body=__body, condition=__condition, collection="companies").update()
            return True
        except:
            return False

    @staticmethod
    def get_company(__c):
        try:
            def __get(__n, __d):
                return __c[__n] if __n in __c.keys() else __d

            try:
                products = []
                for i in __c['products']:
                    __p = ProductsModel(_id=i).get_one()
                    if __p is not False:
                        products.append(__p)
            except:
                products = []
            try:
                materials = []
                for i in __c['materials']:
                    __p = ProductsModel(_id=i).get_one()
                    if __p is not False:
                        materials.append(__p)
            except:
                materials = []
            try:
                province_name = ProvinceCityModel(_id=__c['province']).get_province()['name']
            except:
                province_name = "-"
            try:
                city_name = ProvinceCityModel(_id=__c['city']).get_city()['name']
            except:
                city_name = "-"
            try:
                unit_name = UnitCompaniesModel(_id=__c['unit']).get_one()['name']
            except:
                unit_name = "-"
            try:
                industrial_town_name = IndustrialTownCompaniesModel(_id=__c['industrial_town']).get_one()['name']
            except:
                industrial_town_name = "-"

            return dict(
                _id=__get("_id", None),
                name=__get("name", ""),
                main_page=__get("main_page", False),
                slider=__get("slider", False),
                active=__get("active", False),
                logo=__get("logo", ""),
                slider_image=__get("slider_image", ""),
                image=__get("image", ""),
                address=__get("address", ""),
                phone=__get("phone", ""),
                phone2=__get("phone2", ""),
                mobile=__get("mobile", ""),
                fax=__get("fax", ""),
                site=__get("site", ""),
                email=__get("email", ""),
                ceo=__get("ceo", ""),
                coordinator=__get("coordinator", ""),
                owner=__get("owner", ""),
                province=__get("province", ""),
                province_name=province_name,
                city_name=city_name,
                city=__get("city", ""),
                unit=__get("unit", ""),
                unit_name=unit_name,
                industrial_town=__get("industrial_town", ""),
                industrial_town_name=industrial_town_name,
                images=__get("images", []),
                materials=materials,
                products=products,
                description=__get("description", ""),
                about=__get("about", "")
            )
        except:
            return False

    def get_one(self):
        try:
            __body = {"_id": self.id}
            __c = MongodbModel(body=__body, collection="companies").get_one()
            return self.get_company(__c)

        except:
            return False

    def get_products(self):
        try:
            __body = {"_id": self.id}
            __key = {"products": 1}
            __c = MongodbModel(body=__body, key=__key, collection="companies").get_one_key()
            return __c['products']
        except:
            return []

    @staticmethod
    def get_by_products(product):
        try:
            __body = {"products": product}
            __key = {"_id": 1, "name": 1, "logo": 1, "products": 1}
            __c = MongodbModel(body=__body, key=__key, collection="companies").get_all_key()
            __l = []
            for i in __c:
                try:
                    products = []
                    for j in i['products']:
                        __p = ProductsModel(_id=j).get_one()
                        if __p is not False:
                            products.append(__p)
                except:
                    products = []
                __l.append(dict(
                    _id=i['_id'],
                    name=i['name'],
                    logo=i['logo'],
                    products=products
                ))
            return __l
        except:
            return []

    def get_materials(self):
        try:
            __body = {"_id": self.id}
            __key = {"materials": 1}
            __c = MongodbModel(body=__body, key=__key, collection="companies").get_one_key()
            return __c['materials']
        except:
            return []

    @staticmethod
    def get_by_materials(material):
        try:
            __body = {"materials": material}
            __key = {"_id": 1, "name": 1, "logo": 1, "materials": 1}
            __c = MongodbModel(body=__body, key=__key, collection="companies").get_all_key()
            __l = []
            for i in __c:
                try:
                    materials = []
                    for j in i['materials']:
                        __p = ProductsModel(_id=j).get_one()
                        if __p is not False:
                            materials.append(__p)
                except:
                    materials = []
                __l.append(dict(
                    _id=i['_id'],
                    name=i['name'],
                    logo=i['logo'],
                    materials=materials
                ))
            return __l
        except:
            return []

    def admin_search(self, name="all", ceo="all", owner="all", province="all", city="all", unit="all", industrial_town="all"):
        try:
            __body = {"$and": []}
            if name != 'all':
                __body['$and'].append({'name': {"$regex": name}})
            if ceo != 'all':
                __body['$and'].append({'ceo': {"$regex": ceo}})
            if owner != 'all':
                __body['$and'].append({'owner': {"$regex": owner}})
            if province != 'all':
                __body['$and'].append({'province': province})
            if city != 'all':
                __body['$and'].append({'city': city})
            if unit != 'all':
                __body['$and'].append({'unit': unit})
            if industrial_town != 'all':
                __body['$and'].append({'industrial_town': industrial_town})
            if not len(__body['$and']):
                __body = {}
            __a = MongodbModel(body=__body, collection="companies").get_all()
            __r = []
            for __i in __a:
                company = self.get_company(__i)
                if company is not False:
                    __r.append(company)
            return __r
        except:
            return []

    @staticmethod
    def user_search(name="all", province="all", city="all", unit="all", page=1, size=30):
        try:
            __body = {"$and": [{"active": True}]}
            if name != 'all':
                __body['$and'].append(dict(name={"$regex": name}))
            if province != 'all':
                __body['$and'].append(dict(province=province))
            if city != 'all':
                __body['$and'].append(dict(city=city))
            if unit != 'all':
                __body['$and'].append(dict(unit=unit))
            if not len(__body['$and']):
                __body = {}
            __key = {'name': 1, 'image': 1, 'city': 1, 'industrial_town': 1, 'description': 1}
            __a = MongodbModel(body=__body, key=__key, collection="companies", sort="name", page=page, size=size,
                               ascending=1).get_all_key_pagination()
            __r = []
            for __i in __a:
                __r.append(dict(
                    _id=__i['_id'],
                    name=__i['name'],
                    image=__i['image'] if "image" in __i.keys() else "",
                    city=ProvinceCityModel(_id=__i['city']).get_city()['name'],
                    industrial_town=IndustrialTownCompaniesModel(_id=__i['industrial_town']).get_one()['name'],
                    description=__i['description']
                ))
            return __r
        except:
            return []

    @staticmethod
    def user_search_count(name="all", province="all", city="all", unit="all"):
        try:
            __body = {"$and": [{"active": True}]}
            if name != 'all':
                __body['$and'].append(dict(name={"$regex": name}))
            if province != 'all':
                __body['$and'].append(dict(province=province))
            if city != 'all':
                __body['$and'].append(dict(city=city))
            if unit != 'all':
                __body['$and'].append(dict(unit=unit))
            if not len(__body['$and']):
                __body = {}
            return MongodbModel(body=__body, collection="companies", sort="name").count()
        except:
            return 0

    @staticmethod
    def get_all_by_like(__text=""):
        try:
            __body = {'name': {"$regex": __text}}
            __key = {'name': 1, 'logo': 1, "slider_image": 1}
            __a = MongodbModel(body=__body, key=__key, collection="companies", sort="name", ascending=1, size=10).get_all_key_pagination()
            __r = []
            for __i in __a:
                __r.append(dict(
                    _id=__i['_id'],
                    name=__i['name'],
                    logo=__i['logo'],
                    slider_image=__i['slider_image'] if 'slider_image' in __i.keys() else None,
                ))
            return __r
        except:
            return []

    @staticmethod
    def get_all_by_like_has_slider(__text=""):
        try:
            __body = {'name': {"$regex": __text}, "slider": True, "active": True}
            __key = {'name': 1, 'logo': 1, "slider_image": 1}
            __a = MongodbModel(body=__body, key=__key, collection="companies", sort="name", ascending=1, size=10).get_all_key_pagination()
            __r = []
            for __i in __a:
                __r.append(dict(
                    _id=__i['_id'],
                    name=__i['name'],
                    logo=__i['logo'],
                    slider_image=__i['slider_image'] if 'slider_image' in __i.keys() else None,
                ))
            return __r
        except:
            return []

    @staticmethod
    def get_all_active_main_page(_text="", _unit=None):
        try:
            __body = {'name': {"$regex": _text}, "active": True}
            if _unit is not None:
                __body['unit'] = _unit
            __key = {'name': 1, 'image': 1, 'city': 1, 'industrial_town': 1, 'description': 1}
            __a = MongodbModel(body=__body, key=__key, collection="companies", sort="name", ascending=1, size=10).get_all_key_pagination()
            __r = []
            for __i in __a:
                __r.append(dict(
                    _id=__i['_id'],
                    name=__i['name'],
                    image=__i['image'] if "image" in __i.keys() else "",
                    city=ProvinceCityModel(_id=__i['city']).get_city()['name'],
                    industrial_town=IndustrialTownCompaniesModel(_id=__i['industrial_town']).get_one()['name'],
                    description=__i['description']
                ))
            return __r
        except:
            return []

    @staticmethod
    def get_by_unit(unit=None, size=8):
        try:
            __body = {'unit': unit, "active": True}
            __key = {'name': 1, 'image': 1, 'city': 1, 'industrial_town': 1, 'description': 1}
            __a = MongodbModel(body=__body, key=__key, collection="companies", sort="name", ascending=1, size=size).get_all_key_pagination()
            __r = []
            for __i in __a:
                __r.append(dict(
                    _id=__i['_id'],
                    name=__i['name'],
                    image=__i['image'] if "image" in __i.keys() else "",
                    city=ProvinceCityModel(_id=__i['city']).get_city()['name'],
                    industrial_town=IndustrialTownCompaniesModel(_id=__i['industrial_town']).get_one()['name'],
                    description=__i['description']
                ))
            return __r
        except:
            return []

    @staticmethod
    def get_one_main_page(__id=None):
        try:
            __body = {'_id': __id}
            __key = {'name': 1, 'image': 1, 'city': 1, 'industrial_town': 1, 'description': 1}
            __i = MongodbModel(body=__body, key=__key, collection="companies").get_one_key()
            return dict(
                _id=__i['_id'],
                name=__i['name'],
                image=__i['image'] if "image" in __i.keys() else "",
                city=ProvinceCityModel(_id=__i['city']).get_city()['name'],
                industrial_town=IndustrialTownCompaniesModel(_id=__i['industrial_town']).get_one()['name'],
                description=__i['description']
            )
        except:
            return False

    @staticmethod
    def get_similar(count=4, unit=None, _id=None):
        try:
            __body = {"active": True, "unit": unit, "image": {"$ne": None}, "_id": {"$ne": _id}}
            __key = {'name': 1, 'image': 1}
            __count = MongodbModel(body=__body, collection="companies").count()
            __rand = []
            __r = []
            while len(__rand) < count:
                _num = random.randint(0, __count - 1)
                if _num not in __rand:
                    __rand.append(_num)

            for i in __rand:
                __i = MongodbModel(body=__body, key=__key, size=i, collection="companies").get_all_key_random()
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
