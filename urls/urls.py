#!/usr/bin/env python
# -*- coding: utf-8 -*-
from handlers import base
from handlers import admin

__author__ = 'Morteza'
url_patterns = [
    ("/", base.IndexHandler, None, "index"),
    ("/ProvinceCity", base.ProvinceCityHandler, None, "province_city"),
    ("/SubTypeProducts", base.SubTypeProductsHandler, None, "sub_type_products"),

    (r'^(?i)/Admin/Companies[/]?$', admin.AdminCompaniesHandler),
    (r'^/Admin/Companies', admin.AdminCompaniesHandler, None, "admin:companies"),

    (r'^(?i)/Admin/AddCompanies[/]?$', admin.AdminAddCompaniesHandler),
    (r'^/Admin/AddCompanies', admin.AdminAddCompaniesHandler, None, "admin:add_companies"),

    (r'^(?i)/Admin/EditCompanies[/]?([\w^/]+)?[/]?$', admin.AdminEditCompaniesHandler),
    (r'/Admin/EditCompanies', admin.AdminEditCompaniesHandler, None, 'admin:edit_companies'),
    (r'/Admin/EditCompanies/(id)', admin.AdminEditCompaniesHandler, None, 'admin:edit_companies_by_id'),

    (r'^(?i)/Admin/UnitCompanies[/]?$', admin.AdminUnitCompaniesHandler),
    (r'^/Admin/UnitCompanies', admin.AdminUnitCompaniesHandler, None, "admin:unit_companies"),

    (r'^(?i)/Admin/IndustrialTownsCompanies[/]?$', admin.AdminIndustrialTownCompaniesHandler),
    (r'^/Admin/IndustrialTownsCompanies', admin.AdminIndustrialTownCompaniesHandler, None, "admin:industrial_town_companies"),

    (r'^(?i)/Admin/Tables[/]?$', admin.AdminTablesHandler),
    (r'^/Admin/Tables', admin.AdminTablesHandler, None, "admin:tables"),

    (r'^(?i)/Admin/TypeProducts[/]?$', admin.AdminTypeProductsHandler),
    (r'^/Admin/TypeProducts', admin.AdminTypeProductsHandler, None, "admin:type_products"),

    (r'^(?i)/Admin/Products[/]?$', admin.AdminProductsHandler),
    (r'^/Admin/Products', admin.AdminProductsHandler, None, "admin:products"),

    (r'^(?i)/Admin/AddProducts[/]?$', admin.AdminAddProductsHandler),
    (r'^/Admin/AddProducts', admin.AdminAddProductsHandler, None, "admin:add_products"),

    (r'^(?i)/Admin/EditProducts[/]?([\w^/]+)?[/]?$', admin.AdminEditProductsHandler),
    (r'/Admin/EditProducts', admin.AdminEditProductsHandler, None, 'admin:edit_products'),
    (r'/Admin/EditProducts/(id)', admin.AdminEditProductsHandler, None, 'admin:edit_products_by_id'),

    (r'^(?i)/Admin/CompaniesProducts[/]?([\w^/]+)?[/]?$', admin.AdminCompaniesProductsHandler),
    (r'/Admin/CompaniesProducts', admin.AdminCompaniesProductsHandler, None, 'admin:companies_products'),
    (r'/Admin/CompaniesProducts/(id)', admin.AdminCompaniesProductsHandler, None, 'admin:companies_products_by_id'),
]

