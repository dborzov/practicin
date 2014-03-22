import json


START_CHARACTER = u"Woobeewoo Villagers"

dict_characters = json.loads(open('../problem/graph_nodes.json','rb').read())
dict_episodes = json.loads(open('../problem/graph_vertices.json','rb').read())

def adj(for_character):
    return [(character, episode) for episode in dict_characters[for_character] for character in dict_episodes[episode] if not character == for_character]



i = 0
level = {START_CHARACTER:{'level':0, 'parent': None}}
frontier = [(START_CHARACTER, None)]
logger = "BFS started: \n"

while frontier:
    for each, parent in frontier:
        level[each] = {'level':i,'parent':parent}
        print '----------- %s visit: parent %s, level %i' % (each, parent, i)
    i += 1
    next = []
    for each, _ in frontier:
        for character, episode in adj(each):
            if character not in level:
                # print 'At level %s from %s to %s: through episode "%s"' % (i, each, character, episode)
                next.append((character, each))
    frontier = next



print "------------------------------------"
print "  Total: %s of %s characters discovered" % (len(level.keys()), len(dict_characters.keys()))
