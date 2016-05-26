#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("/root/ehsan/ToosCompanies")

from classes.get_url import GetUrl
from classes.soap import Soap
from models.mongodb.tables import TablesModel


tables = TablesModel().get_all()

for table in tables:
    data = GetUrl(url=table['base_link']).value
    doc = Soap(document=data).soap
    for i in range(1, len(table['trs'])):
        for td in table['trs'][i]['tds']:
            try:
                td['amount'] = doc.select_one(td['address']).text.encode('utf-8').strip()
            except:
                td['amount'] = 'نا مشخص'
    TablesModel(_id=table['_id']).update_trs(table['trs'])
