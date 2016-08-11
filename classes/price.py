#!/usr/bin/env python
# -*- coding: utf-8 -*-
from classes.get_url import GetUrl
from classes.soap import Soap

__author__ = 'Morteza'


class PriceClass:
    def __init__(self):
        self.dollar = "li#l-price_dollar_rl span.info-value span.info-price"
        self.coin = "li#l-sekee span.info-value span.info-price"
        self.oil = "li#l-oil span.info-value span.info-price"
        self.gold = "li#l-geram18 span.info-value span.info-price"

    def get_prices(self):
        try:
            data = GetUrl("http://www.tgju.org/").value
            if data:
                soap = Soap(document=data).soap
                return dict(
                    dollar=soap.select_one(self.dollar).text,
                    coin=soap.select_one(self.coin).text,
                    oil=soap.select_one(self.oil).text,
                    gold=soap.select_one(self.gold).text
                )
            return False
        except:
            return False
