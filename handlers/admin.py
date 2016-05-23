#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bson import ObjectId

from classes.upload_pic import UploadPic
from handlers.base import BaseHandler
from models.mongodb.companies import CompaniesModel
from models.mongodb.industrial_town_companies import IndustrialTownCompaniesModel
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


class AdminAddCompaniesHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.data['units'] = UnitCompaniesModel().get_all()
        self.data['industrial_towns'] = IndustrialTownCompaniesModel().get_all()
        self.render('admin/add_companies.html', **self.data)

    def post(self, *args, **kwargs):
        try:
            name = self.get_argument('name', '')
            main_page = self.get_argument('main_page', 'false')
            slider = self.get_argument('slider', 'false')
            active = self.get_argument('active', 'false')
            description = self.get_argument('description', '')
            unit = ObjectId(self.get_argument('unit', ''))
            industrial_town = ObjectId(self.get_argument('industrial_town', ''))
            if name != "" and description != "":
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
                CompaniesModel(name=name, main_page=main_page, slider=slider, description=description, logo=logo, images=images, unit=unit, active=active, industrial_town=industrial_town).insert()
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
