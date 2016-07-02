#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urls import admin
from urls import user
from handlers import base

__author__ = 'Morteza'


url_patterns = [
    ("/ProvinceCity", base.ProvinceCityHandler, None, "province_city"),
    ("/SubTypeProducts", base.SubTypeProductsHandler, None, "sub_type_products")
] + admin.url_patterns + user.url_patterns
