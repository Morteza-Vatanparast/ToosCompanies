#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os

import khayyam
import qrcode
from bson import ObjectId
from tornado import gen

from classes.upload_pic import UploadPic
from config import Config
from handlers.base import UserBaseHandler
from models.mongodb.companies import CompaniesModel
from models.mongodb.contact_us import ContactUsModel
from models.mongodb.industrial_town_companies import IndustrialTownCompaniesModel
from models.mongodb.news import NewsModel
from models.mongodb.orders import OrdersModel
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
        self.data['services_slider'] = ServicesModel().get_all_main_page_slider()
        self.data['news'] = NewsModel().get_all_main_page()
        self.data['news_slider'] = NewsModel().get_all_main_page_slider()
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


class AllNewsHandler(UserBaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        self.data['all_news'] = NewsModel().get_all_pagination()
        self.data['count'] = NewsModel().count()
        self.render('user/all_news.html', **self.data)

    def post(self, *args, **kwargs):
        try:
            page = int(self.get_argument('page', 1))
            all_news = NewsModel().get_all_pagination(page=page)
            html = ''
            for _s in all_news:
                html += '<div class="col-md-4 margin-top-10">'
                html += self.render_string('../ui_modules/template/companies_box/news_box.html',
                                           news=_s)
                html += '</div>'
            self.write({'count': len(all_news), 'status': 'success', 'data': html, 'page': int(page) + 1})
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
            phone = self.get_argument('phone', '')
            email = email if email != "" else None
            phone = phone if phone != "" else None
            description = self.get_argument('description', '')
            if name == "" or description == "":
                self.write('empty')
                return
            if ContactUsModel().is_duplicate(self.secure_cookie):
                self.write('duplicate')
                return
            ContactUsModel(name=name, email=email, phone=phone, description=description, secure_cookie=self.secure_cookie).insert()
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
        if not os.path.exists(_folder):
            os.makedirs(_folder)
        photo_name = str(self.data['company']['_id']) + '.jpg'
        img.save(os.path.join(_folder, photo_name))
        self.render('user/company.html', **self.data)


class NewsHandler(UserBaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        try:
            news = args[0]
            if news is not None:
                news = ObjectId(news)
        except:
            news = None
        self.data['news'] = NewsModel(_id=news).get_one()
        self.render('user/news.html', **self.data)


class ServiceHandler(UserBaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        try:
            service = args[0]
            if service is not None:
                service = ObjectId(service)
        except:
            service = None
        self.data['service'] = ServicesModel(_id=service).get_one()
        self.data['similar_services'] = ServicesModel(_id=service).get_similar(_id=self.data['service']['_id'])
        self.render('user/service.html', **self.data)

    def post(self, *args, **kwargs):
        try:
            service = args[0]
            if service is not None:
                service = ObjectId(service)
        except:
            service = None
        try:
            name = self.get_argument('name', '')
            phone = self.get_argument('phone', '')
            count = self.get_argument('count', '')
            address = self.get_argument('address', '')
            description = self.get_argument('description', '')
            if name == "" or phone == "" or count == "" or address == "" or description == "" or service is None:
                self.write('empty')
                return
            if OrdersModel().is_duplicate(self.secure_cookie):
                self.write('duplicate')
                return
            OrdersModel(name=name, phone=phone, count=count, address=address, description=description, service=service,
                        secure_cookie=self.secure_cookie).insert()
            self.write('success')
        except:
            self.write('error')


class RegisterCompaniesHandler(UserBaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        self.data['units'] = UnitCompaniesModel().get_all()
        self.data['industrial_towns'] = IndustrialTownCompaniesModel().get_all()
        self.data['provinces'] = ProvinceCityModel().get_all_province()
        self.render('user/register_companies.html', **self.data)

    @gen.coroutine
    def post(self, *args, **kwargs):
        try:
            name = self.get_argument('name', '')
            description = self.get_argument('description', '')
            about = self.get_argument('about', '')
            address = self.get_argument('address', '')
            phone = self.get_argument('phone', '')
            phone2 = self.get_argument('phone2', '')
            mobile = self.get_argument('mobile', '')
            fax = self.get_argument('fax', '')
            site = self.get_argument('site', '')
            email = self.get_argument('email', '')
            ceo = self.get_argument('ceo', '')
            coordinator = self.get_argument('coordinator', '')
            mobile_coordinator = self.get_argument('mobile_coordinator', '')
            products_info = self.get_argument('products_info', '')
            materials_info = self.get_argument('materials_info', '')
            owner = self.get_argument('owner', '')
            province = int(self.get_argument('province', ''))
            city = int(self.get_argument('city', ''))
            unit = ObjectId(self.get_argument('unit', ''))
            industrial_town = ObjectId(self.get_argument('industrial_town', ''))

            if name != "" and unit != "" and industrial_town != ""\
                    and province != "" and city != "":
                main_page = False
                slider = True
                active = False
                try:
                    logo = UploadPic(handler=self, folder='company_logo').upload_from_cropper(base64_str=[self.get_argument('logo', '')])[0]
                except:
                    logo = False
                if logo is False:
                    self.messages = ['لوگو شرکت را انتخاب کنید.']
                    self.status = False
                    self.write(self.result)
                    return
                try:
                    image = UploadPic(handler=self, folder='company_image').upload_from_cropper(base64_str=[self.get_argument('image', '')])[0]
                except:
                    image = False
                if image is False:
                    self.messages = ['عکس شرکت را انتخاب کنید.']
                    self.status = False
                    self.write(self.result)
                    return
                try:
                    slider_image = UploadPic(handler=self, folder='company_slider').upload_from_cropper(base64_str=[self.get_argument('slider_image', '')])[0]
                except:
                    slider_image = False
                if slider_image is False:
                    self.messages = ['اسلایدر شرکت را انتخاب کنید.']
                    self.status = False
                    self.write(self.result)
                    return
                try:
                    try:
                        images = self.request.arguments['images']
                    except:
                        images = []
                    images = UploadPic(handler=self, name='images', folder='company_images').upload_from_cropper(count=4, base64_str=images)
                except:
                    images = []
                CompaniesModel(name=name, main_page=main_page, slider=slider, description=description, logo=logo,
                               images=images, unit=unit, active=active, industrial_town=industrial_town,
                               address=address, phone=phone, phone2=phone2, fax=fax, site=site, email=email,
                               province=province, city=city, ceo=ceo, coordinator=coordinator,
                               mobile_coordinator=mobile_coordinator, products_info=products_info,
                               materials_info=materials_info, owner=owner,
                               slider_image=slider_image, image=image, mobile=mobile, about=about).insert(register=True)
            self.status = True
            self.write(self.result)
        except:
            self.write(self.error_result)