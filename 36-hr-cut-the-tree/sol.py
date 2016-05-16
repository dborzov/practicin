a = raw_input()
inputer = open("sample.in", "rb")
def readline():
    return inputer.readline().rstrip()

num_vertex = int(readline())
vertices =  [int(val) for val in readline().split(" ")]
edges = {}
for _ in range(num_vertex-1):
    v1, v2 = [int(val)-1 for val in readline().split(" ")]
    edges[v1] = edges.get(v1, []) + [v2]
    edges[v2] = edges.get(v2, []) + [v1]

visited = {}
def visit(position):
    visited[position] = True
    children = [(child, visit(child)) for child in edges[position] if not child in visited]
    total = vertices[position] + sum([weight for _child, weight in children])
    return total

total_top = visit(0)
print 'total weight: ', total_top
best_diff = 9999999999999
visited = {}
def traverse_diffs(position):
    global best_diff
    visited[position] = True
    children = [(child, traverse_diffs(child)) for child in edges[position] if not child in visited]
    for child, weight in children:
        diff = abs(total_top - 2*weight)
        if best_diff > diff:
            best_diff = diff
    total = vertices[position] + sum([weight for _child, weight in children])
    return total

traverse_diffs(0)
print 'lowest diff: ', best_diff

(1608)
