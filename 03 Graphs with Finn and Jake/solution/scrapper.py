#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re
import json

config = json.loads(open("../problem/consts.json","rb").read())

def scrap_characters():
    with open("../problem/characters.html","rb") as html_page:
        for line in html_page:
            match = re.search('href="/wiki/([\w\_]+)"\s+title="([\w\s]+)"',line)
            if match:
                print "Url: ", match.group(1), "\nName: ", match.group(2)


r = requests.get(config['list_of_episodes_url'])
source_html = r.text.rstrip().encode('utf-8')
print source_html.encode('utf-8')
episode_entries =  re.findall(u'<tr style="text-align: center; background: #f2f2f2">([.\n]+)</tr>',source_html)

for episode in episode_entries:
    print 'Heyo!'
    print episode.encode('utf-8')
