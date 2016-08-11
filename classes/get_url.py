#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import urllib2
import urlparse

import functools
from threading import Thread

__author__ = 'Morteza'


def time_out(__timeout=50):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = [Exception('function [%s] timeout [%s seconds] exceeded!' % (func.__name__, __timeout))]

            def new_func():
                try:
                    res[0] = func(*args, **kwargs)
                except Exception, e:
                    res[0] = e
            t = Thread(target=new_func)
            t.daemon = True
            try:
                t.start()
                t.join(__timeout)
            except Exception, je:
                print 'error starting thread'
                raise je
            ret = res[0]
            if isinstance(ret, BaseException):
                raise ret
            return ret
        return wrapper
    return deco


class GetUrl:
    def __init__(self, url):
        self.url = url
        self.value = False
        try:
            self.read_url()
        except:
            self.value = False

    @staticmethod
    def url_encode_none_ascii(__url):
        return re.sub('[\x80-\xFF]', lambda c: '%%%02x' % ord(c.group(0)), __url)

    def iri_to_uri(self, _enc):
        try:
            parts = urlparse.urlparse(self.url)
            return urlparse.urlunparse(
                part.encode('idna') if part_i == 1 else self.url_encode_none_ascii(part if _enc else part.encode('utf-8'))
                for part_i, part in enumerate(parts)
            )
        except:
            return False

    def clean_url(self):
        return self.url.replace("'", "").replace('"', '')

    def get_url(self, __url):
        try:
            response = urllib2.urlopen(__url)
            self.value = response.read()
            return True
        except:
            return False

    @time_out()
    def read_url(self):
        try:
            self.clean_url()
            if not self.get_url(self.iri_to_uri(False)):
                if not self.get_url(self.iri_to_uri(True)):
                    self.get_url(self.url)
        except:
            pass
