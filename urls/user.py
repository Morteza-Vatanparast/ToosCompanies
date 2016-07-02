#!/usr/bin/env python
# -*- coding: utf-8 -*-
from handlers import user

__author__ = 'Morteza'


user_url_patterns = {
    ("/", user.IndexHandler, None, "index"),

    (r'^(?i)/SearchCompanies/([^/]+)/([\w^/]+)/([\w^/]+)/([\w^/]+)?[/]?$', user.SearchCompaniesHandler),
    (r'/SearchCompanies', user.SearchCompaniesHandler, None, 'search_companies'),
    (r'/SearchCompanies/(name)/(unit)/(province)/(city)', user.SearchCompaniesHandler, None, 'search_companies_by_params'),
}
