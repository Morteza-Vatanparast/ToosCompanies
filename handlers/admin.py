#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from bson import ObjectId

from classes.get_url import GetUrl
from classes.soap import Soap
from classes.upload_pic import UploadPic
from handlers.base import BaseHandler
from models.mongodb.companies import CompaniesModel
from models.mongodb.industrial_town_companies import IndustrialTownCompaniesModel
from models.mongodb.orders import OrdersModel
from models.mongodb.products import ProductsModel
from models.mongodb.province_city import ProvinceCityModel
from models.mongodb.services import ServicesModel
from models.mongodb.tables import TablesModel
from models.mongodb.type_products import TypeProductsModel
from models.mongodb.unit_companies import UnitCompaniesModel

__author__ = 'Morteza'


class AdminDashboardHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('admin/dashboard.html', **self.data)


class AdminSearchCompaniesHandler(BaseHandler):
    def get(self, *args, **kwargs):
        try:
            name = args[0]
        except:
            name = "all"
        try:
            ceo = args[1]
        except:
            ceo = "all"
        try:
            owner = args[2]
        except:
            owner = "all"
        try:
            province = int(args[3])
        except:
            province = "all"
        try:
            city = int(args[4])
        except:
            city = "all"
        try:
            unit = ObjectId(args[5])
        except:
            unit = "all"
        try:
            industrial_town = ObjectId(args[6])
        except:
            industrial_town = "all"

        self.data['companies'] = CompaniesModel().admin_search(name=name, ceo=ceo, owner=owner, province=province,
                                                               city=city, unit=unit, industrial_town=industrial_town)
        self.data['this_name'] = name if name != "all" else ""
        self.data['this_ceo'] = ceo if ceo != "all" else ""
        self.data['this_owner'] = owner if owner != "all" else ""
        self.data['this_province'] = province if province != "all" else ""
        self.data['this_city'] = city if city != "all" else ""
        self.data['this_unit'] = unit if unit != "all" else ""
        self.data['this_industrial_town'] = industrial_town if industrial_town != "all" else ""
        self.data['units'] = UnitCompaniesModel().get_all()
        self.data['industrial_towns'] = IndustrialTownCompaniesModel().get_all()
        self.data['provinces'] = ProvinceCityModel().get_all_province()
        self.data['cities'] = ProvinceCityModel(province=province).get_all_city()
        self.render('admin/search_companies.html', **self.data)


class AdminShowCompaniesHandler(BaseHandler):
    def get(self, *args, **kwargs):
        try:
            company = args[0]
            if company is not None:
                company = ObjectId(company)
        except:
            company = None
        __company = CompaniesModel(_id=company).get_one()
        for i in __company['materials']:
            i['companies'] = CompaniesModel().get_by_products(i['_id'])
        for i in __company['products']:
            i['companies'] = CompaniesModel().get_by_materials(i['_id'])
        self.data['company'] = __company
        self.render('admin/show_companies.html', **self.data)


class AdminSearchProductsHandler(BaseHandler):
    def get(self, *args, **kwargs):
        try:
            name = args[0]
        except:
            name = "all"
        try:
            _type = ObjectId(args[1])
        except:
            _type = "all"
        try:
            _sub_type = ObjectId(args[2])
        except:
            _sub_type = "all"

        self.data['products'] = ProductsModel().admin_search(name=name, _type=_type, _sub_type=_sub_type)
        self.data['this_name'] = name if name != "all" else ""
        self.data['this_type'] = _type if _type != "all" else ""
        self.data['this_sub_type'] = _sub_type if _sub_type != "all" else ""
        self.data['type_products'] = TypeProductsModel().get_all()
        self.data['sub_type_products'] = TypeProductsModel(parent=_type).get_all_sub()
        self.render('admin/search_products.html', **self.data)


class AdminShowProductsHandler(BaseHandler):
    def get(self, *args, **kwargs):
        try:
            product = args[0]
            if product is not None:
                product = ObjectId(product)
        except:
            product = None
        __product = ProductsModel(_id=product).get_one()
        __product['companies_product'] = CompaniesModel().get_by_products(product)
        __product['companies_material'] = CompaniesModel().get_by_materials(product)
        self.data['product'] = __product
        self.render('admin/show_products.html', **self.data)


class AdminCompaniesHandler(BaseHandler):
    def get(self, *args, **kwargs):
        try:
            page = int(args[0])
        except:
            page = 1
        companies = CompaniesModel().get_all(page=page, size=30)
        count_all = CompaniesModel().count()
        self.data['companies'] = []
        self.data['pagination'] = dict(count_all=count_all, count_per_page=30, active_page=page)
        for i in companies:
            try:
                i['unit_name'] = UnitCompaniesModel(_id=i['unit']).get_one()['name']
            except:
                i['unit_name'] = u"وجود ندارد"
            i['active'] = i['active'] if 'active' in i.keys() else False
            self.data['companies'].append(i)
        self.render('admin/companies.html', **self.data)

    def delete(self, *args, **kwargs):
        try:
            company = self.get_argument('company', '')
            CompaniesModel(_id=ObjectId(company)).delete()
            self.status = True
            self.write(self.result)
        except:
            self.write(self.error_result)


class AdminAddCompaniesHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.data['units'] = UnitCompaniesModel().get_all()
        self.data['industrial_towns'] = IndustrialTownCompaniesModel().get_all()
        self.data['provinces'] = ProvinceCityModel().get_all_province()
        self.render('admin/add_companies.html', **self.data)

    def post(self, *args, **kwargs):
        try:
            name = self.get_argument('name', '')
            main_page = self.get_argument('main_page', 'false')
            slider = self.get_argument('slider', 'false')
            active = self.get_argument('active', 'false')
            description = self.get_argument('description', '')
            address = self.get_argument('address', '')
            phone = self.get_argument('phone', '')
            fax = self.get_argument('fax', '')
            site = self.get_argument('site', '')
            email = self.get_argument('email', '')
            ceo = self.get_argument('ceo', '')
            owner = self.get_argument('owner', '')
            province = int(self.get_argument('province', ''))
            city = int(self.get_argument('city', ''))
            unit = ObjectId(self.get_argument('unit', ''))
            industrial_town = ObjectId(self.get_argument('industrial_town', ''))
            if name != "" and description != "" and address != "" and phone != "" and fax != "" \
                    and province != "" and city != "":
                main_page = True if main_page == "true" else False
                slider = True if slider == "true" else False
                active = True if active == "true" else False
                try:
                    logo = UploadPic(handler=self, name='logo', folder='company_logo').upload()[0]
                except:
                    logo = 'default.jpg'
                try:
                    images = UploadPic(handler=self, name='image', folder='company_image').upload()
                except:
                    images = []
                CompaniesModel(name=name, main_page=main_page, slider=slider, description=description, logo=logo,
                               images=images, unit=unit, active=active, industrial_town=industrial_town,
                               address=address, phone=phone, fax=fax, site=site, email=email,
                               province=province, city=city, ceo=ceo, owner=owner).insert()
            self.status = True
            self.write(self.result)
        except:
            self.write(self.error_result)


class AdminEditCompaniesHandler(BaseHandler):
    def get(self, *args, **kwargs):
        try:
            company = args[0]
            if company is not None:
                company = ObjectId(company)
        except:
            company = None
        self.data['company'] = CompaniesModel(_id=company).get_one()
        self.data['units'] = UnitCompaniesModel().get_all()
        self.data['industrial_towns'] = IndustrialTownCompaniesModel().get_all()
        self.data['provinces'] = ProvinceCityModel().get_all_province()
        self.data['cities'] = ProvinceCityModel(province=self.data['company']['province']).get_all_city()
        self.render('admin/edit_companies.html', **self.data)

    def post(self, *args, **kwargs):
        try:
            company = args[0]
            if company is not None:
                company = ObjectId(company)
        except:
            company = None
        try:
            name = self.get_argument('name', '')
            main_page = self.get_argument('main_page', 'false')
            slider = self.get_argument('slider', 'false')
            active = self.get_argument('active', 'false')
            description = self.get_argument('description', '')
            address = self.get_argument('address', '')
            phone = self.get_argument('phone', '')
            fax = self.get_argument('fax', '')
            site = self.get_argument('site', '')
            email = self.get_argument('email', '')
            ceo = self.get_argument('ceo', '')
            owner = self.get_argument('owner', '')
            province = int(self.get_argument('province', ''))
            city = int(self.get_argument('city', ''))
            unit = ObjectId(self.get_argument('unit', ''))
            industrial_town = ObjectId(self.get_argument('industrial_town', ''))
            if name != "" and description != "" and address != "" and phone != "" and fax != "" \
                    and province != "" and city != "":
                main_page = True if main_page == "true" else False
                slider = True if slider == "true" else False
                active = True if active == "true" else False
                try:
                    logo = UploadPic(handler=self, name='logo', folder='company_logo').upload()[0]
                except:
                    logo = []
                try:
                    images = UploadPic(handler=self, name='image', folder='company_image').upload()
                except:
                    images = []
                CompaniesModel(_id=company, name=name, main_page=main_page, slider=slider, description=description, logo=logo,
                               images=images, unit=unit, active=active, industrial_town=industrial_town,
                               address=address, phone=phone, fax=fax, site=site, email=email,
                               province=province, city=city, ceo=ceo, owner=owner).update()
            self.status = True
            self.write(self.result)
        except:
            self.write(self.error_result)

    def delete(self, *args, **kwargs):
        try:
            company = args[0]
            if company is not None:
                company = ObjectId(company)
        except:
            company = None
        try:
            image = self.get_argument('image', '')
            CompaniesModel(_id=company).delete_image(image)
        except:
            pass
        self.status = True
        self.write(self.result)


class AdminUnitCompaniesHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.data['units'] = UnitCompaniesModel().get_all()
        self.render('admin/unit_companies.html', **self.data)

    def post(self, *args, **kwargs):
        try:
            action = self.get_argument('action', '')
            unit = self.get_argument('unit', '')

            if action == 'add':
                name = self.get_argument('name', '')
                UnitCompaniesModel(name=name).insert()
                self.status = True
            elif action == 'edit':
                name = self.get_argument('name', '')
                UnitCompaniesModel(_id=ObjectId(unit), name=name).update()
                self.status = True
            self.write(self.result)
        except:
            self.write(self.error_result)

    def delete(self, *args, **kwargs):
        try:
            unit = self.get_argument('unit', '')
            UnitCompaniesModel(_id=ObjectId(unit)).delete()
            self.status = True
            self.write(self.result)
        except:
            self.write(self.error_result)


class AdminIndustrialTownCompaniesHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.data['industrial_towns'] = IndustrialTownCompaniesModel().get_all()
        self.render('admin/industrial_town_companies.html', **self.data)

    def post(self, *args, **kwargs):
        try:
            action = self.get_argument('action', '')
            town = self.get_argument('town', '')

            if action == 'add':
                name = self.get_argument('name', '')
                IndustrialTownCompaniesModel(name=name).insert()
                self.status = True
            elif action == 'edit':
                name = self.get_argument('name', '')
                IndustrialTownCompaniesModel(_id=ObjectId(town), name=name).update()
                self.status = True
            self.write(self.result)
        except:
            self.write(self.error_result)

    def delete(self, *args, **kwargs):
        try:
            town = self.get_argument('town', '')
            IndustrialTownCompaniesModel(_id=ObjectId(town)).delete()
            self.status = True
            self.write(self.result)
        except:
            self.write(self.error_result)



class AdminTablesHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.data['tables'] = TablesModel().get_all()
        self.render('admin/tables.html', **self.data)

    def post(self):
        try:
            method = self.get_argument('method')
            if method == "AddTable":
                try:
                    trs = json.loads(self.get_argument('trs', '[]'))
                except:
                    trs = []
                _d = dict()
                self.check_sent_value("name", _d, "name", u"نام جدول را وارد کنید")
                self.check_sent_value("base_link", _d, "base_link", u"آدرس سایت را وارد کنید")
                self.check_sent_value("active", _d, "active")
                _d['active'] = True if 'active' in _d.keys() else False
                _d['trs'] = trs
                if not len(self.errors):
                    TablesModel().insert(**_d)
                    self.status = True
                else:
                    self.messages = self.errors
            if method == "EditTable":
                try:
                    trs = json.loads(self.get_argument('trs', '[]'))
                except:
                    trs = []
                _d = dict()
                self.check_sent_value("_id", _d, "_id", u"همه موارد را وارد کنید")
                self.check_sent_value("name", _d, "name", u"نام جدول را وارد کنید")
                self.check_sent_value("base_link", _d, "base_link", u"آدرس سایت را وارد کنید")
                self.check_sent_value("active", _d, "active")
                _d['active'] = True if 'active' in _d.keys() else False
                _d['trs'] = trs
                if not len(self.errors):
                    TablesModel(_id=ObjectId(_d['_id'])).update(**_d)
                    self.status = True
                else:
                    self.messages = self.errors

            elif method == "PreviewTable":
                table = self.get_argument('table', '')
                table = TablesModel(_id=ObjectId(table)).get_one()
                data = GetUrl(url=table['base_link']).value
                doc = Soap(document=data).soap
                for i in range(1, len(table['trs'])):
                    for td in table['trs'][i]['tds']:
                        try:
                            td['amount'] = doc.select_one(td['address']).text.encode('utf-8').strip()
                        except:
                            td['amount'] = 'نا مشخص'

                self.value = self.render_string("../ui_modules/template/admin/table.html", table=table)
                self.status = True

            elif method == "ShowEditTable":
                table = self.get_argument('table', '')
                self.value = TablesModel(_id=ObjectId(table)).get_one()
                self.value['_id'] = str(self.value['_id'])
                self.status = True

            elif method == "DeleteTable":
                table = self.get_argument('table', '')
                TablesModel(_id=ObjectId(table)).delete()
                self.status = True
            self.write(self.result)
        except:
            self.write(self.error_result)


class AdminTypeProductsHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.data['type_products'] = TypeProductsModel().get_all()
        self.render('admin/type_products.html', **self.data)

    def post(self):
        try:
            action = self.get_argument('action', '')

            if action == 'add':
                _type = dict()
                self.check_sent_value("type-name", _type, "name", u"نام موضوع را وارد کنید.")
                self.check_sent_value("type-parent", _type, "parent", u"مجموعه را وارد کنید.")
                if not len(self.errors):
                    if _type['parent'] == '0':
                        _type['parent'] = None
                    else:
                        _type['parent'] = ObjectId(_type['parent'])
                    TypeProductsModel(**_type).insert()
                    self.status = True
                else:
                    self.messages = self.errors
            elif action == 'edit':
                _type = dict()
                self.check_sent_value("type", _type, "_id", u"همه موارد را وارد کنید.")
                self.check_sent_value("type-name", _type, "name", u"نام موضوع را وارد کنید.")
                self.check_sent_value("type-parent", _type, "parent", u"مجموعه را وارد کنید.")
                if not len(self.errors):
                    if _type['parent'] == '0':
                        _type['parent'] = None
                    else:
                        _type['parent'] = ObjectId(_type['parent'])
                    _type['_id'] = ObjectId(_type['_id'])
                    TypeProductsModel(**_type).update()
                    self.status = True
                else:
                    self.messages = self.errors
            elif action == 'delete':
                _type = self.get_argument('type', '')
                TypeProductsModel(_id=ObjectId(_type)).delete()
                self.status = True
            else:
                self.messages = [u"عملیا ت با خطا مواجه شد"]

            self.write(self.result)
        except:
            self.write(self.error_result)


class AdminProductsHandler(BaseHandler):
    def get(self, *args, **kwargs):
        products = ProductsModel().get_all()
        self.data['products'] = []
        for i in products:
            try:
                i['type_name'] = TypeProductsModel(_id=i['type']).get_one()['name']
            except:
                i['type_name'] = u"وجود ندارد"
            try:
                i['sub_type_name'] = TypeProductsModel(_id=i['sub_type']).get_one()['name']
            except:
                i['sub_type_name'] = u"وجود ندارد"
            self.data['products'].append(i)
        self.render('admin/products.html', **self.data)

    def delete(self, *args, **kwargs):
        try:
            product = self.get_argument('product', '')
            ProductsModel(_id=ObjectId(product)).delete()
            self.status = True
            self.write(self.result)
        except:
            self.write(self.error_result)


class AdminAddProductsHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.data['type_products'] = TypeProductsModel().get_all()
        self.render('admin/add_products.html', **self.data)

    def post(self, *args, **kwargs):
        try:
            name = self.get_argument('name', '')
            try:
                _type = ObjectId(self.get_argument('type', ''))
                _sub_type = ObjectId(self.get_argument('sub_type', ''))
            except:
                _type = ""
                _sub_type = ""

            if name != "" and _type != "" and _sub_type != "":
                try:
                    image = UploadPic(handler=self, name='image', folder='product_image').upload()[0]
                except:
                    image = 'default.jpg'
                ProductsModel(name=name, _type=_type, _sub_type=_sub_type, image=image).insert()
            self.status = True
            self.write(self.result)
        except:
            self.write(self.error_result)


class AdminEditProductsHandler(BaseHandler):
    def get(self, *args, **kwargs):
        try:
            product = args[0]
            if product is not None:
                product = ObjectId(product)
        except:
            product = None
        self.data['type_products'] = TypeProductsModel().get_all()
        self.data['product'] = ProductsModel(_id=product).get_one()
        self.data['sub_type_products'] = TypeProductsModel(parent=self.data['product']['type']).get_all_sub()
        self.render('admin/edit_products.html', **self.data)

    def post(self, *args, **kwargs):
        try:
            product = args[0]
            if product is not None:
                product = ObjectId(product)
        except:
            product = None
        try:
            name = self.get_argument('name', '')
            try:
                _type = ObjectId(self.get_argument('type', ''))
                _sub_type = ObjectId(self.get_argument('sub_type', ''))
            except:
                _type = ""
                _sub_type = ""

            if name != "" and _type != "" and _sub_type != "":
                try:
                    image = UploadPic(handler=self, name='image', folder='product_image').upload()[0]
                except:
                    image = []
                ProductsModel(_id=product, name=name, _type=_type, _sub_type=_sub_type, image=image).update()
            self.status = True
            self.write(self.result)
        except:
            self.write(self.error_result)


class AdminCompaniesProductsHandler(BaseHandler):
    def get(self, *args, **kwargs):
        try:
            company = args[0]
            if company is not None:
                company = ObjectId(company)
        except:
            company = None

        __company = CompaniesModel(_id=ObjectId(company))
        self.data['companies'] = __company.get_all()
        self.data['this_company'] = __company.get_one()

        self.render('admin/companies_products.html', **self.data)

    def post(self, *args, **kwargs):
        try:
            company = args[0]
            if company is not None:
                company = ObjectId(company)
        except:
            company = None
        try:
            text = self.get_argument('text', '')
            action = self.get_argument('action', 'search')
            if action == 'search':
                l = []
                if text != '':
                    products = ProductsModel().get_all_by_like(text)
                    for item in products:
                        l.append({
                            'id': str(item['id']),
                            'name': item['name'],
                            'value': item['name'],
                            'label': item['name'],
                            'pic': item['image'],
                        })
                self.write(json.dumps({'status': 'ok', 'items': [f['name'] for f in l], 'full_item': l}))
            elif action == 'add':
                product = ObjectId(self.get_argument('product', ''))
                method = self.get_argument('method', '')
                if method == "product":
                    CompaniesModel(_id=company).add_product(product)
                    self.status = True
                elif method == "material":
                    CompaniesModel(_id=company).add_material(product)
                    self.status = True
                self.write(self.result)
            elif action == 'delete':
                product = ObjectId(self.get_argument('product', ''))
                method = self.get_argument('method', '')
                if method == "product":
                    CompaniesModel(_id=company).delete_product(product)
                    self.status = True
                elif method == "material":
                    CompaniesModel(_id=company).delete_material(product)
                    self.status = True
                self.write(self.result)
        except:
            self.write(self.error_result)


class AdminServicesHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.data['services'] = ServicesModel().get_all()
        self.render('admin/services.html', **self.data)


class AdminAddServicesHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('admin/add_services.html', **self.data)

    def post(self, *args, **kwargs):
        try:
            name = self.get_argument('name', '')
            description = self.get_argument('description', '')
            if name != "" and description != "":
                try:
                    image = UploadPic(handler=self, name='image', folder='service_image').upload()[0]
                except:
                    image = 'default.jpg'
                ServicesModel(name=name, description=description, image=image).insert()
            self.status = True
            self.write(self.result)
        except:
            self.write(self.error_result)


class AdminEditServicesHandler(BaseHandler):
    def get(self, *args, **kwargs):
        try:
            service = args[0]
            if service is not None:
                service = ObjectId(service)
        except:
            service = None
        self.data['service'] = ServicesModel(_id=service).get_one()
        self.render('admin/edit_services.html', **self.data)

    def post(self, *args, **kwargs):
        try:
            service = args[0]
            if service is not None:
                service = ObjectId(service)
        except:
            service = None
        try:
            name = self.get_argument('name', '')
            description = self.get_argument('description', '')
            if name != "" and description != "":
                try:
                    image = UploadPic(handler=self, name='image', folder='service_image').upload()[0]
                except:
                    image = []
                ServicesModel(_id=service, name=name, description=description, image=image).update()
            self.status = True
            self.write(self.result)
        except:
            self.write(self.error_result)


class AdminOrdersHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.data['orders'] = OrdersModel().get_all()
        self.render('admin/orders.html', **self.data)

    def delete(self, *args, **kwargs):
        try:
            order = self.get_argument('order', '')
            OrdersModel(_id=ObjectId(order)).delete()
            self.status = True
            self.write(self.result)
        except:
            self.write(self.error_result)
