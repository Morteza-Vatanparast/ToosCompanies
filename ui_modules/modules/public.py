#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tornado.web import UIModule

__author__ = 'Morteza'


class Pagination(UIModule):
    def render(self, count_all=None, count_per_page=None, active_page=None):
        try:
            return self.render_string('../ui_modules/template/pagination/pagination.html', count_all=count_all, count_per_page=count_per_page, active_page=active_page)
        except:
            return ''


class Footer(UIModule):
    def render(self):
        return self.render_string('../ui_modules/template/footer/footer.html')


class NavBar(UIModule):
    def render(self):
        return self.render_string('../ui_modules/template/navbar/navbar.html')


class CompaniesBox(UIModule):
    def render(self, companies=None, position=""):
        if companies is None:
            companies = []
        return self.render_string('../ui_modules/template/companies_box/companies_box.html', companies=companies, position=position)


class CompaniesBox1(UIModule):
    def render(self, company=None):
        return self.render_string('../ui_modules/template/companies_box/companies_box_1.html', company=company)


class CompaniesBox3(UIModule):
    def render(self, company_1=None, company_2=None, company_3=None):
        return self.render_string('../ui_modules/template/companies_box/companies_box_3.html',
                                  company_1=company_1, company_2=company_2, company_3=company_3)
