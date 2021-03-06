#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import datetime

__author__ = 'Morteza'


class Config:
    def __init__(self):
        self.applications_root = os.path.join(os.path.dirname(__file__), "")
        self.domain = '37.59.92.3:8099'

        self.SESSION_TIME = datetime.timedelta(seconds=3600)

        self.web = {
            'port': 8099,
            'server_ip': '127.0.0.1',
            'server_path': os.path.join(self.applications_root, ''),
            'mysql': {
                'host': '127.0.0.1',
                'db': '',
                'user': 'root',
                'password': '',
                'port': 3306,
            },

            'template_address': os.path.join(os.path.dirname(__file__), "templates"),
            'static_address': os.path.join(os.path.dirname(__file__), "static"),
        }

        self.mongodb = {
            'host': '127.0.0.1',
            'db': 'ToosCompanies',
            'port': 27017,
        }

        self.global_config = {
            'cookie_secret': "Gy8tgGsVvz3n#(3eDeW poY667^&A95j6hf5_4cvv 2Y&sAl",
            'login_url': 'http://{0}:{1}/login'.format(self.web['server_ip'], self.web['port']),
            'logout_url': 'http://{0}:{1}/logout'.format(self.web['server_ip'], self.web['port']),
            'redis': {
                'host': '127.0.0.1',
                'port': 6379,
                'password': "",
                'db_sessions': 8,
                'db_notifications': 9,
            },
        }