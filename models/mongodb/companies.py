from models.mongodb.base_model import MongodbModel


class CompaniesModel:
    def __init__(self, _id=None, name=None, main_page=None, slider=None, description=None, logo=None, images=None,
                 unit=None, active=None, industrial_town=None, address=None, phone=None, fax=None, site=None,
                 email=None, province=None, city=None, ceo=None, mobile=None, mobile2=None, products=None):
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
        self.products = products
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
                "products": self.products
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
                    "name": self.name
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
