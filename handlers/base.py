#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

import functools
import khayyam
import tornado.web
from bson import ObjectId
from pycket.notification import NotificationMixin
from pycket.session import SessionMixin

from models.mongodb.province_city import ProvinceCityModel
from models.mongodb.type_products import TypeProductsModel

__author__ = 'Morteza'


def admin_authentication():
    def f(func):
        @functools.wraps(func)
        def func_wrapper(self, *args, **kwargs):
            if not self.admin_is_authenticated():
                self.redirect(self.reverse_url("admin:login"))
                return
            return func(self, *args, **kwargs)
        return func_wrapper
    return f


class BaseHandler(tornado.web.RequestHandler, SessionMixin, NotificationMixin):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.result = {'value': {}, 'status': False, 'messages': []}
        self.error_result = {'value': {}, 'status': False, 'messages': [u"عملیا ت با خطا مواجه شد"]}
        self.data = dict(
            title=""
        )
        self.errors = []

    @property
    def current_admin(self):
        return self.session.get('current_admin_toos', None)

    @current_admin.setter
    def current_admin(self, current_admin):
        self.session.set('current_admin_toos', current_admin)

    def admin_is_authenticated(self):
        if self.current_admin is not None:
            return True
        return False

    @property
    def value(self):
        return self.result['value']

    @value.setter
    def value(self, value):
        self.result['value'] = value

    @property
    def status(self):
        return self.result['status']

    @status.setter
    def status(self, status):
        self.result['status'] = status

    @property
    def messages(self):
        return self.result['messages']

    @messages.setter
    def messages(self, messages):
        self.result['messages'] = messages

    def check_sent_value(self, val, _table, _field, error_msg=None, nullable=False, default=None):
        vl = self.get_argument(val, None)

        if vl is not None:
            if not nullable:
                if vl != '':
                    _table[_field] = vl
                else:
                    if error_msg:
                        self.errors.append(error_msg)
            else:
                _table[_field] = vl if vl else default
        else:
            if error_msg:
                self.errors.append(error_msg)


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.data['__now'] = datetime.datetime.now()
        self.data['__now_name'] = khayyam.JalaliDatetime().now().strftime("%A - %d %B %Y")
        self.render('index_2.html', **self.data)


class ProvinceCityHandler(BaseHandler):
    def post(self, *args, **kwargs):
        selected = ""
        try:
            province = int(self.get_argument('province', 0))
            _all = self.get_argument('all', 'false')
            _all = True if _all == 'true' else False
            cities = ProvinceCityModel(province=province).get_all_city()
            html = '<option value="all">همه شهر ها</option>' if _all else '<option value="">انتخاب کنید.</option>'
            try:
                __a = True
                for i in cities:
                    if __a:
                        selected = str(i['_id'])
                    html += "<option value=" + str(i['_id']) + ">" + i['name'].encode("utf-8") + "</option>"
                    __a = False
            except:
                pass
            self.write(dict(html=html, selected=selected))
        except:
            self.write(dict(html="<option selected value="">انتخاب کنید.</option>", selected=selected))


class SubTypeProductsHandler(BaseHandler):
    def post(self, *args, **kwargs):
        selected = ""
        try:
            _type = ObjectId(self.get_argument('type', 0))
            _all = self.get_argument('all', 'false')
            _all = True if _all == 'true' else False
            _sub_types = TypeProductsModel(parent=ObjectId(_type)).get_all_sub()
            html = '<option value="all">همه زیر مجموعه ها</option>' if _all else '<option value="">انتخاب کنید.</option>'
            try:
                __a = True
                for i in _sub_types:
                    if __a:
                        selected = str(i['_id'])
                    html += "<option value=" + str(i['_id']) + ">" + i['name'].encode("utf-8") + "</option>"
                    __a = False
            except:
                pass
            self.write(dict(html=html, selected=selected))
        except:
            self.write(dict(html="<option selected value="">انتخاب کنید.</option>", selected=selected))
