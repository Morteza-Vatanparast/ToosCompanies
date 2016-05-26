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
from models.mongodb.products import ProductsModel
from models.mongodb.province_city import ProvinceCityModel
from models.mongodb.tables import TablesModel
from models.mongodb.type_products import TypeProductsModel
from models.mongodb.unit_companies import UnitCompaniesModel

__author__ = 'Morteza'


class AdminCompaniesHandler(BaseHandler):
    def get(self, *args, **kwargs):
        companies = CompaniesModel().get_all()
        self.data['companies'] = []
        for i in companies:
            try:
                i['unit_name'] = UnitCompaniesModel(_id=i['_id']).get_one()['name']
            except:
                i['unit_name'] = u"وجود ندارد"
            i['status'] = i['status'] if 'status' in i.keys() else False
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
            province = int(self.get_argument('province', ''))
            city = int(self.get_argument('city', ''))
            unit = ObjectId(self.get_argument('unit', ''))
            industrial_town = ObjectId(self.get_argument('industrial_town', ''))
            if name != "" and description != "" and address != "" and phone != "" and fax != "" and site != "" \
                    and email != "" and ceo != "" and province != "" and city != "":
                main_page = True if main_page == "true" else False
                slider = True if slider == "true" else False
                active = True if active == "true" else False
                try:
                    logo = UploadPic(handler=self, name='logo', folder='logo').upload()[0]
                except:
                    logo = 'default.jpg'
                try:
                    images = UploadPic(handler=self, name='image', folder='image').upload()
                except:
                    images = []
                CompaniesModel(name=name, main_page=main_page, slider=slider, description=description, logo=logo,
                               images=images, unit=unit, active=active, industrial_town=industrial_town,
                               address=address, phone=phone, fax=fax, site=site, email=email,
                               province=province, city=city, ceo=ceo).insert()
            self.status = True
            self.write(self.result)
        except:
            self.write(self.error_result)


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
                    image = UploadPic(handler=self, name='image', folder='product').upload()[0]
                except:
                    image = 'default.jpg'
                ProductsModel(name=name, _type=_type, _sub_type=_sub_type, image=image).insert()
            self.status = True
            self.write(self.result)
        except:
            self.write(self.error_result)


class AdminEditProductsHandler(BaseHandler):
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