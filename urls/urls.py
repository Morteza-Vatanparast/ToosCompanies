#!/usr/bin/env python
# -*- coding: utf-8 -*-
from handlers import base
from handlers import admin

__author__ = 'Morteza'

url_patterns = [
    ("/", base.IndexHandler, None, "index"),

    (r'^(?i)/Admin/Companies[/]?$', admin.AdminCompaniesHandler),
    (r'^/Admin/Companies', admin.AdminCompaniesHandler, None, "admin:companies"),

    (r'^(?i)/Admin/AddCompanies[/]?$', admin.AdminAddCompaniesHandler),
    (r'^/Admin/AddCompanies', admin.AdminAddCompaniesHandler, None, "admin:add_companies"),

    (r'^(?i)/Admin/EditCompanies[/]?([\w^/]+)?[/]?$', admin.AdminAddCompaniesHandler),
    (r'/Admin/EditCompanies', admin.AdminAddCompaniesHandler, None, 'admin:edit_companies'),
    (r'/Admin/EditCompanies/(id)', admin.AdminAddCompaniesHandler, None, 'admin:edit_companies_by_id'),

    (r'^(?i)/Admin/UnitCompanies[/]?$', admin.AdminUnitCompaniesHandler),
    (r'^/Admin/UnitCompanies', admin.AdminUnitCompaniesHandler, None, "admin:unit_companies"),

    (r'^(?i)/Admin/IndustrialTownsCompanies[/]?$', admin.AdminIndustrialTownCompaniesHandler),
    (r'^/Admin/IndustrialTownsCompanies', admin.AdminIndustrialTownCompaniesHandler, None, "admin:industrial_town_companies"),
]
