#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urls.admin import admin_url_patterns
from urls.user import user_url_patterns
from handlers import base

__author__ = 'Morteza'


url_patterns = {
    ("/ProvinceCity", base.ProvinceCityHandler, None, "province_city"),
    ("/SubTypeProducts", base.SubTypeProductsHandler, None, "sub_type_products")
}.union(
    admin_url_patterns,
    user_url_patterns
)
