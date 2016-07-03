#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tornado.web import UIModule

from models.mongodb.companies import CompaniesModel
from models.mongodb.setting import SettingModel

__author__ = 'Morteza'


class SlideShow(UIModule):
    def render(self, *args, **kwargs):
        _formats = SettingModel().get_format_slide_show()
        for i in _formats:
            for j in i['areas']:
                j['company'] = CompaniesModel(_id=j['company']).get_one()
        return self.render_string('../ui_modules/template/slide_show/slide_show.html', _formats=_formats)


class Slider(UIModule):
    def render(self, image=None, images=None, count=0):
        if images is None:
            images = []
        return self.render_string('../ui_modules/template/slide_show/slider.html', image=image, images=images, count=count)


class SlideShowFormat1(UIModule):
    def render(self, admin=False, _format=None, _slide=None, all_slide=None):
        if admin:
            return self.render_string('../ui_modules/template/slide_show/admin_format_1.html')
        return self.render_string('../ui_modules/template/slide_show/format_1.html', _format=_format, _slide=_slide, all_slide=all_slide)


class SlideShowFormat2(UIModule):
    def render(self, admin=False, _format=None, _slide=None, all_slide=None):
        if admin:
            return self.render_string('../ui_modules/template/slide_show/admin_format_2.html')
        return self.render_string('../ui_modules/template/slide_show/format_2.html', _format=_format, _slide=_slide, all_slide=all_slide)


class SlideShowFormat3(UIModule):
    def render(self, admin=False, _format=None, _slide=None, all_slide=None):
        if admin:
            return self.render_string('../ui_modules/template/slide_show/admin_format_3.html')
        return self.render_string('../ui_modules/template/slide_show/format_3.html', _format=_format, _slide=_slide, all_slide=all_slide)


class SlideShowFormat4(UIModule):
    def render(self, admin=False, _format=None, _slide=None, all_slide=None):
        if admin:
            return self.render_string('../ui_modules/template/slide_show/admin_format_4.html')
        return self.render_string('../ui_modules/template/slide_show/format_4.html', _format=_format, _slide=_slide, all_slide=all_slide)
