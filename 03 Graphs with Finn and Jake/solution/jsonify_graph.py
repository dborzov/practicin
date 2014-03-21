import os
import json
import collections
from ignore_characters import *





episodes = {}
for episode in open('episodes.csv','rb'):
    wiki, title = episode.split(' | ')
    episodes[wiki] = title.rstrip()

characters = collections.defaultdict(list)
for filename in os.listdir('graph'):
    episode = filename[:-4]
    print 'Reading episode:', episode
    for character in open('graph/'+filename,'rb'):
        if not character.rstrip() in IGNORE_CHARACTERS:
            characters[character.rstrip()].append(episodes[episode])

json_file = open('graph.json','wb')
json_file.write(json.dumps(characters,indent=4, separators=(',', ': ')))
