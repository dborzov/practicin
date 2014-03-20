#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import re
import json
import codecs

characters = {}
with open("../problem/characters.html","rb") as html_page:
    for line in html_page:
        match = re.search('href="/wiki/([\w\_]+)"\s+title="([\w\s]+)"',line)
        if match:
            characters[match.group(2)] = match.group(1)


character_file = open('characters.txt','wb')
for character in characters.keys():
    character_file.write(characters[character]+' | '+ character+'\n')