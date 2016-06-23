#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from bson import ObjectId
sys.path.append("/root/ehsan/ToosCompanies")

from models.mongodb.companies import CompaniesModel

a = u""",شيروان,كارد,برد,,,,,مقواازضايعات كاغذومقوا،مقواي دوبلكس,,,,"مقواازضايعات كاغذومقوا،مقواي دوبلكس,",,___endl__
,چهره,سازان,ساختمان,,,,,,,,,"كارتن بسته بندي( واحدهاي تبديل ورق به كارتن ),",,___endl__
,نصراله,,دهقان,,,,,,,,,"كارتن بسته بندي( واحدهاي تبديل ورق به كارتن ),",,___endl__
,صنايع,سلولزي توس,پاپيروس,,,,,,,,,"كاغذ شبه كرافت ازضايعات كاغذ ومقوا,",,___endl__
,2دفترچه,پارس,نومشهد,,,,,,,,,"دفترچه تحرير,",,___endl__
,ظروف,مقوايي سي چشمه,طوس,,,,,,,,,"ظروف يكبارمصرف كاغذي,",,___endl__
,ساسان,,شوشتري,,,,,,,,,"شانه تخم مرغ مقوايي,",,___endl__
,كارتن,سازي دقت,مشهد,,,,,,,,,"كارتن بسته بندي( واحدهاي تبديل ورق به كارتن ),",,___endl__
,غلامرضا,,قندي,,,,,,,,,"سايركاغذهاي قالبگيري شده(شانه تخم مرغ وميوه جات مق,",,___endl__
,بهران,طلوع,شرق,(كارگاهي),,,,,,,,"ساكاروقطعات نسوز,",,___endl__
,سازه,هاي سلولزي امين مهد,خورشيد,,,,,,,,,"سايركاغذهاي قالبگيري شده(شانه تخم مرغ وميوه جات مق,",,___endl__
,شيروان,كارد برد,۲,,,,,,,,,"مقواي دوبلكس,",,___endl__
,پارت,مقواي,طوس,,,,,,,,,"مقواي دوبلكس,",,___endl__
,اختر,سمباده,خراسان,(۶۹),,,,,,,,"مقواازضايعات   كاغذومقوا,",,___endl__
,نارون,,مشهد,,,,,,,,,"پنجره چوبي,",,___endl__
,درودگري,,حيدريان,,,,,,,,,"درب وپنجره پيش ساخته فلزي,",,___endl__
,كارتن,سازي,افشين,,,,,,,,,"كارتن بسته بندي( واحدهاي تبديل ورق به كارتن ),",,"""
for line in a.split("___endl__"):
    __a = line.split(',')
    _name_1 = u" {}".format(__a[0]) if __a[0] != "" else ""
    _name_2 = u" {}".format(__a[1]) if __a[1] != "" else ""
    _name_3 = u" {}".format(__a[2]) if __a[2] != "" else ""
    _name_4 = u" {}".format(__a[3]) if __a[3] != "" else ""
    _name_5 = u" {}".format(__a[4]) if __a[4] != "" else ""
    __name = _name_1 + _name_2 + _name_3 + _name_4 + _name_5
    _description_1 = u" {}".format(__a[7]) if __a[7] != "" else ""
    _description_2 = u" {}".format(__a[8]) if __a[8] != "" else ""
    _description_3 = u" {}".format(__a[9]) if __a[9] != "" else ""
    _description_4 = u" {}".format(__a[10]) if __a[10] != "" else ""
    _description_5 = u" {}".format(__a[12]) if __a[12] != "" else ""
    __description = _description_1 + _description_2 + _description_3 + _description_4 + _description_5

    c = CompaniesModel()
    c.name = u"{}".format(__name)
    c.main_page = False
    c.slider = False
    c.description = u"{}".format(__description)
    c.logo = "default.jpg"
    c.images = []
    c.unit = ObjectId("574286276dd534700def2731")
    c.active = False
    c.industrial_town = ObjectId("576c2c816dd5341c616bdcba")
    c.address = ""
    c.phone = u"{}".format(__a[13])
    c.phone2 = u"{}".format(__a[14])
    c.mobile = u"{}".format(__a[6])
    c.fax = u"{}".format(__a[11])
    c.site = ""
    c.email = ""
    c.province = 10
    c.city = 122
    c.ceo = u"{}".format(__a[5])
    c.owner = ""
    c.insert()
