#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import codecs

with open('episodes.csv','rb') as episode_list:
    for each in episode_list:
        wiki, title = each.split(' | ')
        with codecs.open('mentions/'+ wiki +'.txt',encoding='utf-8',mode='wb') as result_file:
            r = requests.get('http://adventuretime.wikia.com/wiki/'+wiki)
            content = "".join(r.text.splitlines())
            mentions = re.finditer('Finn', content)
            for mention in mentions:
                quote = content[max(0,mention.start()-10):min(mention.end()+10,len(content))]
                result_file.write(quote+'...\n')

