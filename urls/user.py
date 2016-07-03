#!/usr/bin/env python
# -*- coding: utf-8 -*-
from handlers import user

__author__ = 'Morteza'


user_url_patterns = {
    ("/", user.IndexHandler, None, "index"),

    (r'^(?i)/SearchCompanies/([^/]+)/([\w^/]+)/([\w^/]+)/([\w^/]+)?[/]?$', user.SearchCompaniesHandler),
    (r'/SearchCompanies', user.SearchCompaniesHandler, None, 'search_companies'),
    (r'/SearchCompanies/(name)/(unit)/(province)/(city)', user.SearchCompaniesHandler, None, 'search_companies_by_params'),

    (r'^(?i)/Company/([\w^/]+)?[/]?$', user.CompanyHandler),
    (r'/Company', user.CompanyHandler, None, 'company'),
    (r'/Company/(id)', user.CompanyHandler, None, 'company_by_id'),

    (r'^(?i)/Services[/]?$', user.ServicesHandler),
    (r'^/Services', user.ServicesHandler, None, "services"),

    (r'^(?i)/ContactUs[/]?$', user.ContactUsHandler),
    (r'^/ContactUs', user.ContactUsHandler, None, "contact_us"),

    (r'^(?i)/AboutUs[/]?$', user.AboutUsHandler),
    (r'^/AboutUs', user.AboutUsHandler, None, "about_us"),
}
