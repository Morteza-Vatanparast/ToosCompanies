from models.mongodb.base_model import MongodbModel
from models.mongodb.products import ProductsModel


class CompaniesModel:
    def __init__(self, _id=None, name=None, main_page=None, slider=None, description=None, logo=None, images=None,
                 unit=None, active=None, industrial_town=None, address=None, phone=None, fax=None, site=None,
                 email=None, province=None, city=None, ceo=None, mobile=None, mobile2=None, products=None, materials=None):
        self.id = _id
        self.name = name
        self.main_page = main_page
        self.slider = slider
        self.description = description
        self.logo = logo
        self.images = images
        self.unit = unit
        self.active = active
        self.industrial_town = industrial_town
        self.address = address
        self.phone = phone
        self.mobile = mobile
        self.mobile2 = mobile2
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

    def insert(self):
        try:
            __body = {
                "name": self.name,
                "main_page": self.main_page,
                "slider": self.slider,
                "description": self.description,
                "logo": self.logo,
                "images": self.images,
                "unit": self.unit,
                "industrial_town": self.industrial_town,
                "address": self.address,
                "phone": self.phone,
                "mobile": self.mobile,
                "mobile2": self.mobile2,
                "fax": self.fax,
                "site": self.site,
                "email": self.email,
                "province": self.province,
                "city": self.city,
                "ceo": self.ceo,
                "active": self.active,
                "products": self.products,
                "materials": self.materials
            }
            MongodbModel(body=__body, collection="companies").insert()
            return True
        except:
            return False

    @staticmethod
    def get_all():
        try:
            __body = {}
            return MongodbModel(body=__body, collection="companies").get_all()
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
                    "unit": self.unit,
                    "industrial_town": self.industrial_town,
                    "address": self.address,
                    "phone": self.phone,
                    "mobile": self.mobile,
                    "mobile2": self.mobile2,
                    "fax": self.fax,
                    "site": self.site,
                    "email": self.email,
                    "province": self.province,
                    "city": self.city,
                    "ceo": self.ceo,
                    "active": self.active,
                    "products": self.products
                }
            }
            if len(self.logo):
                __body['$set']['logo'] = self.logo
            if len(self.images):
                images = self.get_one()['images']
                __body['$set']['images'] = images + self.images
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

    def get_one(self):
        try:
            __body = {"_id": self.id}
            __c = MongodbModel(body=__body, collection="companies").get_one()

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
            return dict(
                _id=__get("_id", None),
                name=__get("name", ""),
                main_page=__get("main_page", False),
                slider=__get("slider", False),
                active=__get("active", False),
                logo=__get("logo", ""),
                address=__get("address", ""),
                phone=__get("phone", ""),
                fax=__get("fax", ""),
                site=__get("site", ""),
                email=__get("email", ""),
                ceo=__get("ceo", ""),
                province=__get("province", ""),
                city=__get("city", ""),
                unit=__get("unit", ""),
                industrial_town=__get("industrial_town", ""),
                images=__get("images", []),
                materials=materials,
                products=products,
                description=__get("description", "")
            )
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

    def get_materials(self):
        try:
            __body = {"_id": self.id}
            __key = {"materials": 1}
            __c = MongodbModel(body=__body, key=__key, collection="companies").get_one_key()
            return __c['materials']
        except:
            return []
