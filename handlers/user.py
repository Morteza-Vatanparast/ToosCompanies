#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os

import khayyam
import qrcode
from bson import ObjectId
from tornado import gen

from config import Config
from handlers.base import UserBaseHandler
from models.mongodb.companies import CompaniesModel
from models.mongodb.contact_us import ContactUsModel
from models.mongodb.province_city import ProvinceCityModel
from models.mongodb.services import ServicesModel
from models.mongodb.setting import SettingModel
from models.mongodb.unit_companies import UnitCompaniesModel

__author__ = 'Morteza'


class IndexHandler(UserBaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        self.data['__now'] = datetime.datetime.now()
        self.data['__now_name'] = khayyam.JalaliDatetime().now().strftime("%A - %d %B %Y")
        self.data['main_page'] = SettingModel().get_main_page()
        self.data['services'] = ServicesModel().get_all_main_page()
        self.render('user/index.html', **self.data)


class SearchCompaniesHandler(UserBaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        main = True
        try:
            name = args[0]
            main = False
        except:
            name = "all"
        try:
            unit = ObjectId(args[1])
            main = False
        except:
            unit = "all"
        try:
            province = int(args[2])
            main = False
        except:
            province = "all"
        try:
            city = int(args[3])
            main = False
        except:
            city = "all"

        self.data['count'] = 0
        self.data['companies'] = []
        if not main:
            self.data['companies'] = CompaniesModel().user_search(name=name, province=province, city=city, unit=unit)
            self.data['count'] = CompaniesModel().user_search_count(name=name, province=province, city=city, unit=unit)
        self.data['this_name'] = name if name != "all" else ""

        self.data['this_province'] = province if province != "all" else ""
        self.data['this_city'] = city if city != "all" else ""
        self.data['this_unit'] = unit if unit != "all" else ""
        self.data['units'] = UnitCompaniesModel().get_all()
        self.data['provinces'] = ProvinceCityModel().get_all_province()
        self.data['cities'] = ProvinceCityModel(province=province).get_all_city()
        self.render('user/search_companies.html', **self.data)

    def post(self, *args, **kwargs):
        try:
            name = args[0]
        except:
            name = "all"
        try:
            unit = ObjectId(args[1])
        except:
            unit = "all"
        try:
            province = int(args[2])
        except:
            province = "all"
        try:
            city = int(args[3])
        except:
            city = "all"
        try:
            page = int(self.get_argument('page', 1))
            companies = CompaniesModel().user_search(name=name, province=province, city=city, unit=unit, page=page)
            html = ''
            for _comp in companies:
                html += '<div class="col-md-4">'
                html += self.render_string('../ui_modules/template/companies_box/companies_small_box.html',
                                           company=_comp)
                html += '</div>'
            self.write({'count': len(companies), 'status': 'success', 'data': html, 'page': int(page) + 1})
        except:
            self.write({'status': 'failed', 'data': '', 'page': 0})


class ServicesHandler(UserBaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        self.data['services'] = ServicesModel().get_all_pagination()
        self.data['count'] = ServicesModel().count()
        self.render('user/services.html', **self.data)

    def post(self, *args, **kwargs):
        try:
            page = int(self.get_argument('page', 1))
            services = ServicesModel().get_all_pagination(page=page)
            html = ''
            for _s in services:
                html += '<div class="col-md-4 margin-top-10">'
                html += self.render_string('../ui_modules/template/companies_box/service_box.html',
                                           service=_s)
                html += '</div>'
            self.write({'count': len(services), 'status': 'success', 'data': html, 'page': int(page) + 1})
        except:
            self.write({'status': 'failed', 'data': '', 'page': 0})


class ContactUsHandler(UserBaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        self.render('user/contact_us.html', **self.data)

    def post(self, *args, **kwargs):
        try:
            name = self.get_argument('name', '')
            email = self.get_argument('email', '')
            email = email if email != "" else None
            description = self.get_argument('description', '')
            if name == "" or description == "":
                self.write('empty')
                return
            if ContactUsModel().is_duplicate(self.secure_cookie):
                self.write('duplicate')
                return
            ContactUsModel(name=name, email=email, description=description, secure_cookie=self.secure_cookie).insert()
            self.write('success')
        except:
            self.write('error')


class AboutUsHandler(UserBaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        self.render('user/about_us.html', **self.data)


class CompanyHandler(UserBaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        try:
            company = args[0]
            if company is not None:
                company = ObjectId(company)
        except:
            company = None
        self.data['company'] = CompaniesModel(_id=company).get_one()
        self.data['similar_companies'] = CompaniesModel(_id=company).get_similar(unit=self.data['company']['unit'], _id=self.data['company']['_id'])

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(Config().domain + self.reverse_url('company_by_id', str(self.data['company']['_id'])))
        qr.make(fit=True)
        img = qr.make_image()
        _folder = os.path.join(Config().applications_root, 'static', 'images', 'company_qr_code')
        photo_name = str(self.data['company']['_id']) + '.jpg'
        img.save(os.path.join(_folder, photo_name))
        self.render('user/company.html', **self.data)