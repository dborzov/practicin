#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import codecs

characters = []
for line in codecs.open('characters.txt',encoding='utf-8',mode='rb').readlines():
    wiki, name = line.split(' | ')
    characters.append({'wiki':wiki,'name':name.rstrip()})


with open('episodes.csv','rb') as episode_list:
    for each in episode_list:
        wiki, title = each.split(' | ')
        print ' Reading episode: ', title
        with codecs.open('mentions/'+ wiki +'.txt',encoding='utf-8',mode='wb') as result_file:
            graph_file = codecs.open('graph/'+ wiki +'.txt',encoding='utf-8',mode='wb')
            r = requests.get('http://adventuretime.wikia.com/wiki/'+wiki)
            content = "".join(r.text.splitlines())
            for character in characters:
                mention = re.search('[\w\s]+<a href="/wiki/%s" title="%s">' % (character['wiki'],character['name']), content)
                if mention:
                    quote = content[max(0,mention.start()-100):min(mention.end()+100,len(content))]
                    result_file.write('\n\n'+character['name']+' \n----------------\n' +quote+'...\n')
                    graph_file.write(character['name'] + '\n')

