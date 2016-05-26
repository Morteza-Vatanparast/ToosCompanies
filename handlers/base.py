#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

import khayyam
import tornado.web
from models.mongodb.province_city import ProvinceCityModel
__author__ = 'Morteza'

class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.result = {'value': {}, 'status': False, 'messages': []}
        self.error_result = {'value': {}, 'status': False, 'messages': [u"عملیا ت با خطا مواجه شد"]}
        self.data = dict(
            title=""
        )
        self.errors = []

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
        self.render('index.html', **self.data)


class ProvinceCityHandler(BaseHandler):
    def post(self, *args, **kwargs):
        selected = ""
        try:
            province = int(self.get_argument('province', 0))
            cities = ProvinceCityModel(province=province).get_all_city()
            try:
                html = "<option value="">انتخاب کنید.</option>"
                __a = True
                for i in cities:
                    if __a:
                        selected = str(i['_id'])
                    html += "<option value=" + str(i['_id']) + ">" + i['name'].encode("utf-8") + "</option>"
                    __a = False
            except:
                html = "<option selected value="">انتخاب کنید.</option>"
            self.write(dict(html=html, selected=selected))
        except:
            self.write(dict(html="<option selected value="">انتخاب کنید.</option>", selected=selected))
