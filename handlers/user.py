#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

import khayyam
from bson import ObjectId
from tornado import gen

from handlers.base import UserBaseHandler
from models.mongodb.companies import CompaniesModel
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
        self.data['services'] = ServicesModel().get_all()
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