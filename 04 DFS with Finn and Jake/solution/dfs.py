import json


START_CHARACTER = u"Woobeewoo Villagers"

dict_characters = json.loads(open('../problem/graph_nodes.json','rb').read())
dict_episodes = json.loads(open('../problem/graph_vertices.json','rb').read())

def edges(for_character):
    return [(character, episode) for episode in dict_characters[for_character] for character in dict_episodes[episode] if not character == for_character]



discovered_characters = {}
logger = "started: \n"

def DFS(character_link):
    global logger
    logger += '      + ' +  character_link + '\n'
    discovered_characters[character_link] = logger
    for adjacent_character, link_episode in edges(character_link):
        if adjacent_character not in discovered_characters:
            logger += '----via ' +  link_episode + '\n'
            DFS(adjacent_character)


print edges(START_CHARACTER)
DFS(START_CHARACTER)
print 'Here:'
print discovered_characters['Goblins']
print "------------------------------------"
print "  Total: %s of %s characters discovered" % (len(discovered_characters.keys()), len(dict_characters.keys()))
