#!/usr/bin/env python
# -*- coding: utf-8 -*-
from handlers import base
from handlers import admin

__author__ = 'Morteza'


url_patterns = [
    ("/", base.IndexHandler, None, "index"),
    ("/ProvinceCity", base.ProvinceCityHandler, None, "province_city"),
    ("/SubTypeProducts", base.SubTypeProductsHandler, None, "sub_type_products"),

    (r'^(?i)/Admin/Companies[/]?([\d^/]+)?[/]?$', admin.AdminCompaniesHandler),
    (r'/Admin/Companies', admin.AdminCompaniesHandler, None, 'admin:companies'),
    (r'/Admin/Companies/(page)', admin.AdminCompaniesHandler, None, 'admin:companies_by_page'),

    (r'^(?i)/Admin/Login[/]?$', admin.AdminLoginHandler),
    (r'^/Admin/Login', admin.AdminLoginHandler, None, "admin:login"),

    (r'^(?i)/Admin/Logout[/]?$', admin.AdminLogoutHandler),
    (r'^/Admin/Logout', admin.AdminLogoutHandler, None, "admin:logout"),

    (r'^(?i)/Admin/Dashboard[/]?$', admin.AdminDashboardHandler),
    (r'^/Admin/Dashboard', admin.AdminDashboardHandler, None, "admin:dashboard"),

    (r'^(?i)/Admin/Search/Companies/([^/]+)/([\w^/]+)/([\w^/]+)/([\w^/]+)/([\w^/]+)/([\w^/]+)/([\w^/]+)?[/]?$', admin.AdminSearchCompaniesHandler),
    (r'/Admin/Search/Companies', admin.AdminSearchCompaniesHandler, None, 'admin:search:companies'),
    (r'/Admin/Search/Companies/(name)/(ceo)/(owner)/(province)/(city)/(unit)/(industrial_town)', admin.AdminSearchCompaniesHandler, None, 'admin:search:companies_by_params'),

    (r'^(?i)/Admin/ShowCompanies[/]?([\w^/]+)?[/]?$', admin.AdminShowCompaniesHandler),
    (r'/Admin/ShowCompanies', admin.AdminShowCompaniesHandler, None, 'admin:show_companies'),
    (r'/Admin/ShowCompanies/(id)', admin.AdminShowCompaniesHandler, None, 'admin:show_companies_by_id'),

    (r'^(?i)/Admin/CompareCompanies/([\w^/]+)/([\w^/]+)?[/]?$', admin.AdminCompareCompaniesHandler),
    (r'/Admin/CompareCompanies', admin.AdminCompareCompaniesHandler, None, 'admin:compare_companies'),
    (r'/Admin/CompareCompanies/(id)/(id)', admin.AdminCompareCompaniesHandler, None, 'admin:compare_companies_by_id'),

    (r'^(?i)/Admin/Search/Products/([^/]+)/([\w^/]+)/([\w^/]+)?[/]?$', admin.AdminSearchProductsHandler),
    (r'/Admin/Search/Products', admin.AdminSearchProductsHandler, None, 'admin:search:products'),
    (r'/Admin/Search/Products/(name)/(type)/(sub_type)', admin.AdminSearchProductsHandler, None, 'admin:search:products_by_params'),

    (r'^(?i)/Admin/ShowProducts[/]?([\w^/]+)?[/]?$', admin.AdminShowProductsHandler),
    (r'/Admin/ShowProducts', admin.AdminShowProductsHandler, None, 'admin:show_products'),
    (r'/Admin/ShowProducts/(id)', admin.AdminShowProductsHandler, None, 'admin:show_products_by_id'),

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

    (r'^(?i)/Admin/Services[/]?$', admin.AdminServicesHandler),
    (r'^/Admin/Services', admin.AdminServicesHandler, None, "admin:services"),

    (r'^(?i)/Admin/AddServices[/]?$', admin.AdminAddServicesHandler),
    (r'^/Admin/AddServices', admin.AdminAddServicesHandler, None, "admin:add_services"),

    (r'^(?i)/Admin/EditServices[/]?([\w^/]+)?[/]?$', admin.AdminEditServicesHandler),
    (r'/Admin/EditServices', admin.AdminEditServicesHandler, None, 'admin:edit_services'),
    (r'/Admin/EditServices/(id)', admin.AdminEditServicesHandler, None, 'admin:edit_services_by_id'),

    (r'^(?i)/Admin/Orders[/]?$', admin.AdminOrdersHandler),
    (r'^/Admin/Orders', admin.AdminOrdersHandler, None, "admin:orders"),

    (r'^(?i)/Admin/SlideShow[/]?$', admin.AdminSlideShowHandler),
    (r'^/Admin/SlideShow', admin.AdminSlideShowHandler, None, "admin:slide_show"),

    (r'^(?i)/Admin/MainPage[/]?$', admin.AdminMainPageHandler),
    (r'^/Admin/MainPage', admin.AdminMainPageHandler, None, "admin:main_page"),

    (r'^(?i)/Admin/SlideShow/AddFormat[/]?([\w^/]+)?[/]?$', admin.AdminSlideShowAddFormatHandler),
    (r'/Admin/SlideShow/AddFormat', admin.AdminSlideShowAddFormatHandler, None, 'admin:slide_show:add_format'),
    (r'/Admin/SlideShow/AddFormat/(format)', admin.AdminSlideShowAddFormatHandler, None, 'admin:slide_show:add_format_by_format'),
]
