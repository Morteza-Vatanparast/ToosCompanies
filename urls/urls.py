#!/usr/bin/env python
# -*- coding: utf-8 -*-
from handlers import base

__author__ = 'Morteza'

url_patterns = [
    ("/", base.IndexHandler, None, "index"),
]
