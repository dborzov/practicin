import os
import json
import collections

episodes = {}
for episode in open('episodes.csv','rb'):
    wiki, title = episode.split(' | ')
    episodes[wiki] = title.rstrip()

graph = collections.defaultdict(list)
for filename in os.listdir('graph'):
    episode = filename[:-4]
    print 'Reading episode:', episode
    graph[episodes[episode]] = [character.rstrip() for character in open('graph/'+filename,'rb')] 


json_file = open('graph_vertices.json','wb')
json_file.write(json.dumps(graph,indent=4, separators=(',', ': ')))

