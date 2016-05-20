#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
__author__ = 'Morteza'


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')