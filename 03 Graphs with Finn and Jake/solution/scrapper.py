#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Goes through the wiki page with the list of episodes and scraps for 
    episode names and wiki pages.
"""
import requests
import re
import json
import codecs


config = json.loads(open("../problem/consts.json","rb").read())

def scrap_characters():
    with open("../problem/characters.html","rb") as html_page:
        for line in html_page:
            match = re.search('href="/wiki/([\w\_]+)"\s+title="([\w\s]+)"',line)
            if match:
                print "Url: ", match.group(1), "\nName: ", match.group(2)


r = requests.get(config['list_of_episodes_url'])
source_html = "".join(r.text.splitlines())
# print source_html.encode('utf-8')
b =  re.finditer(u'<tr style="text-align: center; background: #f2f2f2">',source_html)
actual_data = []
for each in b:
    start_from = each.end()
    ender = start_from + re.search('</tr>',source_html[start_from:]).start()
    actual_data.append(source_html[start_from:ender])

with codecs.open('episodes.csv', encoding='utf-8',mode='wb') as output_file:
    for eacher in actual_data:
        c = re.search('<a href="/wiki/([\w\.%]+)" title="([\w\d\s\,\'\.!]+)">',eacher)
        if c:
            output_file.write(c.group(1) + ' | ' + c.group(2)+'\n')
            print 'Episode: ', c.group()

