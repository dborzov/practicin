
def find_path(A, src, dest):
    queue = [src]
    cur = 0
    visited = {src:src}
    while(cur<len(queue)):
        for i in range(len(A)):
            if A[queue[cur]][i] == 0:
                continue
            if i in visited:
                continue
            visited[i] = queue[cur]
            queue.append(i)
        cur += 1
    if dest not in visited:
        raise Exception("Nodes not connected")

    path = [dest]
    while(path[-1] !=src):
        path.append(visited[path[-1]])
    return path


adj = {}
with open("adj_list.csv","rb") as csv_file:
    for line in csv_file:
        states = line.strip().split(",")
        adj[states[0]] = states[1:]

states = sorted([s for s in adj.keys()])
state_inds = {st:i for i, st in enumerate(states)}
A = [[1 if j_state in adj[i_state] else 0 for j_state in states] for i_state in states]
print [states[i] for i in find_path(A, state_inds["California"], state_inds["NY"])]
