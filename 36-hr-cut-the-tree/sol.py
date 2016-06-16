import sys
sys.setrecursionlimit(100000)

inputer = open("input07.in", "rb")

def readline():
    return inputer.readline().rstrip()

print "loading nodes..."
num_vertex = int(readline())
vertices =  [int(val) for val in readline().split(" ")]
edges = {}
print "loading edges..."
for _ in range(num_vertex-1):
    v1, v2 = [int(val)-1 for val in readline().split(" ")]
    edges[v1] = edges.get(v1, []) + [v2]
    edges[v2] = edges.get(v2, []) + [v1]


weights = [val for val in vertices]
visited = {0: True}
queue = [0]
while len(queue) > 0:
    cur = queue[0]
    queue = queue[1:]
    for child in edge[cur]:
        if child in visited:
            continue
        queue.append(child)
        visited[child] = True
