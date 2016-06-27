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
