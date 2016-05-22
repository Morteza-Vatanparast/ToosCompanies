#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bson import ObjectId

from classes.upload_pic import UploadPic
from handlers.base import BaseHandler
from models.mongodb.companies import CompaniesModel
from models.mongodb.unit_companies import UnitCompaniesModel

__author__ = 'Morteza'


class AdminCompaniesHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('index.html', **self.data)


class AdminAddCompaniesHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.data['units'] = UnitCompaniesModel().get_all()
        self.render('admin/add_companies.html', **self.data)

    def post(self, *args, **kwargs):
        try:
            name = self.get_argument('name', '')
            main_page = self.get_argument('main_page', 'false')
            slider = self.get_argument('slider', 'false')
            description = self.get_argument('description', '')
            unit = ObjectId(self.get_argument('unit', ''))
            if name != "" and description != "":
                main_page = True if main_page == "true" else False
                slider = True if slider == "true" else False
                try:
                    logo = UploadPic(handler=self, name='logo', folder='logo').upload()[0]
                except:
                    logo = 'default.jpg'
                try:
                    images = UploadPic(handler=self, name='image', folder='image').upload()
                except:
                    images = []
                CompaniesModel(name=name, main_page=main_page, slider=slider, description=description, logo=logo, images=images, unit=unit).insert()
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