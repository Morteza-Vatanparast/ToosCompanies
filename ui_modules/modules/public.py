#!/usr/bin/env python
# -*- coding: utf-8 -*-
import khayyam
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
    def render(self, active="index"):
        return self.render_string('../ui_modules/template/navbar/navbar.html', active=active)


class Info(UIModule):
    def render(self):
        return self.render_string('../ui_modules/template/navbar/info.html')


class CompaniesBox(UIModule):
    def render(self, companies=None, position=""):
        if companies is None:
            companies = []
        return self.render_string('../ui_modules/template/companies_box/companies_box.html', companies=companies, position=position)


class AdminCompaniesBox(UIModule):
    def render(self, companies=None, position="", empty=False):
        if companies is None:
            companies = []
        return self.render_string('../ui_modules/template/companies_box/admin_companies_box.html', companies=companies,
                                  position=position, empty=empty)


class CompaniesBox1(UIModule):
    def render(self, company=None):
        return self.render_string('../ui_modules/template/companies_box/companies_box_1.html', company=company)


class AdminCompaniesBox1(UIModule):
    def render(self, company=None, empty=False):
        return self.render_string('../ui_modules/template/companies_box/admin_companies_box_1.html', company=company,
                                  empty=empty)


class CompaniesBox3(UIModule):
    def render(self, company_1=None, company_2=None, company_3=None):
        return self.render_string('../ui_modules/template/companies_box/companies_box_3.html',
                                  company_1=company_1, company_2=company_2, company_3=company_3)


class AdminCompaniesBox3(UIModule):
    def render(self, company_1=None, company_2=None, company_3=None, empty=False):
        return self.render_string('../ui_modules/template/companies_box/admin_companies_box_3.html',
                                  company_1=company_1, company_2=company_2, company_3=company_3, empty=empty)


class CompaniesSmallBoxRow(UIModule):
    def render(self, companies=None):
        return self.render_string('../ui_modules/template/companies_box/companies_small_box_row.html',
                                  companies=companies)


class AdminCompaniesSmallBoxRow(UIModule):
    def render(self, companies=None):
        return self.render_string('../ui_modules/template/companies_box/admin_companies_small_box_row.html',
                                  companies=companies)


class CompaniesSmallBox(UIModule):
    def render(self, prices=None):
        now_name = khayyam.JalaliDatetime().now().strftime("%A %d %B %Y")
        return self.render_string('../ui_modules/template/companies_box/companies_small_box.html',
                                  prices=prices, now_name=now_name)


class AdminCompaniesSmallBox(UIModule):
    def render(self, company=None, box=None):
        return self.render_string('../ui_modules/template/companies_box/admin_companies_small_box.html',
                                  company=company, box=box)


class NewsMediumBox(UIModule):
    def render(self, news=None):
        return self.render_string('../ui_modules/template/companies_box/news_medium_box.html',
                                  news=news)


class ServiceMediumBox(UIModule):
    def render(self, service=None):
        return self.render_string('../ui_modules/template/companies_box/service_medium_box.html',
                                  service=service)


class AdminCompaniesMediumBox(UIModule):
    def render(self, company=None, box=None):
        return self.render_string('../ui_modules/template/companies_box/admin_companies_medium_box.html',
                                  company=company, box=box)


class UnitSectionBoxes(UIModule):
    def render(self, unit_name=None, unit_id=None, _format=None, companies=None):
        if companies is None:
            companies = []
        return self.render_string('../ui_modules/template/companies_box/unit_section_boxes.html',
                                  unit_name=unit_name, unit_id=unit_id, _format=_format, companies=companies)


class AdminUnitSectionBoxes(UIModule):
    def render(self, unit_id=None, unit_name=None, _format=None, _sort=None, companies=None, empty=False):
        if companies is None:
            companies = []
        return self.render_string('../ui_modules/template/companies_box/admin_unit_section_boxes.html',
                                  unit_name=unit_name, unit_id=unit_id, _format=_format, _sort=_sort, empty=empty,
                                  companies=companies)


class ServiceBox(UIModule):
    def render(self, service=None):
        return self.render_string('../ui_modules/template/companies_box/service_box.html',
                                  service=service)


class NewsBox(UIModule):
    def render(self, news=None):
        return self.render_string('../ui_modules/template/companies_box/news_box.html',
                                  news=news)
